#Summing the digits in an integer using recursion

def sum_digits(n):
    if n<10:
        return n
    else:
        return n%10+sum_digits(n//10)

a=int(input("Enter the integer:"))
print(sum_digits(a))
