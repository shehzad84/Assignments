# 1. list of 10 elements of four different data types like int, string, complex and float.
mango = ["a","7","CAdd", 6, 2, 1992, 6.43, 23.3, 3+3j, 2+20j]
print(mango)

#####################################################################################################
# 2. list of size 5 and slicing structure
list = [1,2,3,4,5]
print(list[2::])
print(list[1:3])
print(list[::4])

#####################################################################################################
# 3. The sum and multiply of all the items in a given list.
def addMulti(arr):
    add = 0
    multi = 1
    for i in range(len(arr)):
        add += arr[i]
        multi *= arr[i]
    return print("sum : {} and multiplication : {} ".format(add,multi))

if __name__ == "__main__":
    addMulti([3,6,9,5,8,2])

#####################################################################################################
# 4. Finding largest and smallest number from a given list.
def Max_Min(arr):
    minimum = min(arr)
    maximum = max(arr)
    print("Minimum value is: {} and Maximum value is: {} ".format(minimum,maximum))

if __name__ == "__main__":
    Max_Min([5,6,9,7,10,-4,11,42])


#####################################################################################################
# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
arr = eval(input("Enter a list of Integers: "))
ok_list = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        ok_list.append(arr[i])

print(ok_list)


#####################################################################################################
# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).
list6 = []
for i in range(1,31):
    if i < 6 or i > 25:
        list6.append(i**2)
print(list6)


#####################################################################################################
# 7. Write a program to replace the last element in a list with another list. from Sample input: [1,3,5,7,9,10], [2,4,6,8] to Expected output: [1,3,5,7,9,2,4,6,8]

def list7(arr1,arr2):
    new_arr7 = []
    new_arr7.append(arr1[0:len(arr1)-1] + arr2)
    print(new_arr7)

if __name__ == "__main__":
    list7([1,3,5,7,9,10], [2,4,6,8])

#####################################################################################################
# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}, Expected output: {1:10,2:20,3:30,4:40}
d1 = eval(input("Enter the Value of Dictionary1: "))
d2 = eval(input("Enter the value of Dictionary2: "))
dict8 = dict(d1)
dict8.update(d2)
print("New Dictionary is : {}".format(dict8))

#####################################################################################################
# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
# Sample input: n=5  Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
n = int(input("Enter Value of n = "))
dict9 = {}
for i in range(1,n+1):
    dict9[i] = i*i
print(dict9)


#####################################################################################################
# 10. Write a program which accepts a sequence of comma-separated numbers from console 
# and generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98, Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

input10 = eval(input("Enter Commas separated Numbers : "))
list10 = list(input10)
tuple10 = tuple(input10)

print("list : {} and tuple: {}".format(list10,tuple10))