import pdfplumber
from docx import Document
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np
from collections import Counter
import re

# Load the SpaCy English model and BERT model
nlp = spacy.load("en_core_web_sm")
bert_model = SentenceTransformer('all-MiniLM-L6-v2')

# Hardcoded Skill Taxonomy Engine for Aliases
SKILL_TAXONOMY = {
    "javascript": ["js", "es6", "vanilla js", "ecmascript"],
    "react": ["reactjs", "react.js", "react native"],
    "node.js": ["node", "nodejs", "node js"],
    "vue.js": ["vue", "vuejs"],
    "angular": ["angularjs", "angular.js"],
    "python": ["python3", "python 3"],
    "machine learning": ["ml"],
    "artificial intelligence": ["ai"],
    "amazon web services": ["aws"],
    "google cloud platform": ["gcp"],
    "c#": ["csharp", "c sharp"],
    "c++": ["cpp", "c plus plus"],
    "postgresql": ["postgres", "pls-sql"],
    "typescript": ["ts"]
}

def normalize_skill(skill_str):
    """
    Takes a raw string, lowercases it, and checks if it's an alias in the taxonomy.
    If it is, returns the standardized root term.
    """
    cleaned = skill_str.lower().strip()
    
    for root_skill, aliases in SKILL_TAXONOMY.items():
        if cleaned == root_skill or cleaned in aliases:
            return root_skill
            
    return cleaned


