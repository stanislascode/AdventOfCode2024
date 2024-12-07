#input = open("test","r")
input = open("input","r")
lines = input.readlines()
s=0
for line in lines:

    line = [int(i) for i in line[:-1].split(" ")]
    for i in range(len(line)):
        Increase = False
        Close = True
        new_line = line[:i] + line[i+1:]
        if sorted(new_line) == new_line or sorted(new_line, reverse=True) == new_line:
            Increase = True
        for i in range(len(new_line)-1):
            if abs(new_line[i]-new_line[i+1]) > 3 or abs(new_line[i]-new_line[i+1])==0:
                Close = False
                break
        if Close and Increase:
            s+=1
            break
print(s)