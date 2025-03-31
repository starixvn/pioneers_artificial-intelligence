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

#app UI
st.title(":brain: AI Assistant with Ollama - βeta")
st.header("Translation with llama3.2 model")
#st.write("LEARN LLM @ KGP Talkie: https://www.youtube.com/kgptalkie")

#with st.container("llm-form", clear_on_submit=True):
with st.form("llm-form", clear_on_submit=False):
    text = st.text_area("User Input", placeholder="Type your content here...", key="widget", label_visibility="collapsed")
    target = st.selectbox("Select Language", ["English", "Thai", "Vinamese", "Chinese", "Japanese", "Korean"], index=0, label_visibility="collapsed")
    submit = st.form_submit_button("Translate")

if submit and text and target:
    with st.spinner("Generating response..."):
        prompt = f"Translate the following text to {target}:\n\n{text}"
        response: ChatResponse = client.chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': prompt.format(text=text),
            }],
            stream=False
        )

        st.write("**:brain: Bot translate: ", response.message.content)

#streamlit run d:/AI/agent-ai-assistant/app/web/chat_translation.py --server.port 8084