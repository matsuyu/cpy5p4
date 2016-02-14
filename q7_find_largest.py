#Finding the largest number in an array

n=0
def find_largest(alist):
    global n
    if len(alist)!=0:
        if alist[0]>n:
            n=alist[0]
        find_largest(alist[1:])
    return n
arr=[5,1,8,7,2]
print(find_largest(arr))

        
