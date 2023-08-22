lst =  [1,2,3,4,5]

def pro(l):
    r = 1
    for x in l:
        r*=x
    return r

print("Sum of all elements ", sum(lst))
print("Product of all elements", pro(lst))
print("Print the smallest element in the list", min(lst))
print("Print the largest element in the list" , max(lst))