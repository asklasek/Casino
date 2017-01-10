# Come bets portion of Craps game.

import random
import miscfunctions
import images

# Takes the point, chipcount, and initial bet amount and runs the placeComeBet() and rollComeDice(). Returns the winnings or losses.
def comePortion(point, money, initialBet):
    money, finalBet=placeComeBet(money)
    comeroll=rollComeDice(point)
    if comeroll=='win':
        money=winFinalRoll(point, money, initialBet, finalBet)
        return money
    else:
        print('Sorry for your loss.')
        return money

# Get the amount of money the user wants to bet on the come rolls and subtract it from their chipcount.
# Return the bet and their chip count.
def placeComeBet(money):
    print('\nHow much would you like to bet on the point? You currently have $', format(money, ',.2f'), ' in chips left.', sep='')
    bet=input('$') # User's initial bet
    if bet=='':
        bet='0.0' # No input is a zero dollar bet
        print('$0.00 bet on the point')
    test=miscfunctions.checkEntry(bet)
    while test==False: # Ensure the bankroll is all digits.
        print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to place behin the Pass Line?')
        bet=input('$')
        test=miscfunctions.checkEntry(bet)
    bet=float(bet)
    while bet>money: # Ensure the user has enough chips for the bet
        print('\nThat is more money than you have chips for, please try again.')
        print('How many chips would you like to place on the Pass Line?')
        bet=input('$') # User's initial bet
        test=miscfunctions.checkEntry(bet)
        while test==False: # Ensure the bankroll is all digits.
            print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to place behind the Pass Line?')
            bet=input('$')
            test=miscfunctions.checkEntry(bet)
        bet=float(bet)
    money-=bet # keep track of user's total money
    return money, bet

# Uses the point to see if the user wins or loses after random dice rolls yeilds the point or a 7.
def rollComeDice(point):
    print("\nLet's roll the dice!\nPress ENTER to roll.")
    input()
    print("***ROLLING***ROLLING***ROLLING***")
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    # Display the roll.
    images.dicePicture(dice1, dice2)
    roll=dice1+dice2
    while roll!=7 and roll!=point: # keep rolling until user wins or loses.
        print('You rolled a ', roll,', please roll again!', sep='')
        input()
        print("***ROLLING***ROLLING***ROLLING***")
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        # Display the roll.
        images.dicePicture(dice1, dice2)
        roll=dice1+dice2
    if roll==point:# User wins
        print('You rolled a ', roll,', CONGRATULATIONS!\nYou have hit the Point and won a lot of money!!!!!!', sep='')
        outcome='win'
        return outcome
    else: # User loses.
        print('You rolled a 7.')
        outcome='lose'
        return outcome

# Calculate the total winnings if the user rolls the point:
def winFinalRoll(point, money, initialBet, finalBet):
    if point==6 or point==8:
        multiplier=6/5
    elif point==5 or point==9:
        multiplier=3/2
    else:
        multiplier=2/1
    comeWinnings=finalBet*multiplier+finalBet
    passWinnings=initialBet*2
    chipcount=money+passWinnings+comeWinnings
    return chipcount
