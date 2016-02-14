#Computing greatest common divisor using recursion

def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)

a=int(input("Enter n锛�"))
b=int(input("Enter m锛�"))
print(gcd(a,b))
