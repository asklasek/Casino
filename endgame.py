# End game functions of the Craps game.
import time
import sys
import os

# Endgame screen from user loss or quiting.
def endGameDisplay(chipCount):
    if chipCount>0:
        print('\nYou walked away from the table with $', format(chipCount, ',.2f'), sep='')

    else:
       print('\nYou are out of chips!\nThanks for playing!')
       time.sleep(5)
       sys.exit()
       
def saveUser(name, chipCount):
    inFile=open('SavedGames.txt', 'r')
    outFile=open('tempFile.txt', 'w')
    line=inFile.readline()
    while line!='':
        if line.rstrip('\n')!=name:
            outFile.write(line)
            line=inFile.readline()
            outFile.write(line)
            line=inFile.readline()
        else:
            line=inFile.readline()
            line=inFile.readline()
    inFile.close()
    outFile.close()
    inFile=open('tempFile.txt', 'r')
    outFile=open('SavedGames.txt', 'w')
    outFile.write(name+'\n')
    outFile.write(str(chipCount)+'\n')
    line=inFile.readline()
    while line!='':
        outFile.write(line)
        line=inFile.readline()
    inFile.close()
    outFile.close()

def displayHighScores():
    print('\n\nWould you like to see the leaderboard? ', end='')
    display=input()
    if display.lower()=='y' or display.lower()=='yes':
        inFile=open('SavedGames.txt', 'r')
        line=inFile.readline()
        while line!='':
            name=line.rstrip('\n')
            line=inFile.readline()
            bankroll=float(line)
            line=inFile.readline()
            print(name, ': $', format(bankroll, ',.2f'), sep='')
        inFile.close()

    
