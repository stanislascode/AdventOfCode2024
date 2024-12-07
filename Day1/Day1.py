input = open("input","r")
lines = input.readlines()
first_number=[]
last_number = []
for line in lines:
    line = line[:-1].split(" ")
    print(line)
    first_number.append(int(line[0]))
    last_number.append(int(line[-1]))

first_number.sort()
last_number.sort()
s = 0
for i in range(len(first_number)):
    s+=abs(first_number[i]-last_number[i])

print(s)