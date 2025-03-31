# pip install -qU langchain-ollama
# pip install langchain
# pip install streamlit
import os
import streamlit as st
from ollama import chat, Client
from ollama import ChatResponse, GenerateResponse
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_ollama import ChatOllama

os.environ["OLLAMA_HOST"] = "http://localhost:7869/"

#client = Client(base_url='http://localhost:7869')
client = Client()

st.title(":brain: AI Assistant with Ollama - βeta")
st.header("Extraction with llama3.2 model")
#st.write("LEARN LLM @ KGP Talkie: https://www.youtube.com/kgptalkie")

prompt_extration = """
        Extract the following information from the user input:
        - Date: The date mentioned in the input.
        - From Date: The date mentioned in the input.
        - To Date: The date mentioned in the input.
        - Product: The product or service mentioned.
        - Bet Type: The type of bet mentioned.
        - Sport: The sport mentioned.
        - Report Type: The type of report mentioned.
        - Columns: The columns or Information mentioned.
        - Report Name: The name of the report mentioned.
        - Information: Any additional information mentioned.

        User Input: "{content}"

        Provide the extracted information in the following JSON format:
        {{
            "date": "<date>",
            "from_date": "<date>",
            "to_date": "<date>",
            "products": "<product>",
            "bet_types": "<bettype>",
            "sports": "<sport>",
            "report_type": "<reporttype>",
            "report_name": "<reportname>",
            "columns": "<columns>"
            "information": "<information>"
        }}
        If the information is not available, return "N/A" for that field.
    """
default_value = "View the report win-loss detail of  sportsbook soccer sport and bet type handicap from 20 -03-2025 to 30-03-2025"

if "default_value" not in st.session_state:
    st.session_state["default_value"] = default_value

#with st.container("llm-form", clear_on_submit=True):
with st.form("llm-form", clear_on_submit=False):
    content = st.text_area("User Input", value=st.session_state["default_value"], placeholder="Type your content here...", key="widget", label_visibility="collapsed")
    submit = st.form_submit_button("Extract")

if submit and content:
    with st.spinner("Extracting response..."):
        result: GenerateResponse = client.generate(model='llama3.2', 
            prompt=prompt_extration.format(content=content),
            stream=False, 
            format="json", 
            # keep_alive=True
        )
        st.write("**:brain: Bot response: ", result.response)

        with st.expander("See most retrieved information"):
            st.write(result)

else:
    st.session_state["default_value"] = default_value

#streamlit run D:\AI\agent-ai-assistant\app\web\chat_extraction.py --server.port 8085