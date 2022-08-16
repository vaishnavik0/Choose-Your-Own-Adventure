# CHOOSE YOUR OWN ADVENTRUE

name = input("type your name: ")
print("Welcome", name , "to this adventure! ")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()



if answer == "left":
    answer = input("you come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print("you swam across and were eaten by an alligator.")

    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game")

    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ")

    if answer == "cross":
        answer = input("you cross the bridge and meet the stranger. Do you wanna talk to them (Yes/No)? ")

        if answer == "yes":
            print('You talk to the stranger and you receive your parcle. YOU WIN :)')

        
        elif answer == "no":
            print('You ignore the stranger you didnt receive your parcle. YOU LOSE :(')

        else:
            print('Not a valid option. You lose.')


    elif answer == "back":
        print("You go back and lose")

    else:
        print('Not a valid option. You lose.')

else:
    print("Not a valid option. you lose. ")

print('Thankyou for trying', name)