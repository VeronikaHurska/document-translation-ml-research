import evaluate
import re, pandas as pd


chrf = evaluate.load("bertscore")

def clean_text(text):
    text = re.sub(r'[.,!]', '', text)
    return text

def compute_bleu_per_row(row):
    prediction = clean_text(row['TRANSLATION'])
    reference = clean_text(row['EN'])
    results = chrf.compute(predictions=[prediction],
                         references=[reference],
                         model_type="distilbert-base-uncased"
                         )
    print(results['f1'][0])
    return results['f1'][0]

df = pd.read_csv('translations/helsinki_en_uk_translation.csv')

df['bertscore'] = df.apply(compute_bleu_per_row, axis=1)



mean = df['bertscore'].mean()
print(mean)
df.to_csv('bertscore_en_uk_helsinki.csv', index=False)
