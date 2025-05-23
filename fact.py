n = int(input("Enter a number"))
fact = 1 
if n<=1:
    print("Factorial not possible for negative numbers")
else:
    for i in range(1,n+1):
        fact = fact*i 
        print(fact)