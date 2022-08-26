list = []
while True:
    try:
        number = int(input("Number to sort type 0 if you are done entering numbers> "))
        if number != 0:
            list.append(number)
        else:
            break

    except:
        print("Error input is not a number")

print("Numbers unsorted ",list)
list.sort()
print("Numbers Sorted ",list)
