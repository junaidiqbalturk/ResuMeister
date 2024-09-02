import pdfplumber
from docx import Document
import spacy
import torch
from transformers import BertTokenizer, BertModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


# Function to extract text from PDF files
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


# Function to extract text from DOCX files
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


# Function to preprocess text by removing stopwords and punctuation using SpaCy
def preprocess_text(text):
    doc = nlp(text)
    filtered_words = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(filtered_words)


# Function to get BERT embeddings
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy().flatten()


# Function to match resumes to job descriptions using BERT embeddings
def match_resume_to_job(resume_texts, job_description_text):
    job_description_embedding = get_bert_embedding(job_description_text)
    resume_embeddings = [get_bert_embedding(text) for text in resume_texts]
    similarities = cosine_similarity(resume_embeddings, [job_description_embedding])
    return similarities.flatten()


# Function to rank candidates based on similarity scores
def rank_candidates(resume_paths, job_description):
    resume_texts = []
    for path in resume_paths:
        if path.endswith('.pdf'):
            resume_texts.append(preprocess_text(extract_text_from_pdf(path)))
        elif path.endswith('.docx'):
            resume_texts.append(preprocess_text(extract_text_from_docx(path)))
        else:
            print(f"Unsupported file format: {path}")
            continue

    preprocessed_job_description = preprocess_text(job_description)
    scores = match_resume_to_job(resume_texts, preprocessed_job_description)
    ranked_candidates = sorted(zip(resume_paths, scores), key=lambda x: x[1], reverse=True)
    return ranked_candidates


# Main function to demonstrate the ATS algorithm
def main():
    # Example job description
    job_description = "Data Scientist with experience in Python, Machine Learning, and Data Analysis."

    resume_paths = [
        "Junaid-Iqbal-Resume.pdf",  # Replace with actual paths
        "CV-Source.docx",  # Replace with actual paths
    ]

    ranked_candidates = rank_candidates(resume_paths, job_description)
    for resume, score in ranked_candidates:
        print(f"Resume: {resume}, Score: {score:.2f}")


if __name__ == "__main__":
    main()
