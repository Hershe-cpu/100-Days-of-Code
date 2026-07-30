print( """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
yn="yes"
while yn=="yes":
    task=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if task.lower() not in ["encode","decode"]:
        print("Enter Valid Task")
        continue
    else:
        msg=input("Type your message:\n")
        shift=int(input("Type the shift number:\n"))
        encoded_word="" 
        decoded_word="" 
        if task.lower()=="encode":
            for letter in msg:
                ascii_value=ord(letter)
                new_ascii=ascii_value+shift
                new_letter=chr(new_ascii)
                encoded_word=encoded_word+new_letter
            print(f"Your encoded message is {encoded_word}")

        elif task.lower()=="decode":
            for letter in msg:
                ascii_value=ord(letter)
                new_ascii=ascii_value-shift
                new_letter=chr(new_ascii)
                decoded_word=decoded_word+new_letter
            print(f"Your decoded message is {decoded_word}")
        #print(f"Here's the encoded result: {}")
        yn=input("Type 'yes' to move on or 'no' to finish it"
                 )
