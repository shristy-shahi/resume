# 📄 Resume Screening App

A machine learning–based **resume classification web app** built with **Streamlit**.  
Upload a resume in `.pdf` or `.docx` format, and the app will automatically analyze the content and predict the job category.  

---

## 📖 Overview
This project helps recruiters, HR teams, and job portals by automatically classifying resumes into categories such as:
- Data Science  
- Network Security Engineer  
- Advocate  
- Health & Fitness  

It uses natural language processing (NLP) techniques and trained ML models to achieve up to **99.7% accuracy**.  

---

## ✨ Features
- 📂 Upload resumes in **PDF** or **DOCX** format  
- 🧹 Cleans and preprocesses text (removes URLs, punctuation, stopwords, etc.)  
- 🤖 Resume classification using ML models (KNN, RandomForest)  
- 🎯 High accuracy (~99.7% with RandomForest)  
- 💻 User-friendly **Streamlit web interface**  

---

## 🛠️ Tech Stack
- **Python 3.8+**  
- **Streamlit** – frontend web app  
- **scikit-learn** – ML model training and evaluation  
- **pypdf**, **python-docx** – resume parsing  
- **Pickle** – model persistence  

---

## ⚡ Installation & Setup

Clone the repository:
```bash
git clone https://github.com/shristy-shahi/resume.git
cd resume
Create and Activate a Virtual Environment:
python -m venv venv
.\venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux


Install Dependencies:
pip install -r requirements.txt

Contents of requirements.txt:
streamlit==1.45.1
python-docx==1.1.2
pypdf==5.5.0
scikit-learn==1.6.1
pandas==2.2.3
```
---



Built by ❤️ shristy
