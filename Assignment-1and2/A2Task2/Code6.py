string = input("Input a string:   ")
digit=0
alpha=0
for c in string:
    if c.isdigit():
        digit=digit+1
    elif c.isalpha():
        alpha=alpha+1
    else:
        pass
print("Letters", alpha)
print("Digits", digit)