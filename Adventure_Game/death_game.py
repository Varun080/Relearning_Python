name = input ("Type your name: ")
print("Welcome",name,"to this adventure!")

answer = input(
"""
You are on a dirt road, it has come to an end you can go left or right.
Which option would you like to choose?
"Left"  or  "Right"
Choose wisely......
"""
).lower()

if answer == "left":
    answer = input(
        """
        You come to a river, you can walk around it or swim accross.
        "Walk" to walk around.
        and 
        "Swim" to swim accross.
        """
    ).lower()
    if answer == "swim":
        print("You tried to swam accros and eaten by an alligator and died.(x0x)")
    elif answer == "walk":
        print("You walked for many miles and got tired and died.(x0x)")
    else:    
        print("Not a valid option. You lose,")


elif answer == "right":
    answer = input(
        """
        You came to a bridge, it looks wobbly, do you want to cross it or go back
        "Cross" to cross the wobbly bridge.
        and
        "Back" to go back to the dirt road.        
        """
    ).lower()
    if answer == "back":
        print("You got lost on the wacy back and died of hunger.(x0x)")
    elif answer == "cross":
        print("You tried to cross the bridge, bridge was wobbly. You fall into the dithc and died.(x0x)")
    else:
        print("Not a valid option. You lose,")
else:
    
    print("Not a valid option. You lose.")

