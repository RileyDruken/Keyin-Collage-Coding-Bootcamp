import datetime
import random


# Random Bool
def random_bool():
    print(bool(random.getrandbits(1)))


random_bool()


#Print Date
def print_current_time():
    print(datetime.datetime.now())

print_current_time()

try:
    with open("message.txt") as f:
        text = f.read()
        print(text)
except FileNotFoundError:
    with open("message.txt", "w") as f:
        print("File does not exist... Generating new message.txt file")
        text = f.write("Hello World")





