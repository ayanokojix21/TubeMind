# TubeMind 

TubeMind is a multimodal, memory-enabled AI platform that combines Retrieval-Augmented Generation (RAG), emotional intelligence, and technical reasoning. It features three distinct AI modules:

- **RAGMind** – Talk to YouTube videos with transcript-based memory-powered Q&A.
- **TechMind** – A technical programming assistant for writing, debugging, and explaining code.
- **SoulMind** – A persona-based emotional companion with 10 unique personalities like Jethalal, Iron Man, Therapist Bot, and more.

---

## Features

### RAGMind – YouTube RAG Chatbot
- Accepts **YouTube video links** and indexes transcripts.
- Uses **FAISS vector store** for efficient retrieval.
- Memory-enabled conversations with **multi-turn context**.
- Shows **source chunks** for traceability.

### TechMind – Code Assistant
- Supports all programming languages.
- Answers technical questions or writes/debugs code.
- Uses **structured markdown formatting** for clean responses.
- Supports follow-up questions using **token-based memory**.

### SoulMind – Persona Chatbot
- 10 personas: AI Companion, Jethalal, Iron Man, Doraemon, Deadpool, Swami Vivekanand, Therapist Bot, Naruto, Ayanokoji, GPT 2050.
- Each persona has custom **tone, behavior, and goal**.
- Great for **emotional check-ins**, casual talks, and creative fun.

---

## Local Installation

Follow these steps to run **TubeMind** locally on your machine.

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/TubeMind.git
cd TubeMind
```

### 2. Create & Activate Virtual Environment

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
```
```bash
# Windows:
venv\Scripts\activate
```
```bash
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create a .env file in the root directory, or copy the example file:

```bash
cp .env.example .env
```

Edit the .env file and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_key
```

### 5. Launch the App
```bash
streamlit run TubeMind.py
```
This will launch the Streamlit interface with access to:

The application will open in your default web browser at ```http://localhost:8501/.```

---

## Project Structure

```
TubeMind/
│
├── pages/ # Streamlit UI Pages
│ ├── 1_RAGMind.py # YouTube RAG Chat UI
│ ├── 2_TechMind.py # Tech assistant UI
│ └── 3_SoulMind.py # Persona chat UI
│
├── prompts/ # Prompt templates for each module
│ ├── ragmind_prompt.py # RAG Prompt 
│ ├── techmind_prompt.py # Tech Prompt
│ └── soulmind_prompt.py # Persona Prompt
│
├── utils/ # Utilities used across modules
│ ├── embedder.py # Embedding logic
│ ├── memory.py # Memory system using token buffers
│ ├── retriever.py # FAISS retriever + reranker
│ ├── text_splitter.py # Transcript chunking logic
│ ├── transcript_loader.py # Load YouTube transcripts
│ └── vector_store.py # FAISS indexing and caching
│
├── ragmind.py # Backend logic for RAGMind
├── techmind.py # Backend logic for TechMind
├── soulmind.py # Backend logic for SoulMind
│
├── TubeMind.py # TubeMind Main UI Page
├── requirements.txt # Python dependencies
├── .env # Your API keys (not checked into Git)
├── .env.example # Example template for .env file
├── .gitignore # Ignored files for version control
└── README.md # Project documentation
```

---

### Tech Stack

- Python 3.10+
- Streamlit – UI
- LangChain (LCEL) – Memory, agent, prompts
- Groq LLMs – Llama3, Gemma
- HuggingFace Transformers – Embeddings + CrossEncoder reranker
- FAISS – Vector search
- YouTube Transcript API – Video parsing

---

### License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

**Note:** This project was developed for **educational purposes** and is not **production ready**










