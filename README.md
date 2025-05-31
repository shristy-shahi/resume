Resume Screening App

📋 Project Overview
The Resume Screening App is a machine learning-powered web application that automatically classifies resumes into job categories such as Data Science, Health and Fitness, Network Security Engineer, and Advocate. Built with Streamlit, the app allows users to upload resumes in .pdf or .docx format, extracts text, preprocesses it, and predicts the appropriate category using a trained classifier.
The project uses a K-Nearest Neighbors (KNN) or RandomForestClassifier model, achieving up to 99.76% accuracy with RandomForest. Text is processed using TF-IDF vectorization, and categories are mapped with a label encoder, all stored in pickle files (clf.pkl, tfidf.pkl, encoder.pkl).
✨ Features

Resume Upload: Supports .pdf and .docx formats.
Text Extraction: Uses pypdf for PDFs and python-docx for DOCX files.
Text Preprocessing: Cleans text by removing URLs, hashtags, mentions, punctuation, and extra whitespace.
Category Prediction: Predicts job categories using a trained ML model.
Intuitive Interface: Streamlit-based web app with a user-friendly UI.
Error Handling: Robust handling for file errors and unsupported formats.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📁 Project Structure
resume_tracker/
├── src/
│   ├── app.py              # Streamlit app script
│   ├── clf.pkl             # Trained classifier (KNN or RandomForest)
│   ├── tfidf.pkl          # TF-IDF vectorizer
│   ├── encoder.pkl        # Label encoder
├── notebooks/
│   ├── start.ipynb         # Jupyter notebook for model training
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation

🛠️ Prerequisites

Python: 3.12 or higher
Virtual Environment: Recommended for dependency isolation
Packages: Listed in requirements.txt
Optional: Tesseract OCR for scanned PDFs (requires pytesseract)

🚀 Installation

Clone the Repository:
git clone https://github.com/your-username/resume_tracker.git
cd resume_tracker


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


Verify Files:Ensure clf.pkl, tfidf.pkl, and encoder.pkl are in the src/ directory. Generate them by running notebooks/start.ipynb if needed.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 Usage

Run the App:
cd src
streamlit run app.py

This opens a browser at http://localhost:8080.

Upload a Resume:

Upload a .pdf or .docx resume via the file uploader.
The app extracts text and predicts the job category (e.g., "Data Science").
Example output:The resume belongs to the category: Data Science



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧠 Model Details

Dataset: Labeled resumes from various job categories (see start.ipynb).
Preprocessing: Text cleaning (URLs, hashtags, punctuation removal) and TF-IDF vectorization.
Model: KNN or RandomForestClassifier (RandomForest: 99.76% accuracy).
Files:
clf.pkl: Trained classifier
tfidf.pkl: TF-IDF vectorizer
encoder.pkl: Label encoder



To use RandomForestClassifier:
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
rf_model = OneVsRestClassifier(RandomForestClassifier())
rf_model.fit(X_train, y_train)
pickle.dump(rf_model, open('clf.pkl', 'wb'))

🐛 Troubleshooting

Import Errors:pip install python-docx pypdf streamlit scikit-learn pandas


Pickle File Errors:Ensure pickle files are in src/. Recreate them using start.ipynb.
PDF Extraction Issues:For scanned PDFs, install pdfplumber:pip install pdfplumber

Update app.py’s extract_text_from_pdf (see code comments).
Model Compatibility:Run start.ipynb in the same environment.

🌟 Future Enhancements

Add confidence scores for predictions.
Support OCR for scanned PDFs using pytesseract.
Enhance UI with category descriptions and sidebar.
Include job recommendation features.

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a pull request.

Please follow the Code of Conduct and report issues via GitHub Issues.
📜 License
This project is licensed under the MIT License.
📬 Contact
For questions or feedback, contact:

Your Name: your.email@example.com
GitHub: your-username


Built with ❤️ using Python and Streamlit
