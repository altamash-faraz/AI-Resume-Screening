import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set page title and icon
st.set_page_config(page_title="AI Resume Screener", page_icon="📄", layout="wide")

st.markdown("""
    <style>
    .title {text-align: center; font-size: 40px; font-weight: bold; color: #4CAF50;}
    .subheader {text-align: center; font-size: 22px; color: #555;}
    .uploaded-file {color: #1E88E5; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# Title and subheader
st.markdown('<p class="title">📄 AI Resume Screening & Ranking System</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Rank resumes based on job descriptions using AI-powered similarity matching</p>', unsafe_allow_html=True)

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        extracted_text = page.extract_text()
        if extracted_text:  # Avoids NoneType errors
            text += extracted_text + " "
    return text.strip()

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes  
    vectorizer = TfidfVectorizer(stop_words="english")  
    vectors = vectorizer.fit_transform(documents).toarray()
    job_description_vector = vectors[0]  
    resume_vectors = vectors[1:]  
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    return cosine_similarities

# Layout with columns
col1, col2 = st.columns(2)

# Job Description Input
with col1:
    st.header("📝 Job Description")
    job_description = st.text_area("Enter the job description", height=180)

# File Uploader
with col2:
    st.header("📂 Upload Resumes")
    uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("📊 Ranking Resumes")

    resumes = []
    file_names = []

    # Show uploaded files
    with st.expander("📜 Uploaded Files"):
        for file in uploaded_files:
            st.markdown(f'<p class="uploaded-file">✔️ {file.name}</p>', unsafe_allow_html=True)
            text = extract_text_from_pdf(file)
            if text:  
                resumes.append(text)
                file_names.append(file.name)
    
    if resumes:
        with st.spinner("🔍 Analyzing and ranking resumes..."):
            scores = rank_resumes(job_description, resumes)
        
        # Creating DataFrame with color styling
        results = pd.DataFrame({"Resume": file_names, "Score": scores})
        results = results.sort_values(by="Score", ascending=False)
        
        # Color-coding the ranking table
        def color_map(val):
            color = "#66BB6A" if val > 0.7 else "#FFCA28" if val > 0.4 else "#E57373"
            return f"background-color: {color}; color: white; text-align: center"

        st.dataframe(results.style.applymap(color_map, subset=["Score"]))

    else:
        st.error("⚠️ No text extracted from the uploaded PDFs. Try different files.")
