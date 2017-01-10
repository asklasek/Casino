# Black Jack ver. 1.0

import random
import cardMaker
import intro
import betting
import dealing
import sys
import time

def blackjackMain(usersMoney):
    keepGoing='y'
    intro.blackjackInstructions()
    deck=cardMaker.makeDeck('blackjack') # Make the deck
    while usersMoney>0 and keepGoing!='done' and keepGoing!='DONE' and keepGoing!='Done':
        if len(deck)<150: # If deck gets low remake the deck.
            print('\nWe are running low on cards, lets shuffle the deck.')
            deck=cardMaker.makeDeck('blackjack')
        usersMoney, bet=betting.initialBet(usersMoney) # The user makes a bet.
        usersMoney, deck=dealing.dealBlackJack(deck,usersMoney, bet) # Deal the cards, run the game.
        print('\nYour current chip count is $', format(usersMoney, ',.2f'), sep='')
        keepGoing=input('Type "done" to leave the table, else press "Enter" to continue playing! ')
    if usersMoney<=0:
        print('\nYou are out of chips. Thanks for playing!')
        time.sleep(5)
        sys.exit()
    else:
        print('\nYou walked away from the table with $', format(usersMoney,',.2f'),'.', sep='')
    return usersMoney

# Didnt count the user ace as a 1 for optional hitting when >17 hand value