# Function to extract text from PDF files
def extract_text_from_pdf(pdf_path):
    """Extracts text from PDF files."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text


# Function to extract text from DOCX files
def extract_text_from_docx(docx_path):
    """Extracts text from DOCX files."""
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


# Function to extract relevant skills/keywords using SpaCy NLP features
def extract_skills(text):
    """Extracts potential skills and required keywords from text using noun chunks and entities."""
    doc = nlp(text)
    skills = set()
    
    # Extract noun chunks combining important lemma tokens
    for chunk in doc.noun_chunks:
        words = [token.lemma_.lower() for token in chunk if not token.is_stop and not token.is_punct and token.is_alpha]
        if words:
            phrase = ' '.join(words)
            if len(phrase) > 2:
                skills.add(normalize_skill(phrase))
                
    # Also include individual strategic nouns/proper nouns
    for token in doc:
        if token.pos_ in ['PROPN', 'NOUN'] and not token.is_stop and token.is_alpha and len(token.text) > 2:
            skills.add(normalize_skill(token.lemma_))
            
    return list(skills)


def extract_years_of_experience(text):
    """
    Extracts explicit statements of Years of Experience using regex.
    Returns the maximum value found.
    """
    patterns = [
        r'(\d+)\+?\s*years?\s*of\s*experience',
        r'experience:?\s*(\d+)\+?\s*years?',
        r'(\d+)\+?\s*yrs\s*exp',
    ]
    max_years = 0
    text_lower = text.lower()
    for pattern in patterns:
        matches = re.finditer(pattern, text_lower)
        for match in matches:
            try:
                years = int(match.group(1))
                if 0 < years < 50: # Sanity check for realistic years
                    if years > max_years:
                        max_years = years
            except ValueError:
                pass
    return max_years


# Function to chunk text to bypass BERT 512-token limit
def chunk_text(text, max_words=100):
    """Splits full text into appropriately sized chunks for Sentences Transformers."""
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        # Check if adding this sentence exceeds roughly max_words (approximation by split length)
        if len(current_chunk.split()) + len(sentence.split()) > max_words:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = sentence
        else:
            current_chunk += " " + sentence if current_chunk else sentence
            
    if current_chunk:
        chunks.append(current_chunk)
        
    return chunks if chunks else [text]


# Function to calculate keyword/skill match score
def calculate_skill_match(resume_skills, job_skills):
    """Calculates the skill match score based on overlapping/substring keywords."""
    resume_skills_set = set(resume_skills)
    job_skills_set = set(job_skills)
    
    matched = set()
    for js in job_skills_set:
        if js in resume_skills_set:
            matched.add(js)
        else:
            # Substring matching (e.g., job wanted "python sql" and resume has "python")
            for rs in resume_skills_set:
                if js in rs or rs in js:
                    matched.add(js)
                    break

    # Normalize logic
    score = len(matched) / max(len(job_skills_set), 1)
    # Clip score at 1.0 
    score = min(score, 1.0)
    return score, list(matched)


# Function to match resumes to job descriptions utilizing semantic chunks and broad keywords
def match_resume_to_job(resume_texts_raw, resume_skills_list, job_description_raw, job_skills):
    # Process job embeddings by taking the mean of its chunks
    job_chunks = chunk_text(job_description_raw)
    job_embeddings = bert_model.encode(job_chunks)
    mean_job_embedding = job_embeddings.mean(axis=0).reshape(1, -1)
    
    similarities_list = []
    
    for resume_raw in resume_texts_raw:
        resume_chunks = chunk_text(resume_raw)
        resume_embeddings = bert_model.encode(resume_chunks)
        
        # Calculate cosine similarity of each resume chunk to the overall job embedding
        sims_to_job = cosine_similarity(resume_embeddings, mean_job_embedding).flatten()
        
        # Take the top N scoring chunks and average their similarity 
        # (Assuming best bits of a resume mapping to the JD)
        top_k = min(3, len(sims_to_job))
        top_sims = sorted(sims_to_job, reverse=True)[:top_k]
        avg_top_sim = sum(top_sims) / top_k if top_k > 0 else 0.0
        
        similarities_list.append(avg_top_sim)

    # Calculate skill matches
    skill_match_results = [calculate_skill_match(resume_skills, job_skills) for resume_skills in resume_skills_list]
    skill_match_scores = [result[0] for result in skill_match_results]
    matched_skills_list = [result[1] for result in skill_match_results]

    combined_scores = []
    for sim, skill_score in zip(similarities_list, skill_match_scores):
        sim_clamped = max(0.0, float(sim))
        
        # New Scoring Weighting:
        # Semantic Chunk matching is 60%, Broad Keyword match is 40%
        combined_score = (sim_clamped * 0.6) + (skill_score * 0.4)
        combined_scores.append(combined_score)

    return combined_scores, similarities_list, skill_match_scores, matched_skills_list


def generate_actionable_feedback(candidate_yoe, required_yoe, matched_keywords, required_keywords, current_overall_score):
    """
    Analyzes the candidate's deficits against the JD and generates specific string suggestions
    along with a projected algorithmic score increase.
    """
    suggestions = []
    
    # 1. Missing Keyword Analysis
    matched_set = set(k.lower() for k in matched_keywords)
    missing = [k for k in required_keywords if k.lower() not in matched_set]
    
    if missing:
        # Calculate potential score bump if they add 2 keywords
        potential_bump = min(15, len(missing) * 4) # Estimate
        projected_score = min(100, int(current_overall_score + potential_bump))
        
        top_missing = missing[:3]
        missing_str = ", ".join(f"'{k}'" for k in top_missing)
        
        suggestions.append({
            "type": "keywords",
            "message": f"You are missing key requirements like {missing_str}. We highly recommend tailoring your experience bullets to include these terms.",
            "projection": f"Adding these could boost your match score to ~{projected_score}%."
        })
    else:
        suggestions.append({
            "type": "success",
            "message": "Excellent! You hit 100% of the keyword requirements.",
            "projection": None
        })
        
    # 2. Years of Experience Analysis
    if required_yoe > 0 and candidate_yoe < required_yoe:
        diff = required_yoe - candidate_yoe
        projected_score = min(100, int(current_overall_score + 10)) # Recoup the -10 penalty
        suggestions.append({
            "type": "experience",
            "message": f"The job requires {required_yoe} years of experience, but we only detected {candidate_yoe}. Ensure your employment dates are clearly formatted (e.g., 'Jan 2020 - Present').",
            "projection": f"Clarifying your timeline could recover your score back to ~{projected_score}%."
        })
        
    # 3. Structural Advice (Generic)
    if current_overall_score < 60:
         suggestions.append({
            "type": "structure",
            "message": "Your low semantic score indicates the context of your achievements doesn't align with the JD. Try rewriting your bullet points to closely match the duties described in the job posting.",
            "projection": None
         })
         
    return suggestions


# Function to rank candidates based on combined scores and provide detailed explanations
def rank_candidates(resume_paths, job_description):
    resume_texts_raw = []
    resume_skills_list = []
    resume_yoe_list = []
    
    # Try to parse requirement from JD
    job_yoe_required = extract_years_of_experience(job_description)
    
    for path in resume_paths:
        if path.endswith('.pdf'):
            resume_text = extract_text_from_pdf(path)
        elif path.endswith('.docx'):
            resume_text = extract_text_from_docx(path)
        else:
            print(f"Unsupported file format: {path}")
            continue

        resume_texts_raw.append(resume_text)

        # Extract skills directly from raw text for robust matching
        resume_skills = extract_skills(resume_text)
        resume_skills_list.append(resume_skills)
        
        # Extract YoE explicitly stated in the resume
        yoe = extract_years_of_experience(resume_text)
        resume_yoe_list.append(yoe)

    job_skills = extract_skills(job_description)

    combined_scores, similarities, skill_match_scores, matched_skills_list = match_resume_to_job(
        resume_texts_raw, resume_skills_list, job_description, job_skills)

    ranked_candidates = sorted(
        zip(resume_paths, combined_scores, similarities, skill_match_scores, matched_skills_list, resume_yoe_list),
        key=lambda x: x[1], reverse=True
    )

    results = []
    # Structure data for JSON API response
    for resume, combined_score, bert_similarity_score, skill_match_score, matched_skills, yoe in ranked_candidates:
        
        # YoE Scoring Logic (if JD requires YoE, penalize if candidate lacks it, reward if they exceed it)
        yoe_bonus = 0
        if job_yoe_required > 0:
            if yoe >= job_yoe_required:
                yoe_bonus = 5 # Small algorithmic bump for meeting criteria
            else:
                yoe_bonus = -10 # Penalty for not meeting hard baseline

        final_overall_score = float((combined_score * 100) + yoe_bonus)
        final_overall_score = max(0.0, min(100.0, final_overall_score)) # Clamp 0-100

        # Generate Insights
        insights = generate_actionable_feedback(
            yoe, 
            job_yoe_required, 
            matched_skills, 
            job_skills, 
            final_overall_score
        )

        results.append({
            "filename": resume,
            "overall_score": final_overall_score,
            "semantic_score": float(bert_similarity_score * 100),
            "keyword_score": float(skill_match_score * 100),
            "matched_keywords": matched_skills,
            "required_keywords": job_skills,
            "candidate_yoe": yoe,
            "required_yoe": job_yoe_required,
            "actionable_insights": insights
        })

    return results


# Main function to demonstrate the ATS algorithm
def main():
    """Main function to run the ATS algorithm."""
    # Example job description
    job_description = """As a key member of the Data Analytics team, you will enjoy rolling up your sleeves to solve complex business questions through data. You will navigate through unique data sets to build and maintain data pipelines, monitor and optimize data processes, and lead feature engineering for our modeling data sets. The DA team proactively works to identify, prioritize and conduct analysis that drives meaningful insight to achieve our performance objectives.
