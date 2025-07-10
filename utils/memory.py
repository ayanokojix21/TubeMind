# ========================
# Memory
# ========================

from langchain.memory import ConversationTokenBufferMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

memory_cache = {}

llm = ChatGroq(model="llama-3.3-70b-versatile")

def get_memory(session_id: str, namespace: str = None, input_key: str = 'input'):
    """Create a memory for Chatbot to remember context."""
    
    key = f"{namespace}:{session_id}"
    if key not in memory_cache:
        memory_cache[key] = ConversationTokenBufferMemory(
            llm=llm,
            return_messages=True,
            memory_key="chat_history",
            input_key=input_key,
            max_token_limit=3000  
        )
    return memory_cache[key]