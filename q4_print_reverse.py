#Reverse the digits in an integer recursively

def reverse_int(n):
    if n < 10:
        print(n,end='')
    else:
        print(n%10,end='')
        reverse_int(n//10)

a = int(input("Enter the integer:"))
reverse_int(a)
