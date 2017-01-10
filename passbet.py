# Pass bet portion of the Craps game.

import random
import miscfunctions
import images

# Get the amount of money the user wants to bet on the initial roll and subtract it from their chipcount.
# Return the bet and their chip count.
def placePassBet(money):
    print('\nHow many chips would you like to place on the Pass Line?')
    bet=input('$') # User's initial bet
    test=miscfunctions.checkEntry(bet)
    while test==False: # Ensure the bankroll is all digits.
        print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to place on the Pass Line?')
        bet=input('$')
        test=miscfunctions.checkEntry(bet)
    bet=float(bet)
    while bet>money:
        print('\nThat is more money than you have chips for, please try again.')
        print('How many chips would you like to place on the Pass Line?')
        bet=input('$') # User's initial bet
        test=miscfunctions.checkEntry(bet)
        while test==False: # Ensure the bankroll is all digits.
            print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to place on the Pass Line?')
            bet=input('$')
            test=miscfunctions.checkEntry(bet)
        bet=float(bet)
    money-=bet # keep track of user's total money
    return money, bet

# Get the values for each of the 2 dice and their total; returns win, lose, or continue.
def rollPassDice():
    print("\nLet's roll the dice!\nPress ENTER to roll.")
    input()
    print("***ROLLING***ROLLING***ROLLING***")
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    # Display the roll.
    images.dicePicture(dice1, dice2)
    roll=dice1+dice2
    print("The dice rolled a", dice1, "and a", dice2, "totaling", roll)
    if 3<roll<7 or 7<roll<11:
        outcome='continue'
    else:
        if roll==7 or roll==11:
            outcome='win'
        else:
            outcome='lose'
    return roll, outcome


def winInitialRoll(chipcount, bet):
    winnings=bet*2
    print('\nYou win the pass roll and doubled your bet! You won $', format(winnings, ',.2f'), sep='')
    chipcount+=winnings
    return chipcount


