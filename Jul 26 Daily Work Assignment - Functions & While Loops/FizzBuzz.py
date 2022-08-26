def fizzbuzz(x):
    for num in range(1, x):
        if num < x:
            if num%3 == 0 and num%5 != 0:
                print("Fizz")
            elif num%5 == 0 and num%3 !=0:
                print("Buzz")
            elif num%3 == 0 and num%5 == 0:
                print("FizzBuzz")
            else: print(num)
    return
fizzbuzz(25)


