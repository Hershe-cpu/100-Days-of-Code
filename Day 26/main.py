import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.Letter:row.Code for index,row in data.iterrows()}

word = input("Enter a word: ")

some = [code_dict[f"{i.upper()}"] for char in word.split() for i in char]

print(some)