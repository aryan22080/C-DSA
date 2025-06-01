class NegativeAge(Exception):
    pass
def stage(age):
    if age<0:
        raise NegativeAge("Age cannot be negative")
    elif age>=0 and age<13:
        print('Kid')
    elif age>=13 and age<20:
        print('Teen')
    elif age>=20 and age<50:
        print('Young')

try:
    age = int(input("Enter your age"))
    stage(age)
except NegativeAge as n:
    print(n)
    