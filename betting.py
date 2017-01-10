# betting functions for blackjack

import miscfunctions

def initialBet(chipCount):
    print('\nHow many chips would you like to bet?')
    bet=input('$') # User's initial bet
    test=miscfunctions.checkEntry(bet)
    while test==False: # Ensure the bankroll is all digits.
        print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
        bet=input('$')
        test=miscfunctions.checkEntry(bet)
    bet=float(bet)
    while bet>chipCount:
        print('\nThat is more money than you have chips for, please try again.')
        print('How many chips would you like to bet?')
        bet=input('$') # User's initial bet
        test=miscfunctions.checkEntry(bet)
        while test==False: # Ensure the bankroll is all digits.
            print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
            bet=input('$')
            test=miscfunctions.checkEntry(bet)
        bet=float(bet)
    chipCount-=bet # keep track of user's total money
    return chipCount, bet

def insuranceBet(chipCount):
    print('\nHow many chips would you like to bet?')
    bet=input('$') # User's initial bet
    test=miscfunctions.checkEntry(bet)
    while test==False: # Ensure the bankroll is all digits.
        print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
        bet=input('$')
        test=miscfunctions.checkEntry(bet)
    bet=float(bet)
    while bet>chipCount:
        print('\nThat is more money than you have chips for, please try again.')
        print('How many chips would you like to bet?')
        bet=input('$') # User's initial bet
        test=miscfunctions.checkEntry(bet)
        while test==False: # Ensure the bankroll is all digits.
            print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
            bet=input('$')
            test=miscfunctions.checkEntry(bet)
        bet=float(bet)
    chipCount-=bet # keep track of user's total money
    print()
    return chipCount, bet

def preFlopBet(chipCount,ante):
    print('\nHow many chips would you like to bet?')
    bet=input('$') # User's initial bet
    test=miscfunctions.checkEntry(bet)
    while test==False: # Ensure the bankroll is all digits.
        print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
        bet=input('$')
        test=miscfunctions.checkEntry(bet)
    bet=float(bet)
    while bet>chipCount or bet>ante*4 or bet<ante*3:
        print('\nThat is not a valid bet, please try again.')
        print('How many chips would you like to bet?')
        bet=input('$') # User's initial bet
        test=miscfunctions.checkEntry(bet)
        while test==False: # Ensure the bankroll is all digits.
            print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
            bet=input('$')
            test=miscfunctions.checkEntry(bet)
        bet=float(bet)
    chipCount-=bet # keep track of user's total money
    return chipCount, bet

def flopBet(chipCount,ante):
    print('\nHow many chips would you like to bet?')
    bet=input('$') # User's initial bet
    test=miscfunctions.checkEntry(bet)
    while test==False: # Ensure the bankroll is all digits.
        print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
        bet=input('$')
        test=miscfunctions.checkEntry(bet)
    bet=float(bet)
    while bet>chipCount or bet!=ante*2:
        print('\nThat is not a valid bet, please try again.')
        print('How many chips would you like to bet?')
        bet=input('$') # User's initial bet
        test=miscfunctions.checkEntry(bet)
        while test==False: # Ensure the bankroll is all digits.
            print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
            bet=input('$')
            test=miscfunctions.checkEntry(bet)
        bet=float(bet)
    chipCount-=bet # keep track of user's total money
    return chipCount, bet

def endBet(chipCount, ante):
    print('\nHow many chips would you like to bet?')
    bet=input('$') # User's initial bet
    test=miscfunctions.checkEntry(bet)
    while test==False: # Ensure the bankroll is all digits.
        print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
        bet=input('$')
        test=miscfunctions.checkEntry(bet)
    bet=float(bet)
    while bet>chipCount or bet!=ante:
        print('\nThat is not a valid bet, please try again.')
        print('How many chips would you like to bet?')
        bet=input('$') # User's initial bet
        test=miscfunctions.checkEntry(bet)
        while test==False: # Ensure the bankroll is all digits.
            print('That was not an acceptable amount of dollars.\n\nHow many chips would you like to bet?')
            bet=input('$')
            test=miscfunctions.checkEntry(bet)
        bet=float(bet)
    chipCount-=bet # keep track of user's total money
    return chipCount, bet
