# ============================
# Streamlit - Persona Chat UI
# ============================

import streamlit as st
from soulmind import persona_chat  
from utils.memory import get_memory

st.set_page_config(page_title="SoulMind - Persona Chat", page_icon="🧠")

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

session_id = "user_1"

with st.sidebar:
    st.title("🧠 SoulMind")
    st.markdown("This is your emotionally intelligent assistant.")
    st.markdown("Ask casual, thoughtful, or reflective questions.")
    
persona_options = [
"AI Companion", "Jethalal", "Iron Man", "Doraemon", "Deadpool",
"Swami Vivekanand", "Therapist Bot", "Naruto", "Ayanokoji", "GPT 2050"
]

selected_persona = st.sidebar.selectbox("🎭 Choose a Persona", persona_options)

st.title(f"🧠 SoulMind — Chat with {selected_persona}")
st.caption("Talk to an emotionally aware companion that adapts to your mood.")

memory = get_memory(session_id=session_id, namespace=f"persona:{selected_persona}", input_key="question")

for msg in memory.chat_memory.messages:
    if msg.type == "human":
        st.chat_message("user").write(msg.content)
    elif msg.type == "ai":
        st.chat_message("assistant").write(msg.content)

if prompt := st.chat_input("💬 How are you feeling today? Or ask anything..."):
    st.chat_message("user").write(prompt)
    
    with st.spinner("💖 TubeMind is listening..."):
        response = persona_chat(prompt, persona_name=selected_persona, session_id=session_id)
        st.chat_message("assistant").write(response)
