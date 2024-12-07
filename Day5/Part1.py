
input = open("input","r")
lines = input.readlines()

order = []
#1176
for line in lines[:1176]:
    order.append((int(line[:-1].split('|')[0]),int(line[:-1].split('|')[1])))


def check_order(tab,order):
    count = False
    changed = True
    while(changed):
        changed = False
        for i in range(len(tab)):
            for j in range(i,len(tab)):
                if (tab[j],tab[i]) in order:
                    changed = True
                    count = True
                    tab[j], tab[i] = tab[i], tab[j]
                    j = 0
                    i = 0
    if count:
        print(tab)
        return tab[len(tab)//2]
    else:
        return 0
s = 0
for line in lines[1176::]:
    tab = [int(line[:-1].split(',')[i]) for i in range(len(line[:-1].split(',')))]
    s+=check_order(tab,order)

print(s)