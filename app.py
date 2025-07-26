import streamlit as st
from resume_parser import extract_text_from_pdf
from job_matcher import match_job_role

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer & Job Matcher")
st.write("Upload your resume to find the best matching job role based on your skills and experience.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    with open("data/uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Resume uploaded successfully!")

    resume_text = extract_text_from_pdf("data/uploaded_resume.pdf")
    st.subheader("🔍 Extracted Resume Text")
    st.write(resume_text[:1000] + "...")  # limit preview

    matched_roles = match_job_role(resume_text)

    st.subheader("🎯 Best Matching Roles")
    for role, score in matched_roles[:3]:
        st.write(f"✅ {role} — {round(score*100, 2)}% match")

