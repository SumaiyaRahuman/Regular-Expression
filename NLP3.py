text = "The children are playing and eating in the garden"
text = text.lower()
words = text.split()
stop_words = {"the", "are", "and", "in"}
filtered = [w for w in words if w not in stop_words]
lemmatized = []
for w in filtered:
    if w == "children":
        lemmatized.append("child")
    elif w.endswith("ing"):
        lemmatized.append(w[:-3])
    else:
        lemmatized.append(w)

print("After preprocessing:", lemmatized)
