from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

checkpoint = 'facebook/nllb-200-distilled-600M'

model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

source_lang='uk'
target_lang = 'de'

translator = pipeline('translation',
                       model=model,
                       tokenizer=tokenizer,
                         src_lang=source_lang, 
                         tgt_lang=target_lang
                         )

output = translator('Привіт, мене звати Вероніка')
translated_text = output[0]['translation_text']
print(translated_text) 