# ========================
# RAGMind Prompt
# ========================

from langchain_core.prompts import ChatPromptTemplate

CONDENSE_QUESTION_SYSTEM_TEMPLATE = (
    "You are a helpful assistant that reformulates follow-up questions into "
    "standalone questions.\n"
    "Given a conversation history and a new user question, rewrite it so that it "
    "can be fully understood on its own.\n"
    "Do not answer the question. Only return the standalone version.\n"
)

condense_prompt = ChatPromptTemplate.from_messages([
    ("system", CONDENSE_QUESTION_SYSTEM_TEMPLATE),
    ("placeholder", "{chat_history}"),
    ("human", "Follow-up: {input}\nStandalone question:")
])

QA_SYSTEM_PROMPT = (
    "You are a knowledgeable and clear AI tutor helping users understand educational YouTube videos.\n"
    "Use the retrieved transcript context to craft a comprehensive, informative answer to the user's question.\n"
    "Your response should be 2–3 paragraphs long, well-structured, and assume the user has basic understanding of the topic.\n"
    "If the context is insufficient, say: 'I don’t know based on the transcript.'\n\n"
    "Context:\n{context}"
)

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", QA_SYSTEM_PROMPT),
    ("placeholder", "{chat_history}"),
    ("human", "Question: {input}")
])