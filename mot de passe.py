M=str(input("enter the password:  "))
i=0
while M!="Dev@2023" and i<3:
    M=str(input("password is  incorrect, please try again: "))
    i=i+1
if M=="Dev@2023":
    print("Bonjour")
else:
    print("if you forgot the password,  please answer this question")
    A=str(input("what's your favorite movie:  "))
    if A=="inception":
        print("password is: Dev@2023")
    else:
        print("the answer  is incorrect")