import streamlit as st
from langchain_openai import ChatOpenAI

# App Title
st.set_page_config(page_title="Ask Anything", page_icon="💬")
st.title("💬 Ask Anything You Want to Know")

# Sidebar for API Key Input
with st.sidebar:
    st.header("🔐 OpenAI API Key")
    OPENAI_API_KEY = st.text_input("Enter your OpenAI API key", type="password")
    st.caption("Don't have one? Ask Mallikarjun for access.")

# Validate API Key
if not OPENAI_API_KEY:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()

# Initialize Chat Model
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

# Question Input
question = st.text_input("📝 What's your question?", placeholder="Type your question here...")

# Response Handling
if question:
    try:
        response = llm.invoke(question)
        st.subheader("📣 Response")
        st.write(response.content)
    except Exception as e:
        st.error(f"❌ Error communicating with OpenAI: {e}")
