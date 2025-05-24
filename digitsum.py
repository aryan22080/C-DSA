n = int(input("Enter a digit"))
original = n 
digit_sum = 0
while(n>0):
          last_digit = n%10
          digit_sum+=last_digit
          n = n//10
print(digit_sum)
