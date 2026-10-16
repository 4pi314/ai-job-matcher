import streamlit as st

from matcher import calculate_match, compare_skills


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

resume_text = st.text_area(
    "Paste your résumé",
    height=250,
    placeholder="Paste your résumé text here...",
)

job_description = st.text_area(
    "Paste the job description",
    height=250,
    placeholder="Paste the job description here...",
)

if st.button("Calculate Match", type="primary"):
    if not resume_text.strip() or not job_description.strip():
        st.warning("Please enter both a résumé and a job description.")
    else:
        score = calculate_match(resume_text, job_description)
        matched_skills, missing_skills = compare_skills(
            resume_text,
            job_description,
        )

        st.subheader("Match Result")
        st.metric("Overall Match Score", f"{score}%")
        st.progress(score / 100)

        if score >= 70:
            st.success("Strong match! Your résumé aligns well with this job.")
        elif score >= 40:
            st.warning("Moderate match. Your résumé may need some improvements.")
        else:
            st.error("Low match. Consider tailoring your résumé to this role.")

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