import streamlit as st

st.title("Set your price")

price = st.number_input("Price per hour (€)", min_value=0)

# Add validation for price input
if price <= 0:
    st.error("Please enter a valid price greater than 0.")
else:
    if st.button("Next"):
        st.session_state["price"] = price
        st.switch_page("pages/5_Availability.py")
