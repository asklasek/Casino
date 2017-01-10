# Casino main

import intro
import CrapsBeta
import BlackJackBeta
import endgame

def main():
    # set newTable to yes to keep game going.
    newTable='yes'
    # Load an existing user, or enter a new user.
    name, userMoney=intro.loadProfile()
    # Run the game.
    while newTable=='yes' or newTable=='YES' or newTable=='Yes' or newTable=='y' or newTable=='Y':
        # User chooses a game.
        game=intro.chooseGame()
        if game=='craps':
            userMoney=CrapsBeta.crapsMain(userMoney)
        else:
            userMoney=BlackJackBeta.blackjackMain(userMoney)
        # See if user wants to stop playing.
        print('Would you like to play at a new table? Enter yes or no.')
        newTable=input()
    print('Thanks for playing! Your account total has been updated.')
    endgame.saveUser(name, userMoney)
    endgame.displayHighScores()
    input()
main()
