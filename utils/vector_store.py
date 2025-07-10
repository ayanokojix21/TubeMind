# ========================
# Indexing - Vector Store
# ========================

from langchain_community.vectorstores import FAISS
from utils.transcript_loader import load_transcript
from utils.text_splitter import split_transcript

vector_store_cache = {}

def get_faiss_index(video_id, embedder):
    """Loads transcript and builds in-memory FAISS index.""" 
    
    if video_id in vector_store_cache:
        return vector_store_cache[video_id]
    
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    transcript = load_transcript(video_url)
    
    chunks = split_transcript(transcript)
    vector_store = FAISS.from_documents(documents=chunks, embedding=embedder)
    vector_store_cache[video_id] = vector_store
    
    return vector_store