Able to drive successful completion of deliverables and analytic deliverables
Ensures quality and reliability of data obtained from client sources and offline data sources (ensuring that data contains required information for analytics and modeling)
Build and maintain complex data pipelines
Confirm that the AI team is able to optimize the performance metric desired by the client and that the data provided by the client is sufficient (completeness and usability)
Drill down on results (problem-solving analysis) and conduct custom analysis
Reconcile data and procedures with internal teams
Define and improve data joining procedures for new and existing deployments
Ensure data integrity on review of historical data
Bachelors or Masters in Computer Science, Mathematics, Economics, Physics, Engineering or related quantitative field.
Minimum 2-4 years of experience in data analytics, data modelling, SQL scripting, statistics, ETL and Data Warehousing
The ability to manage internal stakeholders in ensuring that data is received and managed in a timely and efficient manner
Experience in a data-centric role in more than one industry
Ability to work under pressure
Strong knowledge and understanding of statistical concepts
Strong problems solving and critical thinking skills
The ability to convey mathematical concepts in a meaningful way to business clients and internal team members
The ability to work independently and in a team environment
The ability to work effectively across functions, levels, and disciplines
Knowledge of SQL required
Knowledge of R or Python required
"""

    resume_paths = [
        "Junaid-Iqbal-Resume.pdf",  # Replace with actual paths
        "CV-Source.docx",  # Replace with actual paths
    ]

    rank_candidates(resume_paths, job_description)


if __name__ == "__main__":
    main()
