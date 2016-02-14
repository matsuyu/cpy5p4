#Finding the number of uppercase letters in a string

def find_num_uppercase(str):
    if len(str)==0:
        return 0
    else:
        if 65<=ord(str[0])<=90:
            return 1+find_num_uppercase(str[1:])
        else:
            return 0+find_num_uppercase(str[1:])

s=input("Enter the string:")
print(find_num_uppercase(s))
    
