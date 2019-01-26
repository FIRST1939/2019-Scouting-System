from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import Tk
from tkinter import font
from tkinter import messagebox
import match_dbconn
import os

win = Tk()

bigfont = font.Font(family="Times",size=20)
win.option_add("*Font",bigfont)


currentMatch = StringVar(value='1')
nextMatch = int()
labelstrs = {}
teams = {}
labels = {}

def popup_keyboard(event):
    os.popen('matchbox-keyboard','r',4096)

def getMatch():
    team_no = match_dbconn.getMatchInfo(match_no,position)
    title_str = "MATCH NO: %s TEAM NO: %s  Postion %s" %(match_no,team_no,position)
    win.title(title_str)
    print(team_no)
    
def badData():
    labels[pos].config(bg="green")
    
def setCurrentMatch():
    #currentMatch.get()
    global match_no
    print("Match = ",matchEntry.get())
    match_dbconn.setCurrentMatch(matchEntry.get())
    match_no = matchEntry.get()
    matchButton.config(bg="green")
    matchButton.config(activebackground="green")
    updateInfoLabels()

def nextCurrentMatch():
    nextMatch = int(matchEntry.get()) + 1
    currentMatch.set(str(nextMatch))
    matchButton.config(bg="red")
    matchButton.config(activebackground="red")
    
def updateInfoLabels():
    global match_no
    print("Getting for = ", match_no)   
   # print("Getting for = ",currentMatch.get())  
    for pos in ['R1','R2','R3','B1','B2','B3']:
        row = match_dbconn.getAllMatchInfo(match_no,pos)
     #   row = match_dbconn.getAllMatchInfo(currentMatch.get(),pos)
        print(row[0],row[1])
        if row[1] is None:
            scoutName = "XXXXXXXXXX"
        else:
            scoutName = row[1]
        
        labelstrs[pos] = pos + " " + str(row[0]) + " " + scoutName
        teams[pos] = row[0]
    strLabelR1.set(labelstrs["R1"])
    strLabelR2.set(labelstrs["R2"])
    strLabelR3.set(labelstrs["R3"])
    strLabelB1.set(labelstrs["B1"])
    strLabelB2.set(labelstrs["B2"])
    strLabelB3.set(labelstrs["B3"])
#    checkScoutStatus()

def checkScoutStatus():
    global match_no
    match = match_no
 #   print("checkScoutStatus match = ",match)
    for pos in ['R1','R2','R3','B1','B2','B3']:
        team = teams[pos]
        id = match_dbconn.checkScoutData(match,team)
 #       print(pos,"  ",id)
        if id == 1:
            labels[pos].config(bg="green")
        else:
            if pos[0] == 'R':
                labels[pos].config(bg="red")
            else:
                labels[pos].config(bg="blue")      
    win.after(2000,checkScoutStatus)
    
              

def exitButton():
    print("Here")
    global win
    win.quit()
    win.destroy()

def resetButton():
    print("Attempting Reset")
    result = messagebox.askyesno("Resetting Data Check" "Are you sure you want to reset?")
    print (result)
    if result:
        print("deleting")
    else:
        print("notdeleting")

#Match No
matchEntry = Entry(win,textvariable=currentMatch)
matchEntry.bind('<Button-1>',popup_keyboard)
matchEntry.grid(row = 1,column = 2)

matchButton = Button(win,text='Set',command=setCurrentMatch)
matchButton.config(bg="red")
matchButton.config(activebackground="red")
matchButton.grid(row=1,column = 3)


matchNext = Button(win,text='Next',command=nextCurrentMatch)
matchNext.grid(row=1,column = 4)

strLabelR1 = StringVar()
infoLabelR1 = Label(win,textvariable=strLabelR1)
infoLabelR1.config(bg="red")
infoLabelR1.grid(row=2,column=1)

strLabelR2 = StringVar()
infoLabelR2 = Label(win,textvariable=strLabelR2)
infoLabelR2.config(bg="red")
infoLabelR2.grid(row=3,column=1)

strLabelR3 = StringVar()
infoLabelR3 = Label(win,textvariable=strLabelR3)
infoLabelR3.config(bg="red")
infoLabelR3.grid(row=4,column=1)

strLabelB1 = StringVar()
infoLabelB1 = Label(win,textvariable=strLabelB1)
infoLabelB1.config(bg="blue")
infoLabelB1.grid(row=2,column=2)

strLabelB2 = StringVar()
infoLabelB2 = Label(win,textvariable=strLabelB2)
infoLabelB2.config(bg="blue")
infoLabelB2.grid(row=3,column=2)

strLabelB3 = StringVar()
infoLabelB3 = Label(win,textvariable=strLabelB3)
infoLabelB3.config(bg="blue")
infoLabelB3.grid(row=4,column=2)

labels["R1"] = infoLabelR1
labels["R2"] = infoLabelR2
labels["R3"] = infoLabelR3
labels["B1"] = infoLabelB1
labels["B2"] = infoLabelB2
labels["B3"] = infoLabelB3
 
exitButton = Button(win,text = "Exit", command=exitButton)
exitButton.grid(row=6,column=4)

resetButton = Button(win,text = "Reset Match Data", command=resetButton)
resetButton.grid(row=5,column=3, columnspan=2)
                 

win.geometry('800x480')

match_no = '1'
updateInfoLabels()
checkScoutStatus()            

win.mainloop()
