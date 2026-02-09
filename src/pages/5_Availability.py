import streamlit as st

st.title("Availability")

available = st.checkbox("Monday–Friday (9–17)", value=True)

# Ensure availability is set before proceeding
if st.button("Review"):
    st.session_state["availability"] = available
    st.switch_page("pages/6_Review_Publish.py")
