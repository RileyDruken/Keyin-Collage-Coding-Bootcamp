def input_droid():
    global droids_cost
    droids_cost = []
    global total_price
    total_price = 0
    global num
    num = 1

    print("type a letter when done entering Droid Prices")
    while True:
        try:
            price_of_droid = float(input(f"Price of Droid {num}> "))
            if type(price_of_droid) != str:
                num += 1
                droids_cost.append("${:,.2f}\n".format(price_of_droid))
                total_price += price_of_droid
        except ValueError:
            print("Exiting")
            break
input_droid()