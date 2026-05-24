# 1- import string module
# 2- store all characters in lists (upper/lower case, digists, punctuations)
# 3- take number of characters from user
# 4- make sure the number of characters is 6 or more
# 5- shuffle all lists
# 6- calculate 30% and 20% of number of characters
# 7- create password 60% letters and 40% digits and punctuations
import random
import string
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

character_number=input("enter the number of characters : ")
while True : 

    try: 
        character_number=int(character_number)
        if character_number<6 : 
            print("you need at least 6 charaters ")
            character_number=input("enter the number agian : ")
        else: 
            break 
    except : 
        print("invalid input , please entre a number  ")
        character_number=input("enter the number of characters : ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1=round(0.3*character_number)
part2=round(0.2*character_number)

password=[]
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])
random.shuffle(password)


if len(password)!=character_number:
    n=character_number-len(password) 
    for i in range(n):
        password.append(s4[i])


password=''.join(password)
print(password , len(password))