x = input("Enter any number: ")
x = int(x)
if x >=0:
    for i in range(x,0,-1):
        print(i)
else:
    x = x-1
    for i in range(0,x,-1):
            print(i)