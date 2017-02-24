import random

roll_again= "yes"

while roll_again=="yes" or roll_again=="y":
    print("Dices is Rolling..")
    print("the value is...")
    print (random.randint(1,6))
    roll_again= input("Do you want to Roll Again?")

    
