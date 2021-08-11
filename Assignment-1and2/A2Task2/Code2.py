action = int((input('Press 1 for +, 2 for -, 3 for /, 4 for * and 5 for Average:')))
if (action == 1 or action == 2 or action == 3 or action == 4):
    num1 = int(input('Enter the First number for +, -, / and *:'))
    num2 = int(input('Enter the second number for +, -, / and *:'))
    if action==1:
        Add = num1+num2
        print('The addition is :',Add)
        if Add < 0:
            print("Negative")
    if action==2:
        Sub = num1-num2
        print('The Subtraction is :',Sub)
        if Sub < 0:
            print("Negative")
    if action==3:
        Div = num1/num2
        print('The Division is :',Div)
        if Div < 0:
            print("Negative")
    if action==4:
        Mul = num1*num2
        print('The Multiplication is :',Mul)
        if (Mul < 0):
            print("Negative")
elif (action == 5):
    average1 = int(input('Enter the First number to calculate Average:'))
    average2 = int(input('Enter the second number to calculate Average:'))
    Average = (average1+average2)/2
    print('The Average of two Numbers is :',Average)
    if (Average < 0):
        print("Negative")