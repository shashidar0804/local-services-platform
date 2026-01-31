import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import the Supabase client
from src.db import supabase

st.title("Review & Publish")

st.write("### Summary")
st.write(st.session_state)

if st.button("Go Live 🚀"):
    # Collect data from session state
    data = {
        "email": st.session_state.get("email"),
        "category": st.session_state.get("category"),
        "description": st.session_state.get("description"),
        "city": st.session_state.get("city"),
        "price": st.session_state.get("price"),
        "availability": st.session_state.get("availability"),
    }

    # Write data to Supabase
    try:
        response = supabase.table("services").insert(data).execute()
        if response.status_code == 201:
            st.success("Service published successfully!")
        else:
            st.error(f"Failed to publish service: {response.json()}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
