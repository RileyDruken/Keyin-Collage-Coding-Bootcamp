

def email_send(name,age,birthday,sender):
    ordinal = lambda age: "%d%s" % (age, "tsnrhtdd"[(age // 10 % 10 != 1) * (age % 10 < 4) * age % 10::4])
    template = \
    f"""    Hello {name},
    It is understood that today,
    {birthday} is your {ordinal(age)} birthday!
    I/We would like to wish you a very happy birthday!
    
    
    Warmest Regards,
      {sender}
    """
    print(template)
    return template



name = input("To? ")
age = int(input("Their age? "))
birthday = input("Their Birthday? ")
sender = input("Your name? ")


email_send(name,age,birthday,sender)