def fac(a):
    res = 1
    i = 1
    if a == 0 or a == 1:
        return 1
    else:
        return a * fac(a-1)

a = int(input("enter the value : "))
res = fac(a)
print("The Factorial is : ", res)