l1 = ['A','E','F','E','A','B']
result = []
for x in l1:
    if x not in result:
        result.append(x)
    count = l1.count(x)
    result.append(count)
print(result)
