list = [[1,2,3],[4,5,6],[7,8,9]]
sum = 0
list2  = []

print(f"Length of list {len(list)}")

for i in list:
    for x in i:
        print(x)
        sum += x
        list2.append(x)
print(f"Sum = {sum}")

print(f"there are {len(list2)} numbers in the list")