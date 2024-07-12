import streamlit as st
import google.generativeai as genai
from config import *
import time
import random


st.set_page_config(
    page_title="Humane AI",
    page_icon="💞"
)

#st.markdown("\twith Love💞")
st.title("Humane Chat")
st.caption("-with love💞")


st.markdown('''A Chatbot Powered by **:red[Google Gemini Pro]**''')

# Initialize Gemini-Pro 
genai.configure(api_key=keys['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

# Gemini uses 'model' for assistant; Streamlit uses 'assistant'
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

# Display Form Title
st.title("Chat with Google Gemini-Pro!")

# Display chat messages from history above current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)
    
    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt) 
    
    # Display last 
    with st.chat_message("assistant"):
        st.markdown(response.text)