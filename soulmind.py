# ========================
# SoulMind - Persona Chat
# ========================

from langchain_groq import ChatGroq
from prompts.soulmind_prompt import get_persona_prompt
from utils.memory import get_memory
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model='gemma2-9b-it', temperature=0.8)

def persona_chat(input: str, persona_name: str, session_id: str = 'user_1') -> str:
    """Answers general queries with emotional intellegence and different Persona."""
    
    try:        
        prompt = get_persona_prompt(persona_name)
        chain = prompt | llm 
        
        memory = get_memory(session_id, namespace=f"persona:{persona_name}", input_key="question")
        
        result = chain.invoke(
            {"question": input, "chat_history": memory.chat_memory.messages},
            config={"configurable": {"session_id": session_id}}
        )
        
        memory.chat_memory.add_user_message(input)
        memory.chat_memory.add_ai_message(result.content.strip())
        
        return result.content.strip()
    
    except Exception as e:
        return f"Persona Chat Error: {str(e)}"
