import streamlit as st
import pickle
from docx import Document
from pypdf import PdfReader
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

# Load the saved models and encoder
try:
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))
    svc_model = pickle.load(open('clf.pkl', 'rb'))
    le = pickle.load(open('encoder.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error: {e}. Please ensure clf.pkl, tfidf.pkl, and encoder.pkl are in the same directory as app.py.")
    st.stop()

# Function to clean resume text
def cleanResume(resumeText):
    resumeText = re.sub(r'http\S+\s*', ' ', resumeText)  # Remove URLs
    resumeText = re.sub(r'RT|cc', ' ', resumeText)  # Remove RT and cc
    resumeText = re.sub(r'#\S+', ' ', resumeText)  # Remove hashtags
    resumeText = re.sub(r'@\S+', ' ', resumeText)  # Remove mentions
    resumeText = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # Remove punctuations
    resumeText = re.sub(r'\s+', ' ', resumeText)  # Remove extra whitespace
    resumeText = resumeText.lower()  # Convert to lowercase
    return resumeText

# Function to extract text from PDF
def extract_text_from_pdf(file):
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + " "
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

# Function to extract text from DOCX
def extract_text_from_docx(file):
    try:
        doc = Document(file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + " "
        return text
    except Exception as e:
        st.error(f"Error reading DOCX: {e}")
        return None

# Function to predict the category of a resume
def pred(input_resume):
    cleaned_text = cleanResume(input_resume)
    vectorized_text = tfidf.transform([cleaned_text])
    vectorized_text = vectorized_text.toarray()
    predicted_category = svc_model.predict(vectorized_text)
    predicted_category_name = le.inverse_transform(predicted_category)
    return predicted_category_name[0]

# Streamlit app
st.title("Resume Screening App")
st.write("Upload a resume in PDF or DOCX format to predict its category.")

# File uploader
uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx"])

if uploaded_file is not None:
    try:
        # Extract text based on file type
        if uploaded_file.name.endswith('.pdf'):
            resume_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith('.docx'):
            resume_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload a PDF or DOCX file.")
            resume_text = None

        if resume_text:
            # Predict category
            category = pred(resume_text)
            st.success(f"The resume belongs to the category: **{category}**")
        else:
            st.error("Could not extract text from the uploaded file.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please upload a resume file to get started.")