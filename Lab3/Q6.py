tup = (1,2,3,4,5,6,7,8,9,0)
numm = int(input("ENter the number to find in tuple "))
for x in range(len(tup)):
    if numm==tup[x]:
        print("The index is ", x)
        break
else:
    print("Element not in Tuple")