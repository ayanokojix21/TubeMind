# ========================
# Streamlit - Main Chat UI
# ========================

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN") or st.secrets.get("HUGGINGFACEHUB_API_TOKEN", "")

st.set_page_config(page_title="TubeMind", page_icon="🎥", layout="wide")

st.title("🎬 Welcome to TubeMind")
st.caption("Your intelligent assistant for YouTube learning, code and meaningful chat.")

st.markdown("""
**TubeMind** supports three smart assistants:
- 🎥 **RAGMind** – YouTube transcript-based memory Q&A  
- 💻 **TechMind** – Code writing, debugging, and technical Q&A  
- 🧠 **SoulMind** – Emotionally-aware, thoughtful conversations with different Persona

👉 Use the **left sidebar** to navigate between modes.
""")

st.divider()
st.subheader("🔐 API Key Configuration")

user_groq_api = st.text_input("Groq API Key", type="password", value=GROQ_API_KEY)
user_hf_api = st.text_input("HuggingFace API Key", type="password", value=HUGGINGFACEHUB_API_TOKEN)

if user_groq_api: os.environ["GROQ_API_KEY"] = user_groq_api
if user_hf_api: os.environ["HUGGINGFACEHUB_API_TOKEN"] = user_hf_api

required = {
    "Groq API Key": "GROQ_API_KEY",
    "HuggingFace API Key": "HUGGINGFACEHUB_API_TOKEN",
}
missing = [name for name, key in required.items() if not os.environ.get(key)]

if missing:
    st.warning(f"⚠️ Please set the following API keys: {', '.join(missing)}")
else:
    st.success("✅ All required API keys are set! You're good to go.")

st.markdown("---")
st.info("ℹ️ Tip: In local runs, use `.env`. On Streamlit Cloud, use `Secrets`. You can also enter keys above manually.")
