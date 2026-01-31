import streamlit as st
import openai

st.title("Service details")

# Inputs
description = st.text_area("Description")
city = st.text_input("City")

# Configure OpenAI safely
def get_openai_client():
    key = (
        st.secrets.get("OPENAI_API_KEY")
        or st.secrets.get("general", {}).get("OPENAI_API_KEY")
    )
    if not key:
        return None
    openai.api_key = key
    return openai


def generate_description(category):
    client = get_openai_client()
    if not client:
        return "AI description unavailable. Please configure API key."

    try:
        response = client.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional service marketing assistant."
                },
                {
                    "role": "user",
                    "content": f"Write a concise, professional service description for a {category} service provider."
                }
            ],
            max_tokens=80,
            temperature=0.7,
        )

        return response.choices[0].message["content"].strip()

    except Exception as e:
        st.error("AI service temporarily unavailable.")
        return ""


# AI Button
if st.button("Generate Description with AI ✨"):
    if "category" in st.session_state:
        ai_description = generate_description(st.session_state["category"])
        if ai_description:
            st.session_state["description"] = ai_description
            description = ai_description
    else:
        st.warning("Please select a service category first.")


# Submit button
if st.button("Next"):
    if not description or not city:
        st.error("Both description and city are required.")
    else:
        st.session_state["description"] = description
        st.session_state["city"] = city
        st.switch_page("pages/4_Pricing.py")
