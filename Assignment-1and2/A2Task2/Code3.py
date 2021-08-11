a, b, c = 10, 20, 30
avg = (a+b+c)/3
print("average = ", avg)
if (avg > a and avg > b and avg > c):
    print("average is Higher than a,b,c")
if (avg > a and avg > b):
    print("average is Higher than a and b")
if (avg > a and avg > c):
    print("average is Higher than a and c")
if (avg > b and avg > c):
    print("average is Higher than b and c")
if (avg > a):
    print("average is Higher than a")
if (avg > b):
    print("average is Higher than b")
if (avg > c):
    print("average is Higher than c")