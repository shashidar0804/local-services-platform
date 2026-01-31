import streamlit as st

def get_state():
    if "provider" not in st.session_state:
        st.session_state["provider"] = {}
    return st.session_state["provider"]
