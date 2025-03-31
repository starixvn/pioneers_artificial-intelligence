def get_translation_prompt(text: str, target_language: str) -> str:
    """
    Generates a prompt to translate the given text into the target language.

    Args:
        text (str): The text to be translated.
        target_language (str): The language to translate the text into.

    Returns:
        str: A formatted prompt for translation.
    """
    return f"Translate the following text to {target_language}:\n\n{text}"