# Introduction

import time

def loadProfile():
    # Greet the player. Give them their money!
    print('Welcome to the casino! You can choose between craps or blackjack, whichever game you are feeling lucky at.')
    print('\nGood luck!\n')
    # Check for a saved account.
    print('Do you have a saved account you would like to get your money from?')
    account=input()
    if account=='Y' or account=='y' or account=='YES' or account=='Yes' or account=='yes' or account=='YEs':
        name=input('What is your name? ')
        inFile=open('SavedGames.txt', 'r')
        user=inFile.readline()
        found=False
        while user!='':
            user=user.rstrip('\n')
            money=float(inFile.readline())
            if user==name:
                userMoney=money
                found=True
            user=inFile.readline()
        if found==True:
            print('\nHere is your $', format(userMoney, ',.2f'), sep='')
        else:
            print('\nSorry that account was not found.\nHere is your $1000.00\nGood Luck!')
            userMoney=1000.0
        inFile.close()
    else:
        print('Please enter your name for the Leaderboard.')
        name=input()
        print('Here is your $1000.00\nGood luck!')
        userMoney=1000.00

    return name, userMoney
    
def chooseGame():
    print('\nWhich table would you like to go to? Type "craps" or "blackjack"')
    game=input()
    while game!="craps" and game!="blackjack":
        print('Sorry, we do not have ', game,'.\nWhich table would you like to go to? Type "craps" or "blackjack"', sep='')
        game=input()
    return game


# Greet the player and explain the rules if the player is new.
def crapsInstructions():
    print('Hello! Welcome to the craps table!')
    print('         ___________\t         ___________\n'
    '        /          /|\t        /          /|\n'
    '       /          / |\t       /          / |\n'
    '      /    *     /  |\t      /    *     /  |\n'
    '     /          /  *|\t     /          /  *|\n'
    '    /__________/ *  |\t    /__________/ *  |\n'
    '    |          |   */\t    |          |   */\n'
    '    |  *   *   | * / \t    |  *   *   | * / \n'
    '    |    *     |  /  \t    |    *     |  /  \n'
    '    |  *   *   | /   \t    |  *   *   | /   \n'
    '    |__________|/    \t    |__________|/    \n')
    instructions=input('\nHave you ever played craps before?\nIf not then enter "no" and I will explain the rules.\nOtherwise press "Enter". ')
    if instructions=='no' or instructions=='NO' or instructions=='No' or instructions=='n' or instructions=='N':
        print("\nThe first roll is the 'Pass Roll', if you roll a 7 or 11 on this roll you double your bet!")
        print("If a 2, 3, or 12 is rolled then you lose your bet.")
        print("If any other number is rolled (4, 5, 6, 8, 9, 10) it becomes the Point.")
        print("You can make a place bet on the Point and keep rolling.")
        print("\nThe place bet pays out more than your initial bet on the pass roll, but to win")
        print("you must roll the Point before you roll a 7. If you roll the point then you win")
        print("your initial pass bet and the place bet.")
    print("\nGood Luck!")
    
# Greet the player and explain the rules if the player is new.
def blackjackInstructions():
    print('Hello! Welcome to the Blackjack Table!')
    time.sleep(1.5)
    instructions=input('\nHave you ever played Blackjack before?\nIf not then enter "no" and I will explain the rules.\nOtherwise press "Enter". ')
    if instructions=='no' or instructions=='NO' or instructions=='No' or instructions=='n' or instructions=='N':
        print('You will be playing against the dealer to try to make the highest hand.')
        print('If your cards add up to a higher number than the dealer then you win your bet.')
        print('If there is a tie then you get your bet back with no wins or losses.')
        print('Jacks, Queens, and Kings are worth ten. Aces are worth either eleven or one point.')
        print('If you or the dealer go over 21, it is an automatic bust')
        print('To get an additional card, you can hit. The dealer must hit until their score is more than 16.')
        print('You may also double down, which will double your winnings but you only get 1 more card.')
    time.sleep(1)
    print("\nGood Luck!\n")
    time.sleep(1)
