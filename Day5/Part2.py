input = open("test","r")
#input = open("input","r")
lines = input.readlines()


text = [["."]+[line[i] for i in range(len(line)-1)]+["."] for line in lines]
text = [["."]*(len(text)+2)]+text+[["."]*(len(text)+2)]

cpt = 0
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] != 'A':
            continue
        else:
            if ((text[i-1][j-1] == 'M' and text[i+1][j+1] == 'S') or (text[i-1][j-1] == 'S' and text[i+1][j+1] == 'M')) and ((text[i+1][j-1] == 'M' and text[i-1][j+1] == 'S') or (text[i+1][j-1] == 'S' and text[i-1][j+1] == 'M')):
                cpt+=1
                                                                     
print(cpt)





