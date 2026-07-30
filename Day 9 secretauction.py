from art import logo
import os

print(logo)
print("Welcome to the secret auction program")
yn="yes"
d={}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while yn.lower()=="yes":
     name=input("What is your name?: ")
     bid=input("What is your Bid?: ")
     d[name]=bid
    
    
     yn=input("Are there any other bidders? Type 'yes' or 'no'. ")
     clear()
# d={"abc":"35","def":"97","jkl":"54","mno":"67",}
# print(d)
l=[]
for i in d.values():
    l.append(int(i))
# print(l)
x=max(l)
# print(x)
for keys in (d):
    if d[keys]==str(x):
        print(f"The winner is {keys} with an amount of {x}")
        break


    