#1.	Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError
try:
    eval("4<!=6")
except SyntaxError:
    print('SYNTAX IS NOT CORRECT')
    
############################################################################################

# 2.Write a program in Python to allow the user to open a file by using the argv module.
# If the entered name is incorrect throw an exception and ask them to enter the name again.
# Make sure to use read only mode.
from sys import argv
Nameofprogram,filename=argv
print("Name of program ",Nameofprogram)
print("File Name:" ,filename )
while True:
    try:
        fileH=open(filename )
        content=fileH.read()
        print(content)
        fileH.close()
        break
    except:
        TryAgain=input('Wrong file Name: press Y to re-enter and N for nothing')
        if(TryAgain=="Y"):
            filename=input('Enter the correct file name')
        else:
            break

############################################################################################

# 3.Write a program to handle an error if the user entered the number more than four digits
# it should return “Please length is too short/long !!! Please provide only four digits”
def NUMcheck(num):
    try:
        if len(str(num))>4:
            raise ValueError("length is too long, Only 4 digit number is accepted")
        elif len(str(num))<=3:
            raise ValueError("length is too short, Only 4 digit number is accepted")
        print(num)
    except:
        print("Please provide only four digits.")
        raise


NUMcheck(eval(input('Enter a Number: ')))

############################################################################################

# 4.Create a login page backend to ask users to enter the username and password.
# Make sure to ask for a Re-Type Password and if the password is incorrect give chance to 
# enter it again but it should not be more than 3 times.
tries = 0
while tries<3:
    UserName = (input("enter a username: "))
    password = (input("enter a password: "))
    ReType = (input("re-enter your password: "))
    tries +=1
    if (password == ReType):
        print("login Successfull")
        break
    else:
        if(tries<3):
            print("something went wrong!! try again...")
        elif(tries==3):
            print("maximum allowed attempts exhausted!!")

############################################################################################

# 6.Read any file using Python File handling concept and return only the even length 
# string from the doc.txt file.
with open('doc.txt', 'w') as text:
    text.write("Hello I am a file\nWhere you need to return the data string\nwhich is of even length")
    text.write('\nMake sure you return the content in\nThe same link as it is present')
with open("doc.txt") as text:
    Result = ""
    for i in text:
        read = i.split()
        for j in read:
            if len(j) % 2 == 0:
                Result = Result + " " + j

print(Result)



    

