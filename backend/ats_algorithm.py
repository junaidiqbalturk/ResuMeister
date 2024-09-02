import pdfplumber
from docx import Document
import re
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import os
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
        if ent.label_ in ["SKILL"]:  # Assuming "SKILL" is a label in the NER model
            skills.append(ent.text.lower())
    return skills


# Function to calculate skill match score
def calculate_skill_match(resume_skills, job_skills):
    """Calculates the skill match score based on overlapping skills."""
    resume_skill_counts = Counter(resume_skills)
    job_skill_counts = Counter(job_skills)
    common_skills = resume_skill_counts & job_skill_counts  # Intersection of skills
    return sum(common_skills.values()) / max(len(job_skills), 1)  # Normalized score


# Function to match resumes to job descriptions using BERT embeddings and skill matching
def match_resume_to_job(resume_texts, resume_skills_list, job_description_text, job_skills):
    """Matches resumes to job descriptions using BERT embeddings and skill matching."""
    # BERT Embeddings
    resume_embeddings = bert_model.encode(resume_texts)
    job_description_embedding = bert_model.encode([job_description_text])[0]

    # Calculate cosine similarity between resume embeddings and job description embedding
    similarities = cosine_similarity(resume_embeddings, [job_description_embedding])

    # Skill Match Scores
    skill_match_scores = [calculate_skill_match(resume_skills, job_skills) for resume_skills in resume_skills_list]

    # Combine BERT similarity score and skill match score
    combined_scores = [(sim * 0.7 + skill_score * 0.3) for sim, skill_score in
                       zip(similarities.flatten(), skill_match_scores)]

    return combined_scores


# Function to rank candidates based on combined scores
def rank_candidates(resume_paths, job_description):
    """Ranks candidates based on combined scores from BERT similarity and skill matching."""
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
        resume_skills = extract_skills(resume_text)
        resume_skills_list.append(resume_skills)

    preprocessed_job_description = preprocess_text(job_description)
    job_skills = extract_skills(job_description)

    # Calculate scores
    scores = match_resume_to_job(resume_texts, resume_skills_list, preprocessed_job_description, job_skills)

    # Combine paths and scores into tuples
    ranked_candidates = list(zip(resume_paths, scores))

    # Sort candidates by score
    ranked_candidates = sorted(ranked_candidates, key=lambda x: x[1], reverse=True)

    return ranked_candidates


# Main function to demonstrate the ATS algorithm
def main():
    """Main function to run the ATS algorithm."""
    # Example job description
    job_description = "Data Scientist with experience in Python, Machine Learning, and Data Analysis."

    resume_paths = [
        "Junaid-Iqbal-Resume.pdf",  # Replace with actual paths
        "CV-Source.docx",  # Replace with actual paths
    ]

    ranked_candidates = rank_candidates(resume_paths, job_description)

    # Output results with explanations
    for resume, score in ranked_candidates:
        # Extract the skills and BERT scores
        resume_text = extract_text_from_pdf(resume) if resume.endswith('.pdf') else extract_text_from_docx(resume)
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        skill_match_score = calculate_skill_match(resume_skills, job_skills)
        bert_similarity_score = score  # Combined score already includes BERT similarity

        # Print resume information with explanations
        print(f"Resume: {resume}")
        print(f"Score: {score:.2f}")
        print(
            f"Explanation: Skill Match Score: {skill_match_score:.2f}, BERT Similarity Score: {bert_similarity_score:.2f}")
        print("-" * 40)


if __name__ == "__main__":
    main()
