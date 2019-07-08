s = "2\n2\n2\n100"
a = []
for tmp in s.split():
    a.append(int(tmp))

cou = 0
for yen50 in range(a[2]+1):
    for yen100 in range(a[1]+1):

        for yen500 in range(a[0]+1):
            if (yen50*50 + yen100*100 + yen500*500) / a[3] == 1:
                cou += 1


print(cou)