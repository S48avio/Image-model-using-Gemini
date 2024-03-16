from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenerativeAI with API key
genai.configure(api_key="AIzaSyCfli709TP50_XWu6sSWFNLFiDOC8OX70g")

# Function to load the Gemini model and Gemini Pro model
model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input, image):
    response = model.generate_content([input, image])
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini LLM Application")

# Input textbox for user's question
input_question = st.text_input("Input:",key="input")
upload_file = st.file_uploader("choose an image...",type=["jpg",'jpeg','png'])
image=''
from PIL import Image
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="uploaded image",use_column_width=True)
# Button to submit the question
submit_button = st.button("Image")

# Check if the submit button is clicked
if submit_button:
    if input_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        response_text = get_response(input_question,image)
        st.write(response_text)
