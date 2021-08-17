#task7
#1.
import math
C = 50
H = 30
sequence = []
ValueD = input("Enter the value of D: ")
ValueD = ValueD.split(',')
for D in ValueD:
    Q = round(math.sqrt(2 * C * int(D) / H))
    sequence.append(Q)
print(sequence)
##########################################################################################
#2.
class Shape():
    def __init__(self):
        pass

    def Area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.len = l

    def Area(self):
        return self.len*self.len

Square1= Square(5)
print (Square1.Area())
##########################################################################################
#3.
class sum2zero:
    def sumof3(self, arr):
        arr = sorted(arr)
        output=[]
        i=0
        while i < len(arr) - 2:
            j= i + 1
            k = len(arr) - 1
            while j < k:
                if arr[i] + arr[j] + arr[k] < 0:
                    j = j+1
                elif arr[i] + arr[j] + arr[k] > 0:
                    k = k-1
                else:
                    output.append([arr[i], arr[j], arr[k]])
                    j, k = j + 1, k - 1
                    while j < k and arr[j] == arr[j - 1]:
                        j = j+1
                    while j < k and arr[k] == arr[k + 1]:
                        k = k-1
            i = i+1
            while i < len(arr) - 2 and arr[i] == arr[i - 1]:
                i = i+1
        return output
print("The Input array is [-25,-10,-7,-3,2,4,8,10]\nThe array with three elements that sum to zero is:")
print(sum2zero().sumof3([-25, -10, -7, -3, 2, 4, 8, 10]))
##########################################################################################
#4.
import datetime
#method which displays sum of two different times
def displayTime(sumTime):
    print("Sum of Time : " + str(sumTime))
#method which calculates total minutes in the sum of two different times
def displayMinute(sumTime):
    (h, m, s) = str(sumTime).split(':')
    totalMinute = int(h)*60 + int(m)
    print("Total Minutes : " + str(totalMinute))
#method which calculates sum of two different times
def addTime(t1, t2):
    tList = [t1, t2]
    sumTime = datetime.timedelta()
    for t in tList:
        (h, m, s) = t.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sumTime += d
    displayTime(sumTime)
    displayMinute(sumTime)
t1 = input('Enter First Time(hh:mm:ss) : ')
t2 = input('Enter Second Time(hh:mm:ss) : ')
addTime(t1, t2)
##########################################################################################
#5.
class person:
    def __init__(self,a):
        self.age=a
        if self.age<0:
            self.age=0
            print("Age is not valid")
    def yearPasses(self,i):
        self.age+=i
        print("Current age :",self.age)
    def amiold(self):
        if self.age>0 and self.age <13:
            print("You are young")
        elif self.age>=13 and self.age<=19:
            print("You are teenager")
        else:
            print("You are old")
p=person(21)
p.yearPasses(3)
p.amiold()