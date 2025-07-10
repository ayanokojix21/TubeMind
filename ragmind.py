# ========================
# RAGMind - RAG Chat
# ========================

from langchain_groq import ChatGroq
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from utils.memory import get_memory
from prompts.ragmind_prompt import qa_prompt
from utils.retriever import get_retriever
from utils.transcript_loader import extract_video_id
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model='llama3-70b-8192')

def build_rag_chain(video_id=None, k=5):
    
    retriever = get_retriever(
        video_id=video_id,
        k=k
    )

    qa_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=qa_prompt
    )

    full_chain = create_retrieval_chain(
        retriever=retriever,
        combine_docs_chain=qa_chain
    )

    return full_chain

def rag_chat(query: str, video_url: str, session_id: str = "user_1"):
    """Answers the RAG Query from the Transcripts stored in vector store."""
    
    video_id = extract_video_id(video_url) if video_url else None
    rag_chain = build_rag_chain(video_id)

    memory = get_memory(session_id, namespace="rag", input_key="input")
    chat_history = memory.chat_memory.messages if memory else []

    result = rag_chain.invoke(
        {"input": query, "chat_history": chat_history},
        config={"configurable": {"session_id": session_id}}
    )

    memory.chat_memory.add_user_message(query)
    memory.chat_memory.add_ai_message(result['answer'])

    return {
        "answer": result["answer"],
        "sources": [doc.page_content for doc in result.get("context", [])]
    }