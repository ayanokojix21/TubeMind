# ========================
# Retriever
# ========================

from functools import lru_cache
from langchain_groq import ChatGroq
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from prompts.ragmind_prompt import condense_prompt
from utils.embedder import get_embedder
from utils.vector_store import get_faiss_index

llm = ChatGroq(model='llama3-70b-8192')

@lru_cache(maxsize=1)
def get_reranker_model():
    return HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-base")

def get_retriever(video_id=None, k=5):
    """Returns a history-aware, reranked retriever over the FAISS index."""
    
    embedder = get_embedder()
    vector_store = get_faiss_index(video_id, embedder)
    
    # Base Retriever with MMR
    base_retriever = vector_store.as_retriever(
        search_type='mmr',
        search_kwargs={'k': k, 'lambda_mult': 0.7}
    )
    
    # Reranker
    compressor = CrossEncoderReranker(
        model = get_reranker_model(),
        top_n = k
    )
    
    # Contextual Compression
    reranked_retriever = ContextualCompressionRetriever(
        base_compressor = compressor,
        base_retriever = base_retriever
    )
    
    # Add query rephrasing 
    history_aware = create_history_aware_retriever(
        llm=llm,
        retriever=reranked_retriever,
        prompt=condense_prompt
    )
    
    return history_aware