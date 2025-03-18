import streamlit as st
import time
from config import APP_TITLE, APP_DESCRIPTION, UI_THEME_COLOR
from llm_service import LLMService
from data_handler import CandidateInfo
import utils

# Initialize session state variables if they don't exist
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
    
if 'llm_service' not in st.session_state:
    st.session_state.llm_service = LLMService()
    
if 'candidate_info' not in st.session_state:
    st.session_state.candidate_info = CandidateInfo()
    
if 'conversation_started' not in st.session_state:
    st.session_state.conversation_started = False

if "last_message_time" not in st.session_state:
    st.session_state.last_message_time = 0

# Configure page
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="👨‍💻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Import external CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# App title and description
st.title(APP_TITLE)
st.markdown(APP_DESCRIPTION)

# Function to display chat messages
def display_message(role, content):
    """Display a chat message with appropriate styling"""
    if role == "user":
        st.markdown(f'<div class="chat-message user"><div class="message">{content}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message bot"><div class="message">{content}</div></div>', unsafe_allow_html=True)

# Display chat history
for message in st.session_state.conversation_history:
    display_message(message["role"], message["content"])

# Start conversation if not already started
if not st.session_state.conversation_started:
    # Get greeting from LLM
    greeting = st.session_state.llm_service.start_conversation()
    
    # Add to conversation history
    st.session_state.conversation_history.append({
        "role": "assistant",
        "content": greeting
    })
    
    st.session_state.conversation_started = True
    
    # Force a rerun to display the greeting
    st.rerun() 

# User input area
with st.form(key="user_input_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", key="user_input")
    submit_button = st.form_submit_button("Send")
    
    if submit_button and user_input:
        cooldown = 5  # Rate limit: 5 seconds between messages
        if time.time() - st.session_state.last_message_time < cooldown:
            st.warning(f"Please wait {cooldown} seconds before sending another message.")
        else:
            st.session_state.last_message_time = time.time()

            # Add user message to conversation history
            st.session_state.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Get response from LLM
            with st.spinner("TalentScout Assistant is thinking..."):
                response = st.session_state.llm_service.get_response(user_input)
            
            # Handle NoneType response
            if not response or response == "Error: No response from API.":
                response = "⚠️ API rate limit exceeded. Try again later."

            # Add assistant message to conversation history
            st.session_state.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            # Update candidate info from conversation
            extracted_info = st.session_state.candidate_info.extract_info_from_conversation(
                st.session_state.conversation_history
            )
            
            for field, value in extracted_info.items():
                st.session_state.candidate_info.update_field(field, value)
            
            # Rerun to update the display
            st.rerun() 

# Add a reset button in the sidebar
with st.sidebar:
    st.title("Controls")
    if st.button("Reset Conversation"):
        st.session_state.conversation_history = []
        st.session_state.llm_service.reset_conversation()
        st.session_state.candidate_info = CandidateInfo()
        st.session_state.conversation_started = False
        st.rerun()
