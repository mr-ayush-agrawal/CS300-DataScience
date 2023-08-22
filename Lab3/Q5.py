tup = (1,2,3,4,5)
num = int(input("Enter the interger to end in the end of the tuple  "))
tup = list(tup)
tup.append(num)
tup= tuple(tup)

print(tup)
num = []
num.append(int(input("Enter the 1st interger to insert in the tuple  ")))
num.append(int(input("Enter the 2nd interger to insert in the tuple  ")))
num.append(int(input("Enter the 3rd interger to insert in the tuple  ")))
print(type(num))
tup = list(tup)
for i in range(3):
    tup.insert(2+i,num[i])
tup= tuple(tup)

print(tup)