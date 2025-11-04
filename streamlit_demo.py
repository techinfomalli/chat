from langchain_openai import ChatOpenAI
import streamlit as st

st.title('Aask anything you want to know')

with st.sidebar:
    st.title('provide your API key')
    OPENAI_API_KEY = st.text_input('OPEN AI api Key',type="password")

if not OPENAI_API_KEY:
    st.info('Enter Open api key to continue')
    st.stop()


llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)


question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)

    st.write(response.content)




