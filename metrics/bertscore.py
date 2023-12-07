from bert_score import score

# Example sentences
references = ["this is a test"]
candidates = ["this is a test"]

# Calculating BERTScore
P, R, F1 = score(candidates, references, lang="en")
print(f"Precision: {P.mean()}, Recall: {R.mean()}, F1 Score: {F1.mean()}")
