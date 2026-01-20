import re

def tokenize_text(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

if __name__ == "__main__":
    text = "Natural Language Processing is fun. Python makes NLP easy!"
    tokens = tokenize_text(text)

    print("Tokens:")
    print(tokens)