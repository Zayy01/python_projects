print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
chosen_path = input('    Type "left" or "right"\n')

if chosen_path == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    chosen_path2 = input('Type "wait" to wait for a boat. Type "swim" to swim across\n')
    if chosen_path2 == "wait":
        print("You arrive at the island unharmed. THere is a house with 3 doors.")
        color_door = input("One red, one yellow and one blue. Which color do you choose?\n")
        if color_door == "red":
            print("It's a room full of fire and you were burned alive. Game Over.")
        if color_door == "blue":
            print("You entered a room of beasts and was eaten. Game Over.")
        if color_door == "yellow":
            print("You found the treasure! You Win!")
    else:
        print("You were attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game over.")