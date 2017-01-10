# meta game


import cardMaker
import time

def hitting(playerHand, dealerHand, deck):
    doubleDown=False
    time.sleep(1)
    print('\nType "dd" to double down and get one card only.')
    hit=input('Type "hit" to get another card, or press "enter" to stay: ')
    index=1
    total=playerHand[0][1]+playerHand[1][1]
    if hit=='dd' or hit=='DD':
        doubleDown=True
        index+=1
        playerHand.append(deck[0])
        playerHand[-1]=cardMaker.convertCard(playerHand[-1])
        deck=deck[1:]
        total+=playerHand[index][1]
        if total>21:
            total=0
            for z in range(index+1):
                if playerHand[z][1]==11:
                    total+=1
                else:
                    total+=playerHand[z][1]
        time.sleep(1)
        print('\nPlayer:   ', end='')
        for x in range(index+1):
            print(playerHand[x][0], '  ', end='')
        print('\nDealer:  ', dealerHand[0][0], '    ??????')
        print()
        return playerHand, deck, total, doubleDown
    while hit=='hit' or hit=='Hit' or hit=='HIT':
        if total<21:
            index+=1
            playerHand.append(deck[0])
            playerHand[-1]=cardMaker.convertCard(playerHand[-1])
            deck=deck[1:]
            total+=playerHand[index][1]
            if total>21:
                total=0
                for z in range(index+1):
                    if playerHand[z][1]==11:
                        total+=1
                    else:
                        total+=playerHand[z][1]
            time.sleep(1)
            print('\nPlayer:   ', end='')
            for x in range(index+1):
                print(playerHand[x][0], '  ', end='')
            print('\nDealer:  ', dealerHand[0][0], '    ??????')
            if total<21:
                time.sleep(1)
                hit=input('\nType "hit" to get another card, or press "enter" to stay: ')
            else:
                print()
                return playerHand, deck, total, doubleDown
        else:
            print()
            return playerHand, deck, total, doubleDown
    return playerHand, deck, total, doubleDown

def dealerPlay(playerHand, dealerHand, deck):
    index=1
    total=dealerHand[0][1]+dealerHand[1][1]
    if dealerHand[0][1]==11 and dealerHand[1][1]==11:
        total=12
    time.sleep(1)
    print('\nPlayer:   ', end='')
    for x in range(len(playerHand)):
        print(playerHand[x][0], '  ', end='')
    print('\nDealer:   ', end='')
    for y in range(index+1):
        print(dealerHand[y][0], '  ', end='')
    while total<17:
        index+=1
        dealerHand.append(deck[0])
        dealerHand[-1]=cardMaker.convertCard(dealerHand[-1])
        deck=deck[1:]
        total+=dealerHand[index][1]
        if total>21:
            total=0
            for z in range(index+1):
                if (dealerHand[z][1])==11:
                    total+=1
                else:
                    total+=dealerHand[z][1]
        #time.sleep(1)
        print('\n\nPlayer:   ', end='')
        for x in range(len(playerHand)):
            print(playerHand[x][0], '  ', end='')
        time.sleep(0.5)
        print('\nDealer:   ', end='')
        for y in range(index+1):
            print(dealerHand[y][0], '  ', end='')
            
    print()
    return deck, total
