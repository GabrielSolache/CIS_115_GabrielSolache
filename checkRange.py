while True:
    val = int(input("Enter a number between 0 and 100: "))
    if val < 0 or val > 100:
        print("sorry, the number you enter is out of range?!")
        break