# ========================
# Streamlit - RAG Chat UI
# ========================

import streamlit as st
from ragmind import rag_chat
from utils.transcript_loader import extract_video_id, load_transcript
from utils.text_splitter import split_transcript
from utils.embedder import get_embedder
from utils.vector_store import get_faiss_index, vector_store_cache
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="RAGMind - RAG Chatbot", page_icon="🎥", layout="wide")

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
    st.title("🧠 RAGMind")
    st.markdown("**This chatbot answers questions based on YouTube transcripts.**")
    st.markdown("- Paste a YouTube video link with captions\n- Ask questions about the content\n- RAGMind will remember your chat history 💬")
    st.info("💡 Works best with educational or lecture-style videos.")
    
st.title("🎬 RAGMind — RAG Powered YouTube Chat")
st.caption("Talk to YouTube videos with memory-enabled Q&A.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "video_url" not in st.session_state:
    st.session_state.video_url = ""
if "video_id" not in st.session_state:
    st.session_state.video_id = None
if "indexed" not in st.session_state:
    st.session_state.indexed = False
session_id = "user_1"

st.subheader("📺 Enter YouTube Video URL")
youtube_url = st.text_input("Paste a YouTube link with captions", value=st.session_state.video_url)

if youtube_url and (youtube_url != st.session_state.video_url or not st.session_state.indexed):
    with st.spinner("Indexing transcript... please wait"):
        progress = st.progress(0)
        try:
            video_id = extract_video_id(youtube_url)
            st.session_state.video_url = youtube_url
            st.session_state.video_id = video_id
            st.session_state.chat_history = []
            progress.progress(10)

            transcript = load_transcript(youtube_url)
            if not transcript:
                st.error("No transcript available for this video.")
                st.stop()
            progress.progress(40)

            chunks = split_transcript(transcript)
            progress.progress(70)

            embedder = get_embedder()
            vector_store = get_faiss_index(video_id, embedder)
            vector_store_cache[video_id] = vector_store

            st.session_state.indexed = True
            progress.progress(100)
            st.success("Transcript indexed! You can now ask questions.")
        except Exception as e:
            st.session_state.indexed = False
            st.error(f"Indexing failed: {str(e)}")
            st.stop()

if st.session_state.indexed:
    user_input = st.chat_input("Ask something about the video...")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        with st.spinner("🧠 Thinking..."):
            response = rag_chat(user_input, st.session_state.video_url, session_id=session_id)
            st.session_state.chat_history.append({
                "role": "assistant",
                "text": response["answer"],
                "sources": response["sources"]
            })
            
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])
        if msg["role"] == "assistant" and msg.get("sources"):
            with st.expander("📚 Show Source Context"):
                for i, src in enumerate(msg["sources"], 1):
                    st.markdown(f"**Chunk {i}:**")
                    st.write(src)

if not st.session_state.video_url:
    st.info("📌 Please paste a YouTube video link above to begin.")
elif not st.session_state.indexed:
    st.warning("⏳ Indexing not complete. Please wait...")