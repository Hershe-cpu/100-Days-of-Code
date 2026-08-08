import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.Letter:row.Code for index,row in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ")
    try:
        some = [code_dict[f"{i.upper()}"] for char in word.split() for i in char]
    except KeyError:
        print("Sorry, only letters allowed")
        generate_phonetic()
    else:
        print(some)

generate_phonetic()