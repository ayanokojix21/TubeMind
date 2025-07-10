# ========================
# Indexing - Embeddings
# ========================

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

_embedder = None

def get_embedder(model_name: str = 'BAAI/bge-base-en-v1.5'):
    """Function for making Embeddings from chunks."""
    
    global _embedder
    
    if _embedder is None:
        _embedder = HuggingFaceEmbeddings(
            model_name=model_name,
            encode_kwargs={'normalize_embeddings': True}
        )
        
    return _embedder