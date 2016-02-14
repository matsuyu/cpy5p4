#Summing series

def sum_series(i):
    if i!=1:
        return (1/i)+sum_series1(i-1)
    else:
        return 1

n=int(input("Enter i:"))
print(sum_series(n))
