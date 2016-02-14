#Occurrences of a specified character in a string

def count_letter(str,ch):
    if len(str)==0:
        return 0
    else:
        if str[0]==ch:
            return count_letter(str[1:],ch)+1
        else:
            return count_letter(str[1:],ch)

string=input("Enter the string:")
char=input("Enter the character:")
print(count_letter(string,char))
