s=[150,142,185,120,171,184,149,187,24,59,68,199,78,65,89,86]
for i in s:
    j=0
    while s[j]:
        if i >s[j]:     
            j +=1
        else:
            break
        print(f"MAX NO IS {i}")   
