from deep_translator import GoogleTranslator

def translate_text(text: str):
    return GoogleTranslator(
        source="en",
        target="sn"
    ).translate(text)