import sys
import os
sys.path.append(os.path.abspath("D:\\AI\\agent-ai-assistant\\chatbot\\prompt_design"))

from ollama import Client, ChatResponse
import requests
from prompt_design import prompt_translation as prompt_design
from translation import __model as model_name, __model_url as model_url

def translate_text(text, target_language):
    """
    Translates the given text to the target language using Ollama Llama 3.2 model.

    Args:
        text (str): The text to translate.
        target_language (str): The target language code (e.g., 'es' for Spanish, 'fr' for French).

    Returns:
        str: The translated text.
    """
    client = Client(host='http://localhost/7869')
    prompt = f"Translate the following text to {target_language}:\n\n{text}"
    response: ChatResponse = client.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': prompt.format(target_language=target_language, text=text),
        }],
        stream=False
    )
    return response.message.content
    
    prompt_template = prompt_design.get_translation_prompt(text, target_language)
    response = requests.post(
        url="http://localhost/7869/",
        json={
            "model": model_name,
            "messages": [
                {"role": "user", "content": prompt_template}
            ],
            "temperature": 0.7,
        },
    )
    print(response)

    # Check for errors in the response
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    if "choices" not in response.json() or len(response.json()["choices"]) == 0:
        raise Exception("No translation found in the response.")
    if "message" not in response.json()["choices"][0] or "content" not in response.json()["choices"][0]["message"]:
        raise Exception("Invalid response format.") 
    return response.json()["choices"][0]["message"]["content"]

# if __name__ == "__main__":
#     text = input("Enter the text to translate: ")
#     target_language = input("Enter the target language code (e.g., 'es' for Spanish): ")
#     try:
#         translated_text = translate_text(text, target_language)
#         print("Translated Text:", translated_text)
#     except Exception as e:
#         print("An error occurred during translation:", str(e))