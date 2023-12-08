from datasets import load_metric
import pandas as pd
import numpy as np

bleurt = load_metric('bleurt')

def compute_bleurt(hypotheses, references):
    results = bleurt.compute(predictions=hypotheses, references=references)
    return results['scores']

df = pd.read_csv('translation_results/helsinki_en_uk_result.csv')

bleurt_scores = compute_bleurt(df['TRANSLATION'], df['EN'])

df['BLEURT_Score'] = bleurt_scores

total_score = sum(bleurt_scores)
mean_score = np.mean(bleurt_scores,dtype=np.float32)

summary_df = pd.DataFrame({'EN': ['Total Score', 'Mean Score'], 
                           'TRANSLATION': ['', ''], 
                           'BLEURT_Score': [total_score, mean_score]})

final_df = pd.concat([df, summary_df], ignore_index=True)

final_df.to_csv('bleurt_en_uk_helsinki.csv', index=False)

