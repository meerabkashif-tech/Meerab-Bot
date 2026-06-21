# MeerabBot - Personal RAG Chatbot

## Student Information
- **Student Name:** Meerab Kashif
- **Project Title:** MeerabBot - Personal RAG Chatbot
- **Chatbot Name:** MeerabBot
- **Course:** Natural Language Processing (CC438)

## Project Description
MeerabBot is a RAG-based personal assistant chatbot built using my CV/Resume as the dataset. It answers questions about my background, skills, and experience using Retrieval-Augmented Generation (RAG) pipeline.

## Deployment Link
https://meerab-bot-d9tdjqzdqc2dwykcyprnqq.streamlit.app/

## Tech Stack
- Streamlit (UI)
- Groq API - LLaMA 3.1 (LLM)
- FAISS (Vector Database)
- HuggingFace Embeddings
- LangChain (RAG Pipeline)

## How to Run Locally
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file and add: `GROQ_API_KEY=your_key`
4. Run: `streamlit run app.py`
