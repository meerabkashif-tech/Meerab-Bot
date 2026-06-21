import streamlit as st
import os
from rag_engine import create_vectorstore, get_answer

st.set_page_config(
    page_title="MeerabBot - Personal Assistant",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp { 
        background: linear-gradient(135deg, #1a0533 0%, #2d1b69 50%, #11001c 100%);
        min-height: 100vh;
    }
    .main-title { 
        color: #c77dff; 
        text-align: center;
        text-shadow: 0 0 20px #7b2ff7;
        font-size: 2.5rem !important;
    }
    p { color: #e0aaff !important; text-align: center; }
    .stChatMessage { 
        background: rgba(123, 47, 247, 0.15) !important;
        border: 1px solid #7b2ff7;
        border-radius: 15px;
        margin: 5px 0;
    }
    .stChatInputContainer {
        border-top: 2px solid #7b2ff7 !important;
    }
    input { 
        background: #2d1b69 !important;
        color: #e0aaff !important;
        border: 1px solid #c77dff !important;
    }
    .stSpinner { color: #c77dff !important; }
    hr { border-color: #7b2ff7 !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🤖 MeerabBot - Your Personal Assistant</h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Ask me anything about Meerab!</p>",
            unsafe_allow_html=True)
st.divider()

CV_PATH = None
for f in os.listdir("."):
    if f.endswith(".docx"):
        CV_PATH = f
        break

if CV_PATH is None:
    st.error("❌ No .docx file found! Please add your CV to the folder.")
    st.stop()

if "vectorstore" not in st.session_state:
    with st.spinner("🔄 Loading your CV..."):
        st.session_state.vectorstore = create_vectorstore(CV_PATH)
        st.success("✅ MeerabBot is ready!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me something about Meerab..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_answer(st.session_state.vectorstore, prompt)
            st.markdown(answer)
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })