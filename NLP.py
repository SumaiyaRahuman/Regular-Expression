import re
text = "Data science and machine learning are important in AI applications"
pattern1 = r"AI"
match1 = re.findall(pattern1, text)
print("Single word detected:", match1)
pattern2 = r"\bma\w*"
match2 = re.findall(pattern2, text)
print("Words starting with 'ma':", match2)
pattern3 = r"\b\w+ing\b"
match3 = re.findall(pattern3, text)
print("Words ending with 'ing':", match3)
pattern4 = r"\b\w{4}\b"
match4 = re.findall(pattern4, text)
print("Four-letter words:", match4)
pattern5 = r"\b[A-Z][a-z]*\b"
match5 = re.findall(pattern5, text)
print("Capitalized words:", match5)