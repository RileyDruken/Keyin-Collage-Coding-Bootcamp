price: int = 10
cost: int = 0
discount = 0

orderamount: int = int(input('How many pizzas do you want? '))
orderlocation: str = input('Which country is the order placed from? ')

if orderlocation == "Canada" or orderlocation == "canada":
    price = 3.75



if orderamount > 0:
    if orderamount < 10:
        if orderlocation == "USA":
            cost = orderamount * 7.50
            cost -= orderamount - orderamount%10
        else:
            cost = orderamount * price
            cost -= orderamount - orderamount % 10
    elif orderamount >= 10 and orderamount <= 50:
        if orderlocation == "Canada" or orderlocation == "canada":
            cost = orderamount * price

        else:
            cost = orderamount * price
            cost -= orderamount - orderamount%10
    elif orderamount > 50:
        if orderamount >= 500:
            cost = orderamount * 3.75
        else:
            discount = orderamount
            discount -= 50
            cost = discount * 5 + 500
            cost -= orderamount - orderamount%10

    print('The total cost is $' + str(round(cost, 2)) + ' for ' + str(orderamount) + ' pizzas! ')
else:
    print("Error: You can't have a negative number of pizzas in an order! Please restart the program and try again!")



