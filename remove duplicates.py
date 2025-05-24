l1 = [3,4,3,6,7,9,7]
l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)