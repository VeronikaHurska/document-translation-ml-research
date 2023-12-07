from nltk.translate.bleu_score import sentence_bleu

reference = ['this', 'is', 'a', 'test']
candidate = ['this', 'is', 'a']


score = sentence_bleu(reference, candidate)
print(f"BLEU score: {score}")
