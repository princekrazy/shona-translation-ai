from model import tokenizer, model
import torch

def translate_text(text: str):
    tokenizer.src_lang = "eng_Latn"

    inputs = tokenizer(text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids("sna_Latn"),
        max_length=128
    )

    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]