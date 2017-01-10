# Craps game

import random
import intro
import passbet
import comebet
import endgame

def crapsMain(usersMoney):
    keepGoing='y'
    intro.crapsInstructions()
    while usersMoney>0 and keepGoing!='done' and keepGoing!='DONE':
        usersMoney, passBet=passbet.placePassBet(usersMoney) # Get the user's initial bet.
        print('\nYour current chip count is $', format(usersMoney, ',.2f'), sep='')
        dice, initialRoll=passbet.rollPassDice() # roll the dice
        # Different paths for the dice roll outcome.
        if initialRoll=='win':
            usersMoney=passbet.winInitialRoll(usersMoney, passBet)
        elif initialRoll=='lose':
            print("\nSorry for your loss.")
        elif initialRoll=='continue':
            usersMoney=comebet.comePortion(dice, usersMoney, passBet)
        print('\nYour current chip count is $', format(usersMoney, ',.2f'), sep='')
        keepGoing=input('Press "Enter" to continue playing, otherwise type in "done": ')
    endgame.endGameDisplay(usersMoney)
    return usersMoney
# call the main function

