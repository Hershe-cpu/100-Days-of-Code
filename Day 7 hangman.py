import random
try:
    from hangman_words import word_list # pyright: ignore[reportMissingImports]
except Exception:
    word_list = None

print("""

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
""")

art=["""

 +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""]

words=["roomy","two","overt","finicky","undesirable","scrawny","tan","five","five","full","rich","hill","month","team",
       "ripe","muddled","tiny","wheel","control","debt","unpack","alike","spooky","arrogant","develop","rope","try","fuck"
       ,"shit","rush","drunk","tripping","laptop","future","temperature"]

if word_list is None:
    word_list = words


act_word=random.choice(word_list)
#print(act_word)
word=[]
for i in range(0,len(act_word)):
    a="_"
    word.append(a)
#print(word)



# def letter_in_word():
#     a=act_word.index(letter)
#     word[a]=letter
#     new_word="".join(word)
#     print(new_word)
    

#print(f"Word to guess: {"".join(word)}  ")    
x = 0
new_word="".join(word)
while x<7 and new_word!=act_word:
    print(f"Word to guess {new_word}")
    letters=input("Guess a Letter: ")
    letter=letters.lower()
    #print(f"Word to guess: {new_word}")
     
    if letter in act_word:
        
        if act_word.count(letter)>1:
                for z,char in enumerate(act_word):
                    if char==letter:
                        word[z]=letter
                    new_word="".join(word)
        else:
                a=act_word.index(letter)
                word[a]=letter
                new_word="".join(word)
        print(new_word)
        if x==0:
            print()
        else:
            print(art[x-1])
        print(f"******************* {7-(x)}/7 LIVES LEFT ******************************")
        continue

    elif letter not in act_word :
        print(f"You guessed {letters}, that's not in the word. You lose a life.")
        print(art[x])
        print(f"******************* {7-(x+1)}/7 LIVES LEFT ******************************")
        x+=1
if x==7:
    print("GameOver You LOST")
    print(f"Word is {act_word}")
elif new_word==act_word:
    print("Word guessed correctly. You win.")
    print(f"Word is {new_word}")

#repeating letters 
# #some additional thik krna h
# vaisa hi bnana h jaise vid mai h
#           

    
