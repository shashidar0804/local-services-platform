import streamlit as st
import bcrypt
from db import supabase

# Set page configuration
st.set_page_config(page_title="Local Services - Signup/Login", layout="centered")

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
    }
    .stTextInput > div > input {
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 5px;
    }
    .stRadio > label {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a title and description
st.title("Welcome to Local Services Platform")
st.write("### Signup or Login to get started")

# Add a toggle for login vs signup
mode = st.radio("Select Mode", ["Login", "Signup"])

if mode == "Login":
    st.subheader("Login to Your Account")
    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Login"):
        # Fetch user data from Supabase
        response = supabase.table("users").select("email, password").eq("email", email).execute()
        if response.data:
            stored_password = response.data[0]["password"]
            if bcrypt.checkpw(password.encode(), stored_password.encode()):
                st.session_state["email"] = email
                st.success("Logged in successfully!")
                st.switch_page("pages/2_Choose_Service.py")
            else:
                st.error("Invalid password.")
        else:
            st.error("Email not found.")
else:
    st.subheader("Create a New Account")
    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Create a password")

    if not email or not password:
        st.error("Both email and password are required.")
    else:
        if st.button("Continue"):
            # Check if email already exists
            response = supabase.table("users").select("email").eq("email", email).execute()
            if response.data:
                st.error("Email already exists. Please log in.")
            else:
                # Hash the password
                hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                # Insert user into Supabase
                supabase.table("users").insert({"email": email, "password": hashed_password}).execute()
                st.session_state["email"] = email
                st.success("Account created! Please choose a service.")
                st.switch_page("pages/2_Choose_Service.py")