from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenerativeAI with API key
genai.configure(api_key="AIzaSyCfli709TP50_XWu6sSWFNLFiDOC8OX70g")

# Function to load the Gemini model and Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

def get_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Input textbox for user's question
input_question = st.text_input("Input:")

# Button to submit the question
submit_button = st.button("Ask the question")

# Check if the submit button is clicked
if submit_button:
    if input_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        response_text = get_response(input_question)
        st.write(response_text)
