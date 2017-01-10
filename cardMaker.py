import random
import time

# makeDeck(game) will create a deck to 'draw' cards from. The game will indicate
# how many decks are combined. 
def makeDeck(game):
    time.sleep(0.5)
    print('\nLet me shuffle the deck.\n')
    time.sleep(0.5)
    print('***SHUFFLE***SHUFFLE***SHUFFLE***\n')
    time.sleep(0.5)
    print('***SHUFFLE***SHUFFLE***SHUFFLE***')
    time.sleep(1)
    deck=list(range(1,53))
    if game=='blackjack':
        deck=deck*6
    elif game=='ultimateTexasHoldem':
        deck=deck*1
    random.shuffle(deck)
    return deck

# convertCard will convert the card from the number to the corresponding card.
# Diamond, Heart, Club, Spade. 1=Ace, 11=Jack, 12=Queen, 13=King.
def convertCard(card):
    suit=card/13 # intiger divide to find the suit.
    if suit<=1.0:
        suit=' Diamonds'
    elif suit<=2.0:
        suit=' Hearts  '
    elif suit<=3.0:
        suit=' Clubs   '
    else:
        suit=' Spades  '
    rem=card%13 # remainder divide to find the cards number.
    if rem==1:
        num='A'
        value=11
    elif rem==2:
        num='2'
        value=2
    elif rem==3:
        num='3'
        value=3
    elif rem==4:
        num='4'
        value=4
    elif rem==5:
        num='5'
        value=5
    elif rem==6:
        num='6'
        value=6
    elif rem==7:
        num='7'
        value=7
    elif rem==8:
        num='8'
        value=8
    elif rem==9:
        num='9'
        value=9
    elif rem==10:
        num='10'
        value=10
    elif rem==11:
        num='J'
        value=10
    elif rem==12:
        num='Q'
        value=10
    else:
        num='K'
        value=10
    # card=[card face, card suit, value]
    card=[]
    card.append(num+suit)
    card.append(value)
    return card
