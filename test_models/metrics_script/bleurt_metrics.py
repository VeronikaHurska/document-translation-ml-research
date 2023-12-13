from datasets import load_metric
import pandas as pd
import numpy as np
from bleurt import score 

checkpoint = "bleurt/bleurt/test_checkpoint"
scorer = score.BleurtScorer(checkpoint)

def compute_bleurt(hypotheses, references):
    results = scorer.score(references=references, candidates=hypotheses)
    print(results)
    return results

df = pd.read_csv('translations/facebook/facebook_uk_en.csv')
df = df.head(1000)

bleurt_scores = compute_bleurt(df['TRANSLATION'], df['EN'])
df['BLEURT_Score'] = bleurt_scores

# Normalize BLEURT scores to a 0-1 scale
min_score = min(bleurt_scores)
max_score = max(bleurt_scores)
df['Normalized_BLEURT_Score'] = (df['BLEURT_Score'] - min_score) / (max_score - min_score)

# Convert normalized scores to percentage
df['Percentage_BLEURT_Score'] = df['Normalized_BLEURT_Score'] * 100

total_score = sum(df['BLEURT_Score'])
mean_score = np.mean(df['BLEURT_Score'])

summary_df = pd.DataFrame({'UK': ['Total Score', 'Mean Score', 'Normalized Mean Score', 'Percentage Mean Score'], 
                           'TRANSLATION': ['', '', '', ''], 
                           'BLEURT_Score': [total_score, mean_score, 
                                            np.mean(df['Normalized_BLEURT_Score']), 
                                            np.mean(df['Percentage_BLEURT_Score'])]})
print("----",np.mean(df['Percentage_BLEURT_Score']))
final_df = pd.concat([df, summary_df], ignore_index=True)
final_df.to_csv('bleurt_uk_en_facebook.csv', index=False)
