input = open("test","r")
#input = open("input","r")
lines = input.readlines()


text = [["."]+[line[i] for i in range(len(line)-1)]+["."] for line in lines]
text = [["."]*(len(text)+2)]+text+[["."]*(len(text)+2)]

cpt = 0
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] != 'X':
            continue
        else:
            if text[i+1][j] == 'M' and text[i+2][j] =='A' and text[i+3][j] == 'S':
                cpt+=1
            if text[i][j+1] == 'M' and text[i][j+2] =='A' and text[i][j+3] == 'S':
                cpt+=1    
            if text[i+1][j+1] == 'M' and text[i+2][j+2] =='A' and text[i+3][j+3] == 'S':
                cpt+=1
            if text[i-1][j] == 'M' and text[i-2][j] =='A' and text[i-3][j] == 'S':
                cpt+=1
            if text[i][j-1] == 'M' and text[i][j-2] =='A' and text[i][j-3] == 'S':
                cpt+=1    
            if text[i-1][j-1] == 'M' and text[i-2][j-2] =='A' and text[i-3][j-3] == 'S':
                cpt+=1
            if text[i-1][j+1] == 'M' and text[i-2][j+2] =='A' and text[i-3][j+3] == 'S':
                cpt+=1
            if text[i+1][j-1] == 'M' and text[i+2][j-2] =='A' and text[i+3][j-3] == 'S':
                cpt+=1
print(cpt)





