import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

sia = SentimentIntensityAnalyzer()
score = sia.polarity_scores("The ice cream was the best ever.")
print(score)