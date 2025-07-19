import streamlit as st
from utils.file_handler import extract_text_from_pdf
from utils.similarity_checker import calculate_similarity_score

st.set_page_config(page_title="Resume Screening Bot", layout="centered")

st.title("📑 Resume Screening Bot")
st.markdown("### Paste Job Description and Upload Multiple Resumes to Get Match Scores")

# --- Job Description Input ---
jd_input = st.text_area("📝 Job Description (Max 1000 words)", height=250)
word_count = len(jd_input.split())

if word_count > 1000:
    st.warning(f"❗ Word limit exceeded ({word_count}/1000). Please reduce your job description.")
    jd_input = ""  # clear jd if over limit

# --- Resume Upload (Multiple Allowed) ---
resume_files = st.file_uploader("📎 Upload Resume PDFs", type="pdf", accept_multiple_files=True)

# --- Run Matching ---
if jd_input and resume_files:
    st.markdown("## 📊 Match Scores")
    results = []

    for file in resume_files:
        resume_text = extract_text_from_pdf(file)
        score = calculate_similarity_score(jd_input, resume_text)
        results.append({"Resume": file.name, "Score": f"{score}%"})

    # Display in table
    st.table(results)
elif jd_input and not resume_files:
    st.info("Upload at least one resume PDF.")
elif resume_files and not jd_input:
    st.info("Paste the job description above.")
