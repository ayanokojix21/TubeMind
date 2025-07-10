# ========================
# Indexing - Text Splitters
# ========================

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_transcript(text: str, chunk_size: int=512, chunk_overlap: int=64):
    """Splits transcript into small chunks."""
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    chunks = splitter.create_documents([text]) 
    return chunks