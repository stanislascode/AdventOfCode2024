import math
import itertools
input = open("input","r")
lines = input.readlines()

def test(test_value,true_values):
    
    n_uplets = itertools.product(range(3), repeat=(len(true_values)-1))
    for n_uplet in n_uplets:
        values = list(true_values)
        for j in range(len(values)-1):
            if n_uplet[j] == 0:
                values[j+1] = (values[j] + values[j+1])
            elif n_uplet[j] == 1:
                values[j+1] = (values[j] * values[j+1])
            elif n_uplet[j] == 2:
                values[j+1]=values[j]*(10**(math.ceil(math.log10(values[j+1]+1))))+values[j+1]
        if values[len(values)-1] == test_value:
            return test_value

    return 0


s = 0
for line in lines:
    test_value=int(line.split(":")[0])
    values = [int(line.split(":")[1][1:-1].split(" ")[i]) for i in range(len(line.split(":")[1][1:-1].split(" ")))]
    s+=test(test_value,values)
print(s)