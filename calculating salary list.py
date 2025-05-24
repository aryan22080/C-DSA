work_hours = [int(x)for x in input("Enter no of working hours in a day seperated by space").split()]
wages = int(input("Enter the daily working wages"))
total = sum(work_hours)
salary = total*wages
print(salary)
