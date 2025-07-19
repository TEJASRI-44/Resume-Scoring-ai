import streamlit as st
from utils.file_handler import extract_text_from_pdf
from utils.similarity_checker import calculate_similarity_score

st.set_page_config(page_title="Resume Screening Bot", layout="centered")

st.title("📄 Resume Screening Bot")
st.markdown("Paste your **Job Description** below (max: 1000 words) and upload a **resume PDF** to check the match score.")

# --- Job Description Text Area ---
jd_input = st.text_area("📝 Enter Job Description (Max 1000 words)", height=250)

# --- Word Count Warning ---
word_count = len(jd_input.split())
if word_count > 1000:
    st.warning(f"❗ Your input has {word_count} words. Please reduce to 1000 or less.")
    jd_input = ""  # Ignore input if over limit

# --- Resume PDF Upload ---
resume_file = st.file_uploader("📎 Upload Resume (PDF)", type="pdf")

# --- Calculate Similarity ---
if jd_input and resume_file:
    resume_text = extract_text_from_pdf(resume_file)
    score = calculate_similarity_score(jd_input, resume_text)
    
    st.success(f"✅ Resume Match Score: **{score}%**")
elif jd_input and not resume_file:
    st.info("Please upload a resume file to continue.")
elif resume_file and not jd_input:
    st.info("Please paste your job description above.")
