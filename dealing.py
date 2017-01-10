# dealing

import cardMaker
import time
import betting
import metaGame

def dealUTH(deck, chipCount, bet):
    print('\nLets deal out the cards!\n')
    skip=False
    # Deal out the initial cards as lists into the player's hand and dealer's hand
    playerHand=[]
    dealerHand=[]
    playerHand.append(deck[0])
    playerHand.append(deck[2])
    dealerHand.append(deck[1])
    dealerHand.append(deck[3])
    # Slice off the first 4 cards of the deck.
    deck=deck[4:]
    # Convert the cards to a format of [card face, card value]
    playerHand[0]=cardMaker.convertCard(playerHand[0])
    playerHand[1]=cardMaker.convertCard(playerHand[1])
    dealerHand[0]=cardMaker.convertCard(dealerHand[0])
    dealerHand[1]=cardMaker.convertCard(dealerHand[1])
    # Display the cards on the screen. Hide the last dealer card.
    time.sleep(1)
    print('Player:    ', playerHand[0][0], '\nDealer:')
    time.sleep(1)
    print('\nPlayer:    ', playerHand[0][0], '\nDealer:     ??????')
    time.sleep(1)
    print('\nPlayer:    ', playerHand[0][0], '  ', playerHand[1][0], '\nDealer:     ??????')
    time.sleep(1)
    print('\nPlayer:    ', playerHand[0][0], '  ', playerHand[1][0], '\nDealer:     ??????        ??????')
    time.sleep(3)
    # See if the player wants to make a pre flop bet.
    print('\nWould you like to bet pre-flop? You must bet 3X-4X your initial bet.\nEnter "yes" to bet. ', end='')
    wager=input()
    if wager.lower()=='yes' or wager.lower()=='y':
        skip=True
        chipCount, bet2=betting.preFlopBet(chipCount, bet)
    tableCards=[]
    tableCards.append(deck[0])
    tableCards.append(deck[1])
    tableCards.append(deck[2])
    tableCards.append(deck[3])
    tableCards.append(deck[4])
    tableCards[3]=cardMaker.convertCard(tableCards[3])
    tableCards[4]=cardMaker.convertCard(tableCards[4])
    tableCards[0]=cardMaker.convertCard(tableCards[0])
    tableCards[1]=cardMaker.convertCard(tableCards[1])
    tableCards[2]=cardMaker.convertCard(tableCards[2])
    time.sleep(1)
    print('\nPlayer:    ', playerHand[0][0], '  ', playerHand[1][0], '\nTable Cards:', tableCards[0][0], tableCards[1][0], tableCards[2][0]) 
    print('Dealer:     ??????        ??????')
    time.sleep(3)
    if skip==False:
        print('\nWould you like to bet before the turn and river cards?\nYou must bet 2X your initial bet.\nEnter "yes" to bet. ', end='')
        wager=input()
        if wager.lower()=='yes' or wager.lower()=='y':
            skip=True
            chipCount, bet2=betting.flopBet(chipCount, bet)
    time.sleep(1)
    print('\nPlayer:   ', playerHand[0][0], '  ', playerHand[1][0], '\nTable Cards:', tableCards[0][0], tableCards[1][0], tableCards[2][0], tableCards[3][0], tableCards[4][0]) 
    print('Dealer:    ??????        ??????')
    time.sleep(3)
    if skip==False:
        print('\nWould you like to bet or fold?\nYou must bet your initial bet to stay in the hand.\nEnter "yes" to bet or "fold" to fold.' , end='')
        wager=input()
        while wager.lower()!='yes' or wager.lower()!='y' or wager.lower()!='fold':
            print('\nThat is an invalid input, please enter "bet" or "fold". ', end='')
            wager=input()
        if wager.lower()=='yes' or wager.lower()=='y':
            skip=True
            chipCount, bet2=betting.endBet(chipCount, bet)
        else:
            
            return deck, chipCount
    
            
        
    

