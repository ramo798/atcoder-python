s = "6 \n382253568 723152896 37802240 379425024 404894720 471526144"
a =[]

for tmp in s.split():
    a.append(int(tmp))

# [8,12,40]
total = 0

judge = True

while judge:
    for i in range(a[0]):
        if a[i+1] % 2 == 0:
            a[i+1] = int(a[i+1] / 2)
            
        else:
            judge = False
            total -= 1
        
    total += 1

print(total)