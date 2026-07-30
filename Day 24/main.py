with open ("my_file.txt","r") as f:#/mail-merge-project-start/Input/Names/invited_names.txt
    data  = f.readlines()


with open("/mail-merge-project-start/Input/Letters/starting_letter.txt","r") as w:
    letter_contents = w.read()
    for name in data:
        n = name.strip()
        new_letter = letter_contents.replace("[name]",n)
        with open("/mail-merge-project-start/Input/Letters/starting_letter.txt", "w") as x:
            x.write(new_letter)