def dealBlackJack(deck, chipCount, bet):
    print('\nLets deal out the cards!\n')
    # Deal out the initial cards as lists into the player's hand and dealer's hand
    playerHand=[]
    dealerHand=[]
    playerHand.append(deck[0])
    playerHand.append(deck[2])
    dealerHand.append(deck[1])
    dealerHand.append(deck[3])
    # Set splitting:
    if playerHand[0]%13==playerHand[1]%13:
        split=True
    # Slice off the first 4 cards of the deck.
    deck=deck[4:]
    # Convert the cards to a format of [card face, card value]
    playerHand[0]=cardMaker.convertCard(playerHand[0])
    playerHand[1]=cardMaker.convertCard(playerHand[1])
    dealerHand[0]=cardMaker.convertCard(dealerHand[0])
    dealerHand[1]=cardMaker.convertCard(dealerHand[1])
    # Display the cards on the screen. Hide the last dealer card.
    time.sleep(1)
    print('Player:   ', playerHand[0][0], '\nDealer:')
    time.sleep(1)
    print('\nPlayer:   ', playerHand[0][0], '\nDealer:   ', dealerHand[0][0])
    time.sleep(1)
    print('\nPlayer:   ', playerHand[0][0], '  ', playerHand[1][0], '\nDealer:   ', dealerHand[0][0])
    time.sleep(1)
    print('\nPlayer:   ', playerHand[0][0], '  ', playerHand[1][0], '\nDealer:   ', dealerHand[0][0], '    ??????')
    # If the dealers show card is an Ace (worth 11 initially).
    if dealerHand[0][1]==11:
        insurance=False
        # If the value of the player's hand and the dealer's hand are both 21 initially, there is a push.
        if (playerHand[0][1]+playerHand[1][1])==21 and (dealerHand[0][1]+dealerHand[1][1])==21:
            time.sleep(2)
            print('\nPlayer:   ', playerHand[0][0], '  ', playerHand[1][0], '\nDealer:   ', dealerHand[0][0], '  ', dealerHand[1][0])
            print('\nThere is a push! You get your wager back.')
            # Add the bet back to the chipCount, return the chipCount and the shortened deck.
            chipCount+=bet
            return chipCount, deck
        # If the dealer does not have Blackjack (21) but player does, pay out 2.5X the bet. return the chipCount and current deck.
        elif (playerHand[0][1]+playerHand[1][1])==21:
            time.sleep(2)
            print('\nCongratulations! You hit a BLACKJACK!')
            winnings=bet*2.5
            chipCount+=winnings
            print('You won $', format(winnings, ',.2f'),'.', sep='')
            return chipCount, deck
        # If there was no push, ask for insurance against the dealer having '21'.
        print('\nType "insurance" to purchase insurance, or press enter to skip.')
        insurance=input()
        # If the player takes insurance, get the bet amount from insuranceBet()
        insuranceBet=0
        if insurance=='insurance':
            chipCount, insuranceBet=betting.insuranceBet(chipCount)
        time.sleep(0.5)
        print('***peeking***')
        time.sleep(0.5)
        # If the dealer's hide card is worth 10, the player loses and any insurance is paid out.
        if dealerHand[1][1]==10:
            print('\nPlayer:   ', playerHand[0][0], '  ', playerHand[1][0], '\nDealer:   ', dealerHand[0][0], '  ', dealerHand[1][0])
            print('\nThe dealer has BLACKJACK!')
            # No insurance was taken, player loses bet. Only return chipCount and current deck.
            if insurance==False:
                print('Sorry for your loss.')
                return chipCount, deck
            # Insurance was taken, bet is doubled and added to chipCount. Return chipCount and current deck.
            else:
                winnings=insuranceBet*2
                chipCount+=winnings
                print('You won $', format(winnings, ',.2f'),' with your insurance bet!', sep='')
                return chipCount, deck
        # Else the dealer's hide card is not worth 10 and the player can hit.
        else:
            playerHand, deck, playerTotal, doubleDown=metaGame.hitting(playerHand, dealerHand, deck)
            if doubleDown==True:
                bet*=1.5
            if playerTotal>21:
                time.sleep(2)
                print('You busted!')
                return chipCount, deck
            else:
                deck, dealerTotal=metaGame.dealerPlay(playerHand, dealerHand, deck)
                if dealerTotal>21 or dealerTotal<playerTotal:
                    winnings=bet*2
                    chipCount+=winnings
                    time.sleep(2)
                    if dealerTotal>21:
                        print('The dealer has busted!\nYou have won $', format(winnings, ',.2f'), '.', sep='')
                    else:
                        print('You beat the dealer!\nYou have won $', format(winnings, ',.2f'), '.', sep='')
                    return chipCount, deck
                elif dealerTotal==playerTotal:
                    time.sleep(2)
                    print('\nThere is a push! You get your wager back.')
                    # Add the bet back to the chipCount, return the chipCount and the shortened deck.
                    if doubleDown==True:
                        bet=(bet/3)*2
                    chipCount+=bet
                    return chipCount, deck
                else:
                    time.sleep(2)
                    print('The dealer wins the hand!')
                    return chipCount, deck
    # If the dealer does not show Ace and the player has Blackjack (21), pay out 2.5X the bet. return the chipCount and current deck.
    elif (playerHand[0][1]+playerHand[1][1])==21:
        time.sleep(2)
        print('\nCongratulations! You hit a BLACKJACK!')
        winnings=bet*2.5
        chipCount+=winnings
        print('You won $', format(winnings, ',.2f'),'.', sep='')
        return chipCount, deck

    # If split was True.
    #if split==True:
        #choice=input('Would you like to split your cards? Type "split" to split! ')
        #if choice==split:
            

    # If no initial winner, the player can hit.
    else:
        playerHand, deck, playerTotal, doubleDown=metaGame.hitting(playerHand, dealerHand, deck)
        if doubleDown==True:
            bet*=1.5
        if playerTotal>21:
            time.sleep(2)
            print('You busted!')
            return chipCount, deck
        else:
            deck, dealerTotal=metaGame.dealerPlay(playerHand, dealerHand, deck)
            if dealerTotal>21 or dealerTotal<playerTotal:
                winnings=bet*2
                chipCount+=winnings
                time.sleep(2)
                if dealerTotal>21:
                    print('\nThe dealer has busted!\nYou have won $', format(winnings, ',.2f'), '.', sep='')
                else:
                    print('\nYou beat the dealer!\nYou have won $', format(winnings, ',.2f'), '.', sep='')
                return chipCount, deck
            elif dealerTotal==playerTotal:
                time.sleep(2)
                print('\nThere is a push! You get your wager back.')
                # Add the bet back to the chipCount, return the chipCount and the shortened deck.
                chipCount+=bet
                return chipCount, deck
            else:
                time.sleep(2)
                print('\nThe dealer wins the hand!')
                return chipCount, deck
        
