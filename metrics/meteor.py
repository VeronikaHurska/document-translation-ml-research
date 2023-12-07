import nltk
from nltk.translate.meteor_score import meteor_score

nltk.download('wordnet')


reference = "this is a test"
candidate = "this is a test"

score = meteor_score([reference], candidate)
print(f"METEOR score: {score}")
