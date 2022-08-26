

def sum_up_to(x):
    sum = 0
    for num in range(0,x):
        if num < x:
            sum+=num + 1

    return sum

x = int(input())
returnnum = sum_up_to(x)
print(returnnum)
