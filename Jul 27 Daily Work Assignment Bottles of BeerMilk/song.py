def song(startNum):
    for startNum in range(startNum, 0, -1):
        if startNum == 1 or startNum == 0:
            print("1 bottle of water on the wall, 1 bottle of water")
            print("Take one down, pass it around, no more bottles of water on the wall!")
        else:
            print(f"{startNum} bottles of water on the wall, {startNum} bottles of water.")
            print(f"Take one down, pass it around, {startNum - 1} bottles of water on the wall.\n")


while True:
    try:
        startNum = int(input())
        song(startNum)
    except ValueError:
        print('\33[101m' + "EXCEPTION please enter a number!" + '\x1b[0m')
    else:
        break
