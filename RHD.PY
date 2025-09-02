import streamlit as st

# Title of the app
st.title("Hello Streamlit 👋")

# A simple text
st.write("This is my first Streamlit app!")

# Input box
name = st.text_input("Enter your name:")

# Button action
if st.button("Greet Me"):
    st.success(f"Hello, {name}! Welcome to Streamlit 🚀")
