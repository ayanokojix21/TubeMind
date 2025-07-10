# ========================
# TechMind - Tech Chat
# ========================

from langchain_groq import ChatGroq
from prompts.techmind_prompt import tech_prompt
from utils.memory import get_memory
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model='llama-3.3-70b-versatile', temperature=0.2)

def code_chat(input: str, session_id: str = 'user_1') -> str:
    """Answers programming questions, writes code, or debugs code snippets."""
    try:
        prompt = tech_prompt
        chain = prompt | llm 

        memory = get_memory(session_id, namespace="code", input_key="tech_request")
        result = chain.invoke(
            {"tech_request": input, "chat_history": memory.chat_memory.messages},
            config={"configurable": {"session_id": session_id}}
        )
        memory.chat_memory.add_user_message(input)
        memory.chat_memory.add_ai_message(result.content.strip())
        
        return result.content.strip()
    
    except Exception as e:
        return f"Code Tool Error: {str(e)}"