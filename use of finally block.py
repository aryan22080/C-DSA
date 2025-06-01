def div(a,b):
    if b!=0:
        c = a//b 
        print(c)
    else:
        raise ZeroDivisionError

try:
    res = div(6,0)
except:
    print("Divison by zero")
finally:
    print("The program has ended successfully")