import evaluate
import re, pandas as pd


chrf = evaluate.load("chrf")

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
    return results['score']

df = pd.read_csv('translations/nvidia/nvidia_de_en_result.csv')
df = df.head(1000)
df['chrf_score'] = df.apply(compute_bleu_per_row, axis=1)



mean = df['chrf_score'].mean()
print(mean)
df.to_csv('chrf_de_en_nvidia.csv', index=False)
