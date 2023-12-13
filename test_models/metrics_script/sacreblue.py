from datasets import load_metric
from nltk.tokenize import word_tokenize
import re
import pandas as pd

metric = load_metric("sacrebleu")
def clean_text(text):
    text = re.sub(r'[.,!]', '', text)
    return text


    
def compute_sacrebleu_per_row(row):
    hypothesis = word_tokenize(clean_text(row['TRANSLATION']).lower())
    reference = word_tokenize(clean_text(row['EN']).lower())
    print("--------",[hypothesis])
    print("========",[reference])

    result = metric.compute(predictions=[hypothesis],references=[reference])
    print(result)
    return result['score']

df = pd.read_csv('translations/helsinki_nlp/helsinki_uk_en_translation.csv')

df['sacreBLEU_Score'] = df.apply(compute_sacrebleu_per_row, axis=1)


df['avg'] = df['sacreBLEU_Score'].mean()

df.to_csv('sacreblue_uk_en_helsinki.csv', index=False)
