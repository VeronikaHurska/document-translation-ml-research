from datasets import load_metric
import pandas as pd
import numpy as np
import evaluate
from bleurt import score 


checkpoint = "bleurt/bleurt/test_checkpoint"

# bleurt = evaluate.load("bleurt")
# bleurt = load_metric('bleurt')


scorer = score.BleurtScorer(checkpoint)

def compute_bleurt(hypotheses, references):
    # results = bleurt.compute(predictions=hypotheses, references=references)
    results = scorer.score(references=references, candidates=hypotheses)

    print(results)
    return results

df = pd.read_csv('translations/helsinki_nlp/helsinki_en_de_result.csv')

bleurt_scores = compute_bleurt(df['TRANSLATION'], df['DE'])

df['BLEURT_Score'] = bleurt_scores

total_score = sum(bleurt_scores)
mean_score = np.mean(bleurt_scores)

summary_df = pd.DataFrame({'UK': ['Total Score', 'Mean Score'], 
                           'TRANSLATION': ['', ''], 
                           'BLEURT_Score': [total_score, mean_score]})

final_df = pd.concat([df, summary_df], ignore_index=True)

final_df.to_csv('bleurt_en_de_helsinki.csv', index=False)

