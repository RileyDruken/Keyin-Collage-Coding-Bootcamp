#Uncle Owen
import datetime

import droid_func2
index = 0
avr = droid_func2.num - 1
average_price = droid_func2.total_price/avr

with open("message2.txt", "a") as f:
    f.write(f"#####{datetime.datetime.now()}####\n")
    for x in droid_func2.droids_cost:
        index += 1
        f.write(f"Cost of Droid {index}: {x}\n")
    f.write("total_price_of_Droid: " + "${:,.2f}\n".format(droid_func2.total_price))
    f.write("average_price_of_Droid: " + "${:,.2f}\n".format(average_price))
    f.write("###########################################\n")