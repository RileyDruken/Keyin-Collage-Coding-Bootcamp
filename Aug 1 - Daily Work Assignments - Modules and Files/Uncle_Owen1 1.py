#Uncle Owen
import datetime
import droid_func1

index = 0

average_price = droid_func1.total_price/10

with open("message1.txt", "a") as f:
    f.write(f"#####{datetime.datetime.now()}####\n")
    for x in droid_func1.droids_cost:
        index += 1
        f.write(f"Cost of Droid {index}: {x}\n")
    f.write("total_price_of_Droid: " + "${:,.2f}\n".format(droid_func1.total_price))
    f.write("average_price_of_Droid: " + "${:,.2f}\n".format(average_price))
    f.write("###########################################\n")