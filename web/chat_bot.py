# pip install -qU langchain-ollama
# pip install langchain
# pip install streamlit

import streamlit as st
from ollama import Client, ChatResponse
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_ollama import ChatOllama

#client config
client = Client(host='http://localhost:7869')

st.title(":brain: AI Assistant with Ollama - βeta")
st.header("Chat with LLM llama3.2 model")
#st.write("LEARN LLM @ KGP Talkie: https://www.youtube.com/kgptalkie")


#with st.container("llm-form", clear_on_submit=True):
with st.form("llm-form", clear_on_submit=False):
    text = st.text_area("User Input", placeholder="Type your question here...", key="widget", label_visibility="collapsed")
    submit = st.form_submit_button("Ask")

if submit and text:
    with st.spinner("Generating response..."):
        response: ChatResponse = client.chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': text,
            }],
            stream=False
        )

        #model = ChatOllama(model="llama3.2", base_url="http://localhost:11434/")
        
        #chat_template = ChatPromptTemplate.from_messages(text)
        # chat_template = HumanMessagePromptTemplate.from_template(text)
        # chain = chat_template|model|StrOutputParser()
        # response = chain.invoke({})

        st.write("**:brain: Bot response: ", response.message.content)
        
        #st.write("Bot response: ", [chunk["message"]["content"] for chunk in response if chunk["done"] is False])
        # for chunk in response:
        #     if chunk["done"] is False:
        #         #print(chunk["message"]["content"])
        #         print(chunk["message"]["content"], end="", flush=True)
        #     else:
        #         break

        # st.write(st.session_state['chat_history'])

#streamlit run D:\AI\agent-ai-assistant\app\web\chat_bot.py --server.port 8083