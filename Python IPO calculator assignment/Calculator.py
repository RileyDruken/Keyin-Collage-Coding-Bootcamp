import math
#input

first_number = int(input("First_Number>"))
second_number = int(input("Second_Number>"))

#Processing

add = first_number + second_number
sub = first_number - second_number
multiply = first_number * second_number
divide = first_number / second_number
negated1 = first_number * -1
negated2 = second_number * -1
power = first_number ** second_number
log = math.log(first_number, second_number)
sin = math.sin(first_number)
cos = math.cos(second_number)
tan = math.tan(first_number)/second_number
#output

print("Addition = " + str(add))
print("Subtraction = " + str(sub))
print("multiplication = " + str(multiply))
print("division = " + str(divide))
print("Negated number 1 = " + str(negated1))
print("Negated number 2 = " + str(negated2))
print("the power of number 1 to the power of number 2 = " + str(power))
print(" The log of the first number to the base of the second number = " + str(log))
print("The Sin of the first number = " + str(sin) + " The Cos of the second number = " + str(cos))
print("tan of the first number divided by the second number = " + str(tan))