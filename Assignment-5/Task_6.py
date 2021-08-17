#task6
###################################################################################
#1. 
strIn = (input("Enter a string: "))
Out = [i for i in strIn if i.isupper()]
print(Out)
###################################################################################
#2.
names = ['Khuram', 'Shehzad', 'Dave']
courses = ['Engineering', 'Medical', 'Psychology']
test2 = {key:values for key,values in zip(names,courses)}
print(test2)
###################################################################################
#4.
def rev_string(str):
    length = len(str)
    for i in range(length - 1, -1, -1):
        yield str[i]
input = "PythonDeveloper"
for char in rev_string(input):
    print(char)
###################################################################################
#5.
def deco_example(func):
    def additional():
        print("This is the additional.")
        func()
    return additional

@deco_example
def okfunction():
    print("This is the function.")

okfunction()