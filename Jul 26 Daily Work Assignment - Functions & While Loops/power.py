def print_powers(start,end,power):
    for num in range(start, end):
        if num < end:
           print(num ** power)
    return sum

start = int(input("Start range num? "))
end = int(input("End Range num? "))
power = int(input("Power? "))
print_powers(start,end,power)