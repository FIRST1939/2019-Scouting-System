from tkinter import *
from tkinter import ttk
from tkinter import font

"""
Created on Thu Jun 13 17:13:56 2019

@author: Mason
"""
yeet= False

def getRoundOneList():
    numTeams = int(input('Enter the number of teams(max 17) you would like to enter for round one here: '))
    selection = 1
    roundOneList = []    
    print('Congratulations on making the top 8!')
    for x in range(0, numTeams):
        print('Enter team #',(x+1),' on your round one picklist here:')
        roundOneList[x] = int(input())        
        print(' ')
    
    while selection != 0:
        for x in range(0, numTeams):
                print('The #', (x+1), 'team on your list is team',roundOneList[x])
        print(' ')
        print('Enter 0 if this is correct')
        print('Enter the position in the list order you want to change if this is incorrect')
        selection = int(input('Enter Selection:'))
        
           
        for x in range(0, numTeams):
            if selection == (x+1):
                print ('Re-enter pick', (x+1), 'here:')
                roundOneList[x] = int(input())
                print(' ')

        if selection > numTeams | selection <0:
            print('Please enter a valid number')
    print(' ')   
    return roundOneList

def getRoundTwoList():
    numTeams = int(input('Enter the number of teams(max 34) you would like to enter for round two here: '))
    selection = 1
    roundTwoList = []   
    for x in range(0, numTeams):
            print('Enter team #',(x+1),' on your round two picklist here:')
            roundTwoList[x] = int(input())        
            print(' ')
    
    while selection != 0:
        for x in range(0, numTeams):
                print('The #', (x+1), 'team on your list is team',roundTwoList[x])
        print(' ')
        print('Enter 0 if this is correct')
        print('Enter the position in the list order you want to change if this is incorrect')
        selection = int(input('Enter Selection:'))
        
           
        for x in range(0, numTeams):
            if selection == (x+1):
                print ('Re-enter pick', (x+1), 'here:')
                roundTwoList[x] = int(input())
                print(' ')

        if selection > numTeams | selection <0:
            print('Please enter a valid number')
    print(' ')   
    return roundTwoList

    
def topEightPicker():
    roundOneList = getRoundOneList()
    roundTwoList = getRoundTwoList()


print('Welcome to the alliance selection tool. Enter your team number to begin:')
teamNum = input()

ourAlliance = [teamNum]
while yeet is False:
    yeet = True
    print('Enter 1 if you are in a picking position')
    print('Enter 2 if you might be in a picking position')
    print('Enter 3 if you won\'t be in a picking position')
    selection = input('Enter Number: ')
    if selection == '1':
        topEightPicker()
    elif selection == '2':
         print('you chose option 2')
    elif selection == '3':
         print('you chose option 3')
    else:
        print('Enter a valid response')
        print(' ')
        yeet = False
    