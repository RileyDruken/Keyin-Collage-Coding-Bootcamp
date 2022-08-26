droids_cost = []

def input_droid():
    price_of_droid_1 = float(input("Price of Droid 1> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_1))
    price_of_droid_2 = float(input("Price of Droid 2> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_2))
    price_of_droid_3 = float(input("Price of Droid 3> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_3))
    price_of_droid_4 = float(input("Price of Droid 4> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_4))
    price_of_droid_5 = float(input("Price of Droid 5> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_5))
    price_of_droid_6 = float(input("Price of Droid 6> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_6))
    price_of_droid_7 = float(input("Price of Droid 7> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_7))
    price_of_droid_8 = float(input("Price of Droid 8> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_8))
    price_of_droid_9 = float(input("Price of Droid 9> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_9))
    price_of_droid_10 = float(input("Price of Droid 10> "))
    droids_cost.append("${:,.2f}".format(price_of_droid_10))
    global total_price
    total_price = price_of_droid_1 + price_of_droid_2 + price_of_droid_3 + price_of_droid_4 + price_of_droid_5 + price_of_droid_6 + price_of_droid_7 + price_of_droid_8 + price_of_droid_9 + price_of_droid_10

input_droid()