sum = 0
while (True):
    userInput = input("Enter the price or you can quit by q key: \n")
    if (userInput != "q"):
        sum = sum + int(userInput)
        print(f"Your order total so far {sum}")

    else:
        print(f"Your bill total is {sum}.Thanks for shopping with us")
        break
