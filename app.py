import streamlit as st

st.set_page_config(page_title="My Work App", page_icon="💼")

st.title("Internal Team Dashboard")
st.write("Welcome to the new tool. Let's automate some work.")

user_input = st.text_input("Enter a client name or ID:")
if st.button("Search"):
    st.success(f"Searching database for: {user_input}...")