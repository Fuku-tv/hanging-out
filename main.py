


# This is the start of the text adventure game
# the player will make choices and the game will change based on those choices

from time import sleep


print("You are in a dope room.")
sleep(1)
print("There is a TV facing the couch and a telephone on the wall.")
sleep(1)
print("what do you do? ")
print("1. Watch TV")
print("2. pick up the  telephone")

player_input = None
while player_input != 'exit':
    player_input = input("> ")
    if player_input == "1":
        print("You watch the TV and it's a good show.")
        sleep(1)
        print("You feel better.")
    
    elif player_input == "2":
        print("You pick up the telephone and it's a good one.")
        sleep(1)
        print("you feel hungry for pizza, but you don't want to go to the pizza place.")
        sleep(1)
        print("You can also call your buds to hang out.")
        sleep(1)
        print("What do you do? ")
        print("1. Go to the pizza place")
        print("2. Call your buds")
        print("3. Call your mom")
        print("4. Call your dad")
        print("5. Call your sister")
        player_input = input("> ")
        if player_input == "1":
            print("You go to the pizza place and you get pizza.")
            sleep(1)
            print("You feel better.")
        else:
            print("You call your buds and they are there.")
            sleep(1)
            print("You feel better.")
        
        


# This is the player's first choice
# The player will be prompted to enter a choice




# This is the player's second choice
# The player will be prompted to enter a choice
