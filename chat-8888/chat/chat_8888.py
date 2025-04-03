# pip install -qU langchain-ollama
# pip install langchain
# pip install streamlit

import streamlit as st
from ollama import Client, ChatResponse
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv(".env")

#os.environ["OLLAMA_HOST"] = "http://10.21.10.36:7869"
#os.environ["OLLAMA_MODEL"] = "deepseek-r1" # 'llama3.2' # 'llama2-7b-chat' # 'llama2-13b-chat' # 'llama2-70b-chat' # 'llama3.2'

#ollama_host="http://10.21.10.36:7869"
#ollama_model="deepseek-r1" # 'llama3.2' # 'llama2-7b-chat' # 'llama2-13b-chat' # 'llama2-70b-chat' # 'llama3.2'

ollama_host = os.environ.get("OLLAMA_HOST")
ollama_model = os.environ.get("OLLAMA_MODEL")

#client config
client = Client(host=ollama_host)

st.title(":brain: Alpha - AI Assistant - βeta")
st.header("Chat with LLM {model_name} model".format(model_name=ollama_model))

st.info("model host: {host}".format(host=ollama_host))
with st.form("llm-form", clear_on_submit=False):
    text = st.text_area("User Input", placeholder="Type your question here...", key="widget", label_visibility="collapsed")
    submit = st.form_submit_button("Ask")

if submit and text:
    with st.spinner("Generating response..."):
        response: ChatResponse = client.chat(model=ollama_model, messages=[
            {
                'role': 'user',
                'content': text,
            }],
            stream=False
        )

        st.write("**:brain: Bot response: ", response.message.content, unsafe_allow_html=True)

# To run the Streamlit app, execute the following command in the terminal:
# streamlit run D:\AI\ai-fine-tune\chat\chat_8888.py --server.port 8888
#export OLLAMA_HOST=http://10.21.10.36:7869
#export OLLAMA_MODEL=deepseek-r1
