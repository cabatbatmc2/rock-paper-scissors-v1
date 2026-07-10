#13/02/26: Rock Paper Scissors V1
from easygui import *
import random

selections = ["Rock", "Paper", "Scissors"]
computer = random.choice(selections)

#These are the following rules
#The player gets the choice to play or not. If "yes", the program starts. Else, the program says goodbye.
welcome = buttonbox("Welcome to Rock-Paper-Scissors.\nRock beats scissors. \nPaper beats rock. \nScissors beat paper. \nDo you want to play?", choices = ["Yes", "No"])

#The game exits when the player chose "no"
if welcome == "No":
    msgbox("I understand, goodbye!")

#The main program will start if the player chose "yes"
else:
    def main_program():
        weapon = buttonbox("Choose your weapon.", choices = ["Rock", "Paper", "Scissors"])
        #If the choice of the player and computer are the same , they both will tie.
        if weapon == computer:
            msgbox("It's a tie!")
            
        #Rock beats scissors 
        elif weapon == "Rock":
            if computer == "Scissors":
                msgbox("You chose rock, and the computer chose scissors.")
                msgbox("You win!")
            #But paper beats rock
            else:
                msgbox("The computer picked paper and that beats rock, you lost.")
                
        #Scissors beats paper
        elif weapon == "Scissors":
            if computer == "Paper":
                msgbox("You chose scissors, and the computer chose paper.")
                msgbox("You win!")
            #But Rock beats scissors
            else:
                msgbox("The computer picked rock and that beats scissors, you lost.")

        # Paper beats rock
        elif weapon == "Paper":
            if computer == "Rock":
                msgbox("You chose paper, and the computer chose rock.")
                msgbox("You win!")
            #But Scissors beat paper
            else:
                msgbox("The computer chose rock, you lost.")
                
# Will ask the player if they would like to play again or not
while True:
    main_program()
    repeat = buttonbox("Would you like to play again?", choices = ["Yes", "No"])

    if repeat != "Yes":
        msgbox("Thank you for playing! See you next time.")
        break

    
    
    
