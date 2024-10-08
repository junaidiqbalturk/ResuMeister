import pdfplumber
from docx import Document
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from collections import Counter

# Load the SpaCy English model and BERT model
nlp = spacy.load("en_core_web_sm")
bert_model = SentenceTransformer('bert-base-nli-mean-tokens')


# Function to extract text from PDF files
def extract_text_from_pdf(pdf_path):
    """Extracts text from PDF files."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


# Function to extract text from DOCX files
def extract_text_from_docx(docx_path):
    """Extracts text from DOCX files."""
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


# Function to preprocess text by removing stopwords and punctuation using SpaCy
def preprocess_text(text):
    """Preprocesses text by removing stopwords and punctuation."""
    doc = nlp(text)
    filtered_words = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(filtered_words)


# Function to extract skills using SpaCy NER
def extract_skills(text):
    """Extracts skills from text using SpaCy named entity recognition."""
    doc = nlp(text)
    skills = []
    for ent in doc.ents:
        if ent.label_ == "ORG" or ent.label_ == "PRODUCT":  # This assumes skills are labeled as ORG or PRODUCT
            skills.append(ent.text.lower())
    return skills


# Function to calculate skill match score
def calculate_skill_match(resume_skills, job_skills):
    """Calculates the skill match score based on overlapping skills."""
    resume_skill_counts = Counter(resume_skills)
    job_skill_counts = Counter(job_skills)
    common_skills = resume_skill_counts & job_skill_counts  # Intersection of skills
    return sum(common_skills.values()) / max(len(job_skills), 1), list(
        common_skills.elements())  # Normalized score and matched skills


# Function to match resumes to job descriptions using BERT embeddings and skill matching
def match_resume_to_job(resume_texts, resume_skills_list, job_description_text, job_skills):
    # BERT Embeddings
    resume_embeddings = bert_model.encode(resume_texts)
    job_description_embedding = bert_model.encode([job_description_text])[0]

    # Calculate BERT similarity scores
    similarities = cosine_similarity(resume_embeddings, [job_description_embedding])

    # Skill Match Scores and Matched Skills
    skill_match_results = [calculate_skill_match(resume_skills, job_skills) for resume_skills in resume_skills_list]
    skill_match_scores = [result[0] for result in skill_match_results]
    matched_skills_list = [result[1] for result in skill_match_results]

    # Combine BERT similarity score and skill match score
    combined_scores = [(sim * 0.7 + skill_score * 0.3) for sim, skill_score in
                       zip(similarities.flatten(), skill_match_scores)]

    return combined_scores, similarities.flatten(), skill_match_scores, matched_skills_list


# Function to rank candidates based on combined scores and provide detailed explanations
def rank_candidates(resume_paths, job_description):
    resume_texts = []
    resume_skills_list = []
    for path in resume_paths:
        if path.endswith('.pdf'):
            resume_text = extract_text_from_pdf(path)
        elif path.endswith('.docx'):
            resume_text = extract_text_from_docx(path)
        else:
            print(f"Unsupported file format: {path}")
            continue

        preprocessed_text = preprocess_text(resume_text)
        resume_texts.append(preprocessed_text)

        # Extract skills from the resume
        resume_skills = extract_skills(preprocessed_text)
        resume_skills_list.append(resume_skills)

    preprocessed_job_description = preprocess_text(job_description)
    job_skills = extract_skills(preprocessed_job_description)

    combined_scores, similarities, skill_match_scores, matched_skills_list = match_resume_to_job(
        resume_texts, resume_skills_list, preprocessed_job_description, job_skills)

    ranked_candidates = sorted(
        zip(resume_paths, combined_scores, similarities, skill_match_scores, matched_skills_list),
        key=lambda x: x[1], reverse=True
    )

    # Print detailed explanations for each resume
    for resume, combined_score, bert_similarity_score, skill_match_score, matched_skills in ranked_candidates:
        print(f"Resume: {resume}")
        print(f"Overall Score: {combined_score:.2f}")
        print(f"Explanation:")
        print(
            f"  - BERT Similarity Score: {bert_similarity_score:.2f} (How closely the resume's language matches the job description)")
        print(
            f"  - Skill Match Score: {skill_match_score:.2f} (How many job-required skills are present in the resume)")
        print(f"  - Matched Skills: {', '.join(matched_skills)}")
        print(f"  - Required Skills from Job Description: {', '.join(job_skills)}")
        print()

    return ranked_candidates


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

    ranked_candidates = rank_candidates(resume_paths, job_description)


if __name__ == "__main__":
    main()
