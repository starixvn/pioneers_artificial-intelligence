from typing import Dict

def extract_info_prompt(user_input: str) -> Dict[str, str]:
    """
    Extracts information such as date, product, bet type, and sport from user input.

    Args:
        user_input (str): The input string from the user.

    Returns:
        Dict[str, str]: A dictionary containing the extracted information.
    """
    prompt_template = """
    Extract the following information from the user input:
    - Date: The date mentioned in the input.
    - Product: The product or service mentioned.
    - Bet Type: The type of bet mentioned.
    - Sport: The sport mentioned.

    User Input: "{user_input}"

    Provide the extracted information in the following JSON format:
    {{
        "date": "<date>",
        "product": "<product>",
        "bettype": "<bettype>",
        "sport": "<sport>"
    }}
    """
    return prompt_template.format(user_input=user_input)