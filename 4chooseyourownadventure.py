name = input("Type your name: ")
print("welcome ", name, "to this adventure!")

answer = input(
    "you are on a dirt road, it has come to an end and you can go left or right. which way would like to go? "
).lower()

if answer == "left":
    answer = input(
        "You come to a river. and you can walk around or you can swim across? Type walk to walk around and swim to swim accross: "
    ).lower()
    if answer == "swim":
        print("you swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game")
    else:
        print("you choose invalid option. you loose.")
elif answer == "right":
    answer = input(
        "You come across the bridge, it looks woobly, do you want to cross it or head back(across/back)? "
    ).lower()
    if answer == "back":
        print("you go back and lose.")
    elif answer == "across":
        answer = input(
            "you come across the bridge and meet a stranger. Do you want to talk them (yes/no)? "
        ).lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!...:)")
        elif answer == "no":
            print("You ignore a stranger and they are offended and You lose. :( ")
        else:
            print("you choose invalid option you lose")
    else:
        print("you choose invalid option. you lose.")

else:
    print("you choose invalid option. you loose")

print("Thank you for Trying", name)
