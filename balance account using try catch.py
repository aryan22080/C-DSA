class AccountBalance(Exception):
    pass
balance = 10000
def withdraw(amt):
    global balance
    if balance-amt<5000:
        raise AccountBalance("Minimum balance must be 5000")
    else:
        balance = balance - balance-amt 
        print(balance)

try:
    withdraw(6000)
except AccountBalance as a :
    print(a)
    