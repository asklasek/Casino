# Ultimate Texas Holdem

import cardMaker
import betting
import dealing


def uPokerMain(usersMoney):
    keepGoing='y'
    #intro.uPokerInstructions()
    deck=cardMaker.makeDeck('ultimateTexasHoldem')
    while usersMoney>0 and keepGoing.lower()!='done':
        if len(deck)<32: # If deck gets low remake the deck.
            print('\nWe are running low on cards, lets shuffle the deck.')
            deck=cardMaker.makeDeck('blackjack')
        usersMoney, bet=betting.initialBet(usersMoney) # The user makes a bet.
        usersMoney, deck=dealing.dealUTH(deck,usersMoney, bet) # Deal the cards, run the game.

uPokerMain(1000)


# Change initial bet to bet less than 4X the chipcount of the user
