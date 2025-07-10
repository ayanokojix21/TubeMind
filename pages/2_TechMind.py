# ========================
# Streamlit - Code Chat UI
# ========================

import streamlit as st
import uuid
from techmind import code_chat  
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="TechMind - Code Companion", page_icon="💻")

st.markdown("""
    <style>
    /* Reduce default font size */
    html, body, [class*="css"]  {
        font-size: 14px !important;
    }

    /* Tweak chat message font */
    .stChatMessage {
        font-size: 14px !important;
    }

    /* Tweak chat input */
    .stTextInput > div > div > input {
        font-size: 14px !important;
    }

    /* Optional: Compact sidebar */
    .css-1d391kg {  /* Sidebar title spacing */
        padding-top: 0.5rem !important;
    }

    /* Optional: Reduce line spacing for markdown */
    .stMarkdown p {
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("💡 Code Help")
    st.markdown("- Write code in any language\n- Debug errors\n- Ask technical programming questions")
    
st.title("💻 TechMind – Code Chat")
st.markdown("Ask programming questions, write scripts, or debug code instantly.")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "code_messages" not in st.session_state:
    st.session_state.code_messages = [{"role": "assistant", "content": "👋 Hi! I'm your code assistant. Ask me to write or debug any code!"}]

for msg in st.session_state.code_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("🛠️ Ask about code or debugging...")

if user_input:
    st.session_state.code_messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = code_chat(user_input, session_id=st.session_state.session_id)
        st.markdown(response)
        st.session_state.code_messages.append({"role": "assistant", "content": response})
