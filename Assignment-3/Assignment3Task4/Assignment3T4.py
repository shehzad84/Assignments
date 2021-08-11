# 1. Write a program to reverse a string. Sample input: “1234abcd” Expected output: “dcba4321”
def Re_str(string1):
    return print(string1[::-1])

if __name__ == "__main__":
    Re_str("1234abcd")

################################################################################################
# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
#Sample input: “abcSdefPghijQkl” Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

def Upper_Lower(string2):
    Lower  = 0
    Upper = 0
    for i in range(0,len(string2)):
        if string2[i].islower():
            Lower += 1
        else:
            Upper += 1

    print("Uppercase Count: {} ; Lowercase Count: {}".format(Upper,Lower))

if __name__ == "__main__":
    Upper_Lower("SoNoMaStateUniVerSity")

#####################################################################################################
# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
def single(array3):
    map = {}
    OK_array = []
    for i in range(0,len(array3)):
        if array3[i] not in map:
            map[array3[i]] = 1
            OK_array.append(array3[i])
        else:
            continue

    return print(OK_array)

if __name__ == "__main__":
    single([2,2,6,8,6,8,9,5,9,6,9,7,4,8,2,8,1,0])

######################################################################################################
# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
def sorting(string4):
    split4 = string4.split("-")
    sorted4 = sorted(split4)
    done_str = "-".join(sorted4)
    return print(done_str)

if __name__ == "__main__":
    sorting("S-o-n-o-m-a-S-t-a-t-e-U-n-i-v-e-r-s-i-t-y")

#####################################################################################################
# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect, Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
def capitalize(string5):
    capital = print(string5.upper())
    return capital

if __name__ == "__main__":
    capitalize("Sonoma State University")

#####################################################################################################
# 6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
def Sums(string6a,string6b):
    sum = int(string6a) + int(string6b)
    return print(sum)

if __name__ == "__main__":
    Sums("9","7")

#####################################################################################################
# 7. Define a function that can accept two strings as input and print the string with the maximum length in the console.
# If two strings have the same length, then the function should print both the strings line by line.
def Length_Max(string7a,string7b):
    if len(string7a) == len(string7b):
        print("len of string 1 : {} \nlen of string 2 : {}".format(len(string7a),len(string7b)))
    elif len(string7a) > len(string7b):
        print("Maximum Length : {}".format(len(string7a)))
    else:
        print("Maximum Length : {}".format(len(string7b)))

if __name__ == "__main__":
    Length_Max("KhuramShehzad","CaliforniaStateUniversity")

#####################################################################################################
# 8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).
def Square():
    array8 = []
    for i in range(1,21):
        square_int = i**2
        array8.append(square_int)

    print(tuple(array8))

if __name__ == "__main__":
    Square()

#####################################################################################################
# 9. Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.

def showNumbers(limit):
    for i in range(0,limit+1):
        if i % 2 == 0:
            print("{}  EVEN".format(i))
        else:
            print("{}  ODD".format(i))

if __name__ == "__main__":
    showNumbers(int(input("Enter the Numbers : ")))

#####################################################################################################
# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
def EvenFinder():
    List10 = []
    for i in range(1,21):
        List10.append(i)
    even_num = filter(lambda x:x%2 == 0,List10)
    print(list(even_num))
if __name__ == "__main__":
    EvenFinder()

#####################################################################################################
# 11. Write a program which uses map() and filter() to make a list
# whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].

def EvenSquare():
    List11 = []
    for i in range(1,11):
        List11.append(i)
    even_num = filter(lambda x:x%2 == 0,List11)
    even_square = map(lambda x: x**2, even_num )

    print(list(even_square))
if __name__ == "__main__":
    EvenSquare()

#####################################################################################################
# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
def exception(num12a,num12b):
    try:

        num12c = int(input("enter num1 here: ")) // int(input("enter num2 here: "))
    except:
        print("The divisor(num2) is invalid as its 0, try with different number")

#####################################################################################################
# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce
list13 = reduce(lambda x:str(x), [1,2,3,4,5,6,7])
print(list(list13))

#####################################################################################################
# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
num14 = [2,3,7,14,9]
Not_divisible = filter(lambda x:x%3 != 0,num14)
num_multiple = filter(lambda x:x%7 == 0, Not_divisible)
if Not_divisible and num_multiple :
    print(list(num_multiple))

#####################################################################################################
# 15. Write a program in Python to multiply the elements of a list by itself using a
# traditional function and pass the function to map() to complete the operation.

def multiplication(num15):
    num15a = num15
    num15a = num15a * num15
    return num15a
mul_map = map(multiplication,[1,2,3,4,5,6,7])
print(list(mul_map))

#####################################################################################################
# 16. What is the output of the following codes:
#1.  def foo():
#       try:
#           return 1
#       finally:
#           return 2
#       k = foo()
#       print(k)
"""
output : 2
"""

#2. def a():
#       try:
#           f(x, 4)
#       finally:
#           print('after f')
#           print('after f?')
#       a()

"""
output :  f(x, 4)
NameError: name 'f' is not defined

"""
#####################################################################################################
#####################################################################################################


