phonebook = {'daniel':'555-5555', 'anna':'555-7777', 'linus':'555-6666'}



print("Names + numbers")
for key, value in phonebook.items():
    print(f"Name: {key},",f"phone number: {value}")

print("adding new item to phonebook dictionary")
phonebook.update({'bob':'555-2222'})

print("numbers only")
for key, value in phonebook.items():
    print(f"phone number: {value}")

print(f"Phonebook length {len(phonebook)}")

for key, value in phonebook.items():
    if key == "daniel" and phonebook:
        print(value)