import streamlit as st

from matcher import calculate_match


st.set_page_config(
    page_title="AI Job Matcher",
    page_icon="🎯",
    layout="wide",
)

st.title("🎯 AI Job Matcher")
st.write(
    "Compare your résumé with a job description using "
    "TF-IDF and cosine similarity."
)

resume_column, job_column = st.columns(2)

with resume_column:
    resume_text = st.text_area(
        "Paste your résumé",
        height=300,
        placeholder="Paste your résumé text here...",
    )

with job_column:
    job_description = st.text_area(
        "Paste the job description",
        height=300,
        placeholder="Paste the job description here...",
    )

if st.button("Calculate Match", type="primary", use_container_width=True):
    if not resume_text.strip() or not job_description.strip():
        st.warning("Please provide both your résumé and the job description.")
    else:
        score = calculate_match(resume_text, job_description)

        st.subheader("Analysis Result")
        st.metric("Match Score", f"{score}%")
        st.progress(score / 100)

        if score >= 70:
            st.success("Strong match — this role closely aligns with the résumé.")
        elif score >= 40:
            st.info("Moderate match — some important qualifications overlap.")
        else:
            st.error("Low match — the résumé may need stronger relevant keywords.")