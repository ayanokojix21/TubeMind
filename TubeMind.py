# ========================
# Streamlit - Main Chat UI
# ========================

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
if "HUGGINGFACEHUB_API_TOKEN" in st.secrets:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

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

default_groq = os.environ.get("GROQ_API_KEY", "")
default_hf = os.environ.get("HUGGINGFACEHUB_API_TOKEN", "")

user_groq_api = st.text_input("Groq API Key", type="password", value=default_groq)
user_hf_api = st.text_input("HuggingFace API Key", type="password", value=default_hf)

if user_groq_api:
    os.environ["GROQ_API_KEY"] = user_groq_api
if user_hf_api:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = user_hf_api

required_keys = {
    "Groq API Key": os.environ.get("GROQ_API_KEY"),
    "HuggingFace API Key": os.environ.get("HUGGINGFACEHUB_API_TOKEN"),
}
missing_keys = [name for name, val in required_keys.items() if not val]

if missing_keys:
    st.warning(f"⚠️ Please set the following API keys to proceed: {', '.join(missing_keys)}")
else:
    st.success("✅ All required API keys are set! You're good to go.")

st.markdown("---")
st.info("ℹ️ Tip: In local runs, use a `.env` file. On Streamlit Cloud, use `Secrets`. You can also enter keys manually above.")