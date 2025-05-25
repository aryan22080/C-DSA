x = [[1,1,1],[0,0,0],[1,2,3]]
y = [[1,0,1],[5,6,7],[2,4,5]]
result =[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = y[i][j] - x[i][j]
for r in result:
    print(r)
