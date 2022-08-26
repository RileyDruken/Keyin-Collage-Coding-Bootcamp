"""
Debugging
"""


def calculate_pay(name, wage, hours):
    TAX = 0.15
    total_before_tax = wage * hours
    tax_to_deduct = total_before_tax * TAX
    total_pay = total_before_tax - tax_to_deduct
    message = f"The total pay for {name} is ${total_pay:,.2f}"
    print(message)


def calc(x, y):
    result = x + y
    print(f"The result of x + y is: {result}")


calculate_pay("Mark", 17, 22.5)


in1 = int(input("Enter a number"))
in2 = int(input("Enter another number"))
calc(in1, in2)
