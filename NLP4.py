import nltk
from nltk.stem import PorterStemmer
text = "The children are playing and eating in the garden"
words = text.lower().split()
stop_words = {"the", "are", "and", "in"}
filtered = [w for w in words if w not in stop_words]
ps = PorterStemmer()
stemmed = [ps.stem(w) for w in filtered]
print("After stemming:", stemmed)
