import os
from dotenv import load_dotenv
from docx import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

chat_history = []
client = Groq(api_key=GROQ_API_KEY)

def load_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        if para.text.strip():
            full_text.append(para.text)
    return "\n".join(full_text)

def create_vectorstore(file_path):
    text = load_docx(file_path)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.create_documents([text])
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

def get_answer(vectorstore, question):
    global chat_history
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    history_text = ""
    for q, a in chat_history[-3:]:
        history_text += f"User: {q}\nAssistant: {a}\n"
    prompt = f"""You are MeerabBot, a personal assistant for Meerab. Use the context below to answer questions about Meerab.

Context:
{context}

Chat History:
{history_text}

Question: {question}

Answer helpfully and concisely:"""
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    answer = response.choices[0].message.content
    chat_history.append((question, answer))
    return answer