import math
input = open("input","r")
lines = input.readlines()

def test(test_value,true_values):
    for i in range(2**(len(true_values)-1)):
        values = list(true_values)
        for j in range(len(values)-1):
            values[j+1] = (values[j] + values[j+1])*((i >> j) & 1)+(values[j] * values[j+1])*(1-((i >> j) & 1))
        if values[len(values)-1] == test_value:
            return test_value
    return 0


s = 0
for line in lines:
    test_value=int(line.split(":")[0])
    values = [int(line.split(":")[1][1:-1].split(" ")[i]) for i in range(len(line.split(":")[1][1:-1].split(" ")))]
    print(values[0:2])
    s+=test(test_value,values)

print(s)

print(160*(10**(math.ceil(math.log10(99+1))))+99)