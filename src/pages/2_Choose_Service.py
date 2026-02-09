import streamlit as st

st.title("Choose your service")

service = st.selectbox(
    "Service category",
    ["Cleaning", "Handyman", "Tech Help", "Tutoring", "Moving"]
)

# Add validation for service selection
if not service:
    st.error("Please select a service category.")
else:
    if st.button("Next"):
        st.session_state["category"] = service
        st.switch_page("pages/3_Service_Details.py")
