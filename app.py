import streamlit as st

from document_parser import extract_text_from_file
from matcher import (
    calculate_match,
    calculate_overall_match,
    calculate_skill_coverage,
    compare_skills,
)


st.set_page_config(
    page_title="AI Job Matcher",
    page_icon="🎯",
    layout="wide",
)

st.title("🎯 AI Job Matcher")
st.write(
    "Compare your résumé with a job description and discover "
    "which skills match and which are missing."
)

st.subheader("1. Add Your Résumé")

input_method = st.radio(
    "Choose how to provide your résumé:",
    ["Upload a file", "Paste text"],
    horizontal=True,
)

resume_text = ""

if input_method == "Upload a file":
    uploaded_file = st.file_uploader(
        "Upload your résumé",
        type=["pdf", "docx", "txt"],
        help="Supported formats: PDF, DOCX, and TXT",
    )

    if uploaded_file is not None:
        try:
            resume_text = extract_text_from_file(uploaded_file)

            if resume_text:
                st.success(
                    f"Successfully extracted text from {uploaded_file.name}"
                )

                with st.expander("Preview extracted résumé text"):
                    st.text_area(
                        "Extracted text",
                        value=resume_text,
                        height=250,
                        disabled=True,
                    )
            else:
                st.warning(
                    "The file was opened, but no readable text was found. "
                    "Scanned PDFs may require OCR."
                )

        except Exception as error:
            st.error(f"Could not read the uploaded file: {error}")

else:
    resume_text = st.text_area(
        "Paste your résumé",
        height=250,
        placeholder="Paste your résumé text here...",
    )

st.subheader("2. Add the Job Description")

job_description = st.text_area(
    "Paste the job description",
    height=250,
    placeholder="Paste the job description here...",
)

if st.button("Calculate Match", type="primary"):
    if not resume_text.strip() or not job_description.strip():
        st.warning(
            "Please provide both a résumé and a job description."
        )
    else:
        text_score = calculate_match(
                    resume_text,
                    job_description,
        )
        skill_score = calculate_skill_coverage(
                    resume_text,
                    job_description,
        )
        overall_score = calculate_overall_match(
                    resume_text,
                    job_description,
        )
        matched_skills, missing_skills = compare_skills(
                    resume_text,
                    job_description,
        )

        st.subheader("Match Result")

        overall_column, text_column, skill_column = st.columns(3)

        with overall_column:
            st.metric("Overall Match", f"{overall_score}%")

        with text_column:
            st.metric("Text Similarity", f"{text_score}%")

        with skill_column:
            st.metric("Skill Coverage", f"{skill_score}%")

        st.caption(
            "Overall score = 40% text similarity + 60% skill coverage."
        )
        st.progress(overall_score / 100)

        if overall_score >= 70:
            st.success(
                "Strong match! Your résumé aligns well with this job."
            )
        elif overall_score >= 40:
            st.warning(
                "Moderate match. Your résumé may need some improvements."
            )
        else:
            st.error(
                "Low match. Consider tailoring your résumé to this role."
            )

        

        st.subheader("Skill Analysis")

        matched_column, missing_column = st.columns(2)

        with matched_column:
            st.markdown("### ✅ Matched Skills")

            if matched_skills:
                for skill in matched_skills:
                    st.success(skill)
            else:
                st.info("No recognized matching skills found.")

        with missing_column:
            st.markdown("### ⚠️ Missing Skills")

            if missing_skills:
                for skill in missing_skills:
                    st.warning(skill)
            else:
                st.success("No recognized skills are missing!")