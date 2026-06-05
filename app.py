import streamlit as st
from interview_generator import generate_questions

st.title("🎯 AI Interview Coach")

st.write("Enter a job title and job description to generate interview preparation questions.")

# Inputs
job_title = st.text_input("Job Title")

level = st.selectbox(
    "Experience Level",
    ["Junior", "Mid-Level", "Senior"]
)

job_description = st.text_area(
    "Job Description",
    height=250
)

# Button
if st.button("Generate Questions"):

    if not job_title.strip() or not job_description.strip():
        st.warning("Please enter both job title and job description.")
    else:
        with st.spinner("Generating interview questions..."):
            result = generate_questions(job_title,level,job_description)

        st.subheader("📌 Interview Preparation")
        st.write(result)