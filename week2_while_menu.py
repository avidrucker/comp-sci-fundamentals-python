"""
SDM:

- give the user some choices
- ask the user to make a choice using a number
- tell the user that you got in their choice
- confirm that the user made a valid choice (from the list of options)

"""

asking = True

while asking:
    print("Choices:\n1. Apple\n2. Orange\n3. Banana")
    choice = int(input("Please choose a fruit (1, 2, or 3):"))
    print(f"You chose choice #{choice}")

    if choice == 1 or choice == 2 or choice == 3:
        asking = False
    else:
        print("Please only type in 1, 2, or 3 ;)")

print("Thank you for making a valid choice!")
