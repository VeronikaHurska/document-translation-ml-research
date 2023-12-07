from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-uk-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-uk-en")

text_to_translate = """
"""

inputs = tokenizer.encode(text_to_translate, return_tensors="pt", padding=True)

outputs = model.generate(inputs)

translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(translated_text)
