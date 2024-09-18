def find_quotient(d,n):
    if n==0:
        raise ZeroDivisionError()
    return d/n

try:
    number = int(input("enter a number:"))
    result=10/ number
except ValueError:
    print("Invalid input! please enter a valid integer")
except ZeroDivisionError:
    print("you cannot divide by zero")
else:
    print(result)

finally:#is for releasing object
    print('cleaning up')
print('End of program')
