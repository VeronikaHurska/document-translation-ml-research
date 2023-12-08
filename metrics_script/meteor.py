import evaluate
import re, pandas as pd


chrf = evaluate.load("meteor")

def clean_text(text):
    text = re.sub(r'[.,!]', '', text)
    return text

def compute_bleu_per_row(row):
    prediction = clean_text(row['TRANSLATION'])
    reference = clean_text(row['EN'])
    results = chrf.compute(predictions=[prediction],
                         references=[reference],
                         )
    print(results)
    return results['meteor']

df = pd.read_csv('translations/helsinki_en_uk_translation.csv')

df['meteor_score'] = df.apply(compute_bleu_per_row, axis=1)



mean = df['meteor_score'].mean()
print(mean)
df.to_csv('meteor_en_uk_helsinki.csv', index=False)
