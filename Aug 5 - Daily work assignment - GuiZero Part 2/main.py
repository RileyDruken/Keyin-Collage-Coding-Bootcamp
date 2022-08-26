import random

from guizero import App, Text, PushButton, TextBox, Box,Combo



def button_text():
    message.value = f"Welcome {input_box.value}"
    message.text_color = ("Blue")
    app.title = (input_box.value)
    if input_box.value == "":
        app.warn("Error No Name!!", "Please Enter your name")


def button_color():
    box.bg = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



botscore = 0
playerscore = 0
def Button_flip():
    global playerscore
    global botscore
    coin = random.choice(["Heads", "Tails"])
    print(coin)
    if combo.value == coin:
        playerscore += 1
        message3.value = f"score: Player:{playerscore}, Bot:{botscore}"
    else:
        botscore += 1
        message3.value = f"score: Player:{playerscore}, Bot:{botscore}"
app = App(title="My First Application")
box = Box(app, width="fill",height=200,border=1)

box2 = Box(app, width="fill",height=200,border=1)
box2.bg = (255,255,255)
box3 = Box(app, width="fill",height=200,border=1)
box3.bg = (0,255,255)
message3 = Text(box3, text="score: Player:0, Bot:0", size=12,align="left")
message = Text(box3, text="Select heads or tails then flip the coin", size=12)
combo = Combo(box3, options=["Heads", "Tails"])



message = Text(box, text="Welcome to my program", size=30)
message2 = Text(box, text="Please enter your name!", size=12,align="left")
input_box = TextBox(box,align="left")
button = PushButton(box, text="Click me to change things", command=button_text,align="left")
button2 = PushButton(box2, text="Click me to change the color of the background", command=button_color)
button3 = PushButton(box3, text="Click me to flip coin", command=Button_flip)

app.display()
