string=input("Enter string :")
numbers=0
letters=0
for i in range(len(string)):
    if((string[i] >='a' and string[i] <='z') or (string[i]>= 'A' and string[i] <='Z')):
        letters=letters+1
    elif(string[i]>= '0' and string[i]<= '9'):
        numbers=numbers+1
print("Number of letters in the string are :",letters)
print("No of disits in the string are :",numbers)