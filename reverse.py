# x = input("Enter any number: ")
# x = int(x)
# if x >=0:
#     for i in range(x,0,-1):
#         print(i)
# else:
#     x = x-1
#     for i in range(0,x,-1):
#             print(i)

# print("")
n = int(input("Enter the value of n: "))
print ("numbers from {0} to {1} are: ".format(n,1))
for i in range(n,0,-1):
    print(i)