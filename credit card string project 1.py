credit_card_no = input("Enter credit card number")
last_digit = credit_card_no[15:]
four = 'X'*4
disp_no = four*3 + last_digit
print(disp_no)