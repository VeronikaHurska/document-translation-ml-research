import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu


def clean_text(text):
    text = re.sub(r'[.,!]', '', text)
    return text

def compute_bleu_per_row(row):
    hypothesis = word_tokenize(clean_text(row['TRANSLATION']).lower())
    reference = word_tokenize(clean_text(row['EN']).lower())

    result = sentence_bleu([reference], hypothesis)
    print(result)
    return result

df = pd.read_csv('translations/nvidia/nvidia_de_en_result.csv')

df['BLEU_Score'] = df.apply(compute_bleu_per_row, axis=1)


df['avg'] = df['BLEU_Score'].mean()

df.to_csv('bleu_de_en_nvidia.csv', index=False)
