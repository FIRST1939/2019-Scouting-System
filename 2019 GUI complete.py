     #imports
from tkinter import Entry
from tkinter import Tk
from tkinter import Checkbutton
from tkinter import Button
from tkinter import BooleanVar
from tkinter import IntVar
from tkinter import Label
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import END
from tkinter import Radiobutton
from tkinter import Text
#import os
#import match_dbconn

#opening tkinter
window = Tk() 
window.geometry('800x480')

#Give it some style
style = ttk.Style()
style.theme_settings("default",{"TNotebook.Tab":{"configure":{"padding":[20,20]}}})
labelfont = font.Font(family= "times", size= 20)
window.option_add("*Font", labelfont)
labelfont = ('times', 15)
labelfont2 = ('times', 5)

#add print variables to test here



#some data base stuff
#def getTeam():
#    team_no = match_dbconn.getMatchInfo(match_no,position)
#    title_str = "MATCH NO: %s TEAM NO: %s  Postion %s" %(match_no,team_no,position)
#    window.title(title_str)
#    print(team_no)
#    global teamno
#    teamno = team_no
#    
#def getNextMatch():
#   new_match_no = match_dbconn.getNextMatch();
#    print('new match %s',new_match_no)
#    global match_no
#    global position
#    print('current match %s',match_no)
#    if new_match_no != match_no:
#        print('reinitialize screens')
#        match_no = new_match_no
#        getTeam()
#        btn.config(state = 'enabled')
#        match_dbconn.setScout(Init.get(),match_no,position)
#    window.after(2000,getNextMatch)
#    
#def sendToDatabase():
#    val = selected.get()
#    penalty_yellow = 0
#    penalty_red = 0
#    global teamno
#    if val == 1:
#        penalty_yellow = 1
#    if val == 2:
#        penalty_red = 1
#    match_dbconn.setMatchScout(match_no,
#                               teamno,
#                               ) #export ALL variables within this prin
#



#reinitalize ALL variables here
def reinitscreen():
    crossHABLine_State.set(False)
    dangerousSSDriving_State.set(False)
    attemptLvl1_State.set(False)
    reachLvl1_State.set(False)
    attemptLvl2_State.set(False)
    reachLvl2_State.set(False)
    attemptLvl3_State.set(False)
    reachLvl3_State.set(False)
    deployedRamps_State.set(False)
    attemptDeployedRamps_State.set(False)
    usedAnotherRobot_State.set(False)
    lift_State.set(False)
    attemptLift_State.set(False)
    defense_State.set(False)
    noAttempt_State.set(False)
    groundPickup_State.set(False)   
    SSCargoHatch_Var.set(False)
    SSCargoCargo_Var.set(False)
    touchedRocketLate_State.set(False)
    deadbot_State.set(False)
    badData_State.set(False)
    send_State.set(False)
    SSCargoSSHRocketCargo_Var.set(0)
    SSCargoSSMRocketCargo_Var.set(0) 
    SSCargoSSLRocketCargo_Var.set(0)  
    SSCargoSSHRocketHatch_Var.set(0) 
    SSCargoSSMRocketHatch_Var.set(0)
    SSCargoSSLRocketHatch_Var.set(0) 
    techFoul_Var.set(0) 
    foul_Var.set(0) 
    teleCargoCargo_Var.set(0) 
    teleCargoHatch_Var.set(0) 
    TeleHatchLRocketHatch_Var.set(0) 
    TeleHatchMRocketHatch_Var.set(0)  
    TeleHatchHRocketHatch_Var.set(0) 
    TeleCargoLRocketCargo_Var.set(0) 
    TeleCargoMRocketCargo_Var.set(0)   
    TeleCargoHRocketCargo_Var.set(0)   
    teledropHatch_Var.set(0) 
    teledropCargo_Var.set(0) 
    startRight.set(0)
    startLeft.set(0)
    comments.delete(1.0, END)
    
    #edit the tabs here as needed
tab_control = ttk.Notebook(window)
preMatch = ttk.Frame(tab_control)
sandstorm = ttk.Frame(tab_control)
tele = ttk.Frame(tab_control)
endGame = ttk.Frame(tab_control)
postMatch = ttk.Frame(tab_control)
tab_control.add(preMatch, text='Pre-Match')
tab_control.add(sandstorm, text='Sandstorm')
tab_control.add(tele, text='TeleOp')
tab_control.add(endGame, text='End Game')
tab_control.add(postMatch, text='Post-Match')
tab_control.pack(expand=1, fill='both')

#tele.columnconfigure(1, weight=1)

#keyboard
def popup_keyboard(event):
#    os.popen('matchbox-keyboard','r',4096)
     pass   
    
#put the buttons and spindowns and text boxes and other fun stuff here
crossHABLine_State = BooleanVar(False)
crossHABLine = Checkbutton(sandstorm, text='Cross HAB Line', var=crossHABLine_State)
crossHABLine.grid(row=0, column=0, pady=17)

dangerousSSDriving_State = BooleanVar(False)
dangerousSSDriving = Checkbutton(sandstorm, text='Drove Dangerously during Sandstorm', var=dangerousSSDriving_State)  
dangerousSSDriving.grid(row=5, column =0, pady=15, columnspan=5)

climbLevelLBL = Label(endGame, text='How High did they Climb?')
climbLevelLBL.grid(row=0, column=0)

attemptLvl1_State = BooleanVar(False)
attemptLvl1 = Checkbutton(endGame, text='Attempt Level 1', var=attemptLvl1_State)
attemptLvl1.grid(row=1, column=0)

reachLvl1_State = BooleanVar(False)
reachLvl1= Checkbutton(endGame, text= 'Reach Level 1', var=reachLvl1_State)
reachLvl1.grid(row=1, column=2, pady=12)

attemptLvl2_State = BooleanVar(False)
attemptLvl2= Checkbutton(endGame, text= 'Attempt Level 2', var=attemptLvl2_State)
attemptLvl2.grid(row=2, column=0, pady=12)

attemptLvl3_State = BooleanVar(False)
attemptLvl3= Checkbutton(endGame, text= 'Attempt Level 3', var=attemptLvl3_State)
attemptLvl3.grid(row=3, column=0)

reachLvl2_State = BooleanVar(False)
reachLvl2= Checkbutton(endGame, text= 'Reach Level 2', var=reachLvl2_State)
reachLvl2.grid(row=2, column=2)

reachLvl3_State = BooleanVar(False)
reachLvl3= Checkbutton(endGame, text= 'Reach Level 3', var=reachLvl3_State)
reachLvl3.grid(row=3, column=2, pady=12)

deployedRamps_State = BooleanVar(False)
deployedRamps= Checkbutton(endGame, text= 'Deployed Ramps', var=deployedRamps_State)
deployedRamps.grid(row=4, column=2)

attemptDeployedRamps_State = BooleanVar(False)
attemptDeployedRamps= Checkbutton(endGame, text= 'Attempted to Deploy Ramps', var=attemptDeployedRamps_State)
attemptDeployedRamps.grid(row=4, column=0, pady=17)

usedAnotherRobot_State = BooleanVar(False)
usedAnotherRobot= Checkbutton(endGame, text= 'Tried/Used Another Robot(ramps/another team lifted them)', var=usedAnotherRobot_State)
usedAnotherRobot.grid(row=6, column=0, columnspan=2)

lift_State = BooleanVar(False)
lift= Checkbutton(endGame, text= 'Lifted another bot', var=lift_State)
lift.grid(row=5, column=2)

attemptLift_State = BooleanVar(False)
attemptLift= Checkbutton(endGame, text= 'Attemted to lift another bot', var=attemptLift_State)
attemptLift.grid(row=5, column=0, pady=17)

defense_State = BooleanVar(False)
defense= Checkbutton(tele, text= 'Any Defense Played?', var=defense_State)
defense.grid(row=6, column=0, columnspan=2, pady=15)

noAttempt_State = BooleanVar(False)
noAttempt = Checkbutton(endGame, text= 'Did not try to climb', var=noAttempt_State)
noAttempt.grid(column=0, row=7, pady=17)

groundPickup_State = BooleanVar(False)
groundPickup = Checkbutton(postMatch, text='Did they pickup hatch panels from the ground?', var=groundPickup_State)
groundPickup.grid(row=2, column=0, pady=15)

touchedRocketLate_State = BooleanVar(False)
touchedRocketLate = Checkbutton(postMatch, text = 'Touched the enemy rocket during the last 20 seconds', var=touchedRocketLate_State)
touchedRocketLate.grid(row=0, column=0, pady=12)

deadbot_State = BooleanVar(False)
deadbot = Checkbutton(postMatch, text= 'Deadbot?', var=deadbot_State)
deadbot.grid(row=1, column=0, pady=15)

badData_State = BooleanVar(False)
badData = Checkbutton(postMatch, text='Dont use this data', var=badData_State)
badData.grid(row=5, column=0, pady=40)

cargoHatchLBL = Label(preMatch, text='Started with what in their cargo ship?')
cargoHatchLBL.grid(row=2, column=0, columnspan=2, pady=23)

startRight = IntVar()
cargoRight = Radiobutton(preMatch, text = 'Cargo Right', value=1, var=startRight)
cargoRight.grid(row=3, column=1)
hatchRight = Radiobutton(preMatch, text='Hatch Right', value=2, var=startRight)
hatchRight.grid(row=3, column=0)

startLeft = IntVar()
cargoLeft = Radiobutton(preMatch, text = 'Cargo Left', value=1, var=startLeft)
cargoLeft.grid(row=4, column=1)
hatchLeft = Radiobutton(preMatch, text='Hatch Left', value=2, var=startLeft)
hatchLeft.grid(row=4, column=0, pady=20)

startPosLBL = Label(preMatch, text='Where Did they Start?')
startPosLBL.grid(column=0, row=1, pady=23)
startPos = ttk.Combobox(preMatch)
startPos['values']= ("Level 1 Mid", "Level 1 Left", "Level 1 right", "Level 2 Left", "Level 2 Right")
startPos.current(0)
startPos.grid(column= 1, row= 1, columnspan= 3)
startPos.config(width= 28)

SSCargoHatch_Var = IntVar()
def SSCargoHatchP1():
    global SSCargoHatch_Var
    SSCargoHatch_Var.set(SSCargoHatch_Var.get() + 1)

def SSCargoHatchM1():
    if SSCargoHatch_Var.get() > 0:
       SSCargoHatch_Var.set(SSCargoHatch_Var.get() - 1) 
       
    

SSCargoHatch = Label(sandstorm, text=SSCargoHatch_Var.get(), textvariable = SSCargoHatch_Var)
SSCargoHatchP = Button(sandstorm, text='+', command=SSCargoHatchP1, bg='green4')
SSCargoHatchM = Button(sandstorm, text='-', command=SSCargoHatchM1, bg='red4')
SSCargoHatch.grid(column=2, row=1, pady=20)
SSCargoHatchP.grid(column=3, row=1)
SSCargoHatchM.grid(column=1, row=1)
SSCargoHatchlbl = Label(sandstorm, text = "Cargo Ship Hatch")
SSCargoHatchlbl.grid(column=0, row=1)

SSCargoCargo_Var = IntVar()
def SSCargoCargoP1():
    global SSCargoCargo_Var
    SSCargoCargo_Var.set(SSCargoCargo_Var.get() + 1)

def SSCargoCargoM1():
    if SSCargoCargo_Var.get() > 0:
       SSCargoCargo_Var.set(SSCargoCargo_Var.get() - 1) 
       
    

SSCargoCargo = Label(sandstorm, text=SSCargoCargo_Var.get(), textvariable = SSCargoCargo_Var)
SSCargoCargoP = Button(sandstorm, text='+', command=SSCargoCargoP1, bg='green4')
SSCargoCargoM = Button(sandstorm, text='-', command=SSCargoCargoM1, bg='red4')
SSCargoCargo.grid(column=6, row=1)
SSCargoCargoP.grid(column=7, row=1)
SSCargoCargoM.grid(column=5, row=1)
SSCargoCargolbl = Label(sandstorm, text = "Cargo Ship Cargo")
SSCargoCargolbl.grid(column=4, row=1)


SSCargoSSHRocketHatch_Var = IntVar()
def SSCargoSSHRocketHatchP1():
    global SSCargoSSHRocketHatch_Var
    SSCargoSSHRocketHatch_Var.set(SSCargoSSHRocketHatch_Var.get() + 1)

def SSCargoSSHRocketHatchM1():
    if SSCargoSSHRocketHatch_Var.get() > 0:
       SSCargoSSHRocketHatch_Var.set(SSCargoSSHRocketHatch_Var.get() - 1) 
       
    

SSCargoSSHRocketHatch = Label(sandstorm, text=SSCargoSSHRocketHatch_Var.get(), textvariable = SSCargoSSHRocketHatch_Var)
SSCargoSSHRocketHatchP = Button(sandstorm, text='+', command=SSCargoSSHRocketHatchP1, bg='green4')
SSCargoSSHRocketHatchM = Button(sandstorm, text='-', command=SSCargoSSHRocketHatchM1, bg='red4')
SSCargoSSHRocketHatch.grid(column=2, row=2, pady=20)
SSCargoSSHRocketHatchP.grid(column=3, row=2)
SSCargoSSHRocketHatchM.grid(column=1, row=2)
SSCargoSSHRocketHatchlbl = Label(sandstorm, text = "High Rocket Hatch")
SSCargoSSHRocketHatchlbl.grid(column=0, row=2)

SSCargoSSMRocketHatch_Var = IntVar()
def SSCargoSSMRocketHatchP1():
    global SSCargoSSMRocketHatch_Var
    SSCargoSSMRocketHatch_Var.set(SSCargoSSMRocketHatch_Var.get() + 1)

def SSCargoSSMRocketHatchM1():
    if SSCargoSSMRocketHatch_Var.get() > 0:
       SSCargoSSMRocketHatch_Var.set(SSCargoSSMRocketHatch_Var.get() - 1) 
       
    

SSCargoSSMRocketHatch = Label(sandstorm, text=SSCargoSSMRocketHatch_Var.get(), textvariable = SSCargoSSMRocketHatch_Var)
SSCargoSSMRocketHatchP = Button(sandstorm, text='+', command=SSCargoSSMRocketHatchP1, bg='green4')
SSCargoSSMRocketHatchM = Button(sandstorm, text='-', command=SSCargoSSMRocketHatchM1, bg='red4')
SSCargoSSMRocketHatch.grid(column=2, row=3, pady=20)
SSCargoSSMRocketHatchP.grid(column=3, row=3)
SSCargoSSMRocketHatchM.grid(column=1, row=3)
SSCargoSSMRocketHatchlbl = Label(sandstorm, text = "Med Rocket Hatch")
SSCargoSSMRocketHatchlbl.grid(column=0, row=3)

SSCargoSSLRocketHatch_Var = IntVar()
def SSCargoSSLRocketHatchP1():
    global SSCargoSSLRocketHatch_Var
    SSCargoSSLRocketHatch_Var.set(SSCargoSSLRocketHatch_Var.get() + 1)

def SSCargoSSLRocketHatchM1():
    if SSCargoSSLRocketHatch_Var.get() > 0:
       SSCargoSSLRocketHatch_Var.set(SSCargoSSLRocketHatch_Var.get() - 1) 
       
    

SSCargoSSLRocketHatch = Label(sandstorm, text=SSCargoSSLRocketHatch_Var.get(), textvariable = SSCargoSSLRocketHatch_Var)
SSCargoSSLRocketHatchP = Button(sandstorm, text='+', command=SSCargoSSLRocketHatchP1, bg='green4')
SSCargoSSLRocketHatchM = Button(sandstorm, text='-', command=SSCargoSSLRocketHatchM1, bg='red4')
SSCargoSSLRocketHatch.grid(column=2, row=4, pady=20)
SSCargoSSLRocketHatchP.grid(column=3, row=4)
SSCargoSSLRocketHatchM.grid(column=1, row=4)
SSCargoSSLRocketHatchlbl = Label(sandstorm, text = "Low Rocket Hatch")
SSCargoSSLRocketHatchlbl.grid(column=0, row=4)

SSCargoSSLRocketCargo_Var = IntVar()
def SSCargoSSLRocketCargoP1():
    global SSCargoSSLRocketCargo_Var
    SSCargoSSLRocketCargo_Var.set(SSCargoSSLRocketCargo_Var.get() + 1)

def SSCargoSSLRocketCargoM1():
    if SSCargoSSLRocketCargo_Var.get() > 0:
       SSCargoSSLRocketCargo_Var.set(SSCargoSSLRocketCargo_Var.get() - 1) 
       
    

SSCargoSSLRocketCargo = Label(sandstorm, text=SSCargoSSLRocketCargo_Var.get(), textvariable = SSCargoSSLRocketCargo_Var)
SSCargoSSLRocketCargoP = Button(sandstorm, text='+', command=SSCargoSSLRocketCargoP1, bg='green4')
SSCargoSSLRocketCargoM = Button(sandstorm, text='-', command=SSCargoSSLRocketCargoM1, bg='red4')
SSCargoSSLRocketCargo.grid(column=6, row=4)
SSCargoSSLRocketCargoP.grid(column=7, row=4)
SSCargoSSLRocketCargoM.grid(column=5, row=4)
SSCargoSSLRocketCargolbl = Label(sandstorm, text = "Low Rocket Cargo")
SSCargoSSLRocketCargolbl.grid(column=4, row=4, ipadx=100)

SSCargoSSMRocketCargo_Var = IntVar()
def SSCargoSSMRocketCargoP1():
    global SSCargoSSMRocketCargo_Var
    SSCargoSSMRocketCargo_Var.set(SSCargoSSMRocketCargo_Var.get() + 1)

def SSCargoSSMRocketCargoM1():
    if SSCargoSSMRocketCargo_Var.get() > 0:
       SSCargoSSMRocketCargo_Var.set(SSCargoSSMRocketCargo_Var.get() - 1) 
       
    

SSCargoSSMRocketCargo = Label(sandstorm, text=SSCargoSSMRocketCargo_Var.get(), textvariable = SSCargoSSMRocketCargo_Var)
SSCargoSSMRocketCargoP = Button(sandstorm, text='+', command=SSCargoSSMRocketCargoP1, bg='green4')
SSCargoSSMRocketCargoM = Button(sandstorm, text='-', command=SSCargoSSMRocketCargoM1, bg='red4')
SSCargoSSMRocketCargo.grid(column=6, row=3)
SSCargoSSMRocketCargoP.grid(column=7, row=3)
SSCargoSSMRocketCargoM.grid(column=5, row=3)
SSCargoSSMRocketCargolbl = Label(sandstorm, text = "Med Rocket Cargo")
SSCargoSSMRocketCargolbl.grid(column=4, row=3)

SSCargoSSHRocketCargo_Var = IntVar()
def SSCargoSSHRocketCargoP1():
    global SSCargoSSHRocketCargo_Var
    SSCargoSSHRocketCargo_Var.set(SSCargoSSHRocketCargo_Var.get() + 1)

def SSCargoSSHRocketCargoM1():
    if SSCargoSSHRocketCargo_Var.get() > 0:
       SSCargoSSHRocketCargo_Var.set(SSCargoSSHRocketCargo_Var.get() - 1) 
       
    

SSCargoSSHRocketCargo = Label(sandstorm, text=SSCargoSSHRocketCargo_Var.get(), textvariable = SSCargoSSHRocketCargo_Var)
SSCargoSSHRocketCargoP = Button(sandstorm, text='+', command=SSCargoSSHRocketCargoP1, bg='green4')
SSCargoSSHRocketCargoM = Button(sandstorm, text='-', command=SSCargoSSHRocketCargoM1, bg='red4')
SSCargoSSHRocketCargo.grid(column=6, row=2)
SSCargoSSHRocketCargoP.grid(column=7, row=2)
SSCargoSSHRocketCargoM.grid(column=5, row=2)
SSCargoSSHRocketCargolbl = Label(sandstorm, text = "Med Rocket Cargo")
SSCargoSSHRocketCargolbl.grid(column=4, row=2)


spacingLBL = Label(tele, text=' ').grid(row=0, column=4, padx=80)
TeleCargoHRocketCargo_Var = IntVar()
def TeleCargoHRocketCargoP1():
    global TeleCargoHRocketCargo_Var
    TeleCargoHRocketCargo_Var.set(TeleCargoHRocketCargo_Var.get() + 1)

def TeleCargoHRocketCargoM1():
    if TeleCargoHRocketCargo_Var.get() > 0:
       TeleCargoHRocketCargo_Var.set(TeleCargoHRocketCargo_Var.get() - 1) 
       
    

TeleCargoHRocketCargo = Label(tele, text=TeleCargoHRocketCargo_Var.get(), textvariable = TeleCargoHRocketCargo_Var)
TeleCargoHRocketCargoP = Button(tele, text='+', command=TeleCargoHRocketCargoP1, bg='green4')
TeleCargoHRocketCargoM = Button(tele, text='-', command=TeleCargoHRocketCargoM1, bg='red4')
TeleCargoHRocketCargo.grid(column=7, row=1)
TeleCargoHRocketCargoP.grid(column=8, row=1)
TeleCargoHRocketCargoM.grid(column=6, row=1)
TeleCargoHRocketCargolbl = Label(tele, text = "High Rocket Cargo")
TeleCargoHRocketCargolbl.grid(column=5, row=1, pady=15)

TeleCargoMRocketCargo_Var = IntVar()
def TeleCargoMRocketCargoP1():
    global TeleCargoMRocketCargo_Var
    TeleCargoMRocketCargo_Var.set(TeleCargoMRocketCargo_Var.get() + 1)

def TeleCargoMRocketCargoM1():
    if TeleCargoMRocketCargo_Var.get() > 0:
       TeleCargoMRocketCargo_Var.set(TeleCargoMRocketCargo_Var.get() - 1) 
       
    

TeleCargoMRocketCargo = Label(tele, text=TeleCargoMRocketCargo_Var.get(), textvariable = TeleCargoMRocketCargo_Var)
TeleCargoMRocketCargoP = Button(tele, text='+', command=TeleCargoMRocketCargoP1, bg='green4')
TeleCargoMRocketCargoM = Button(tele, text='-', command=TeleCargoMRocketCargoM1, bg='red4')
TeleCargoMRocketCargo.grid(column=7, row=2)
TeleCargoMRocketCargoP.grid(column=8, row=2)
TeleCargoMRocketCargoM.grid(column=6, row=2)
TeleCargoMRocketCargolbl = Label(tele, text = "Med Rocket Cargo")
TeleCargoMRocketCargolbl.grid(column=5, row=2, pady=15)

TeleCargoLRocketCargo_Var = IntVar()
def TeleCargoLRocketCargoP1():
    global TeleCargoLRocketCargo_Var
    TeleCargoLRocketCargo_Var.set(TeleCargoLRocketCargo_Var.get() + 1)

def TeleCargoLRocketCargoL1():
    if TeleCargoLRocketCargo_Var.get() > 0:
       TeleCargoLRocketCargo_Var.set(TeleCargoLRocketCargo_Var.get() - 1) 
       
    

TeleCargoLRocketCargo = Label(tele, text=TeleCargoLRocketCargo_Var.get(), textvariable = TeleCargoLRocketCargo_Var)
TeleCargoLRocketCargoP = Button(tele, text='+', command=TeleCargoLRocketCargoP1, bg='green4')
TeleCargoLRocketCargoL = Button(tele, text='-', command=TeleCargoLRocketCargoL1, bg='red4')
TeleCargoLRocketCargo.grid(column=7, row=3)
TeleCargoLRocketCargoP.grid(column=8, row=3)
TeleCargoLRocketCargoL.grid(column=6, row=3)
TeleCargoLRocketCargolbl = Label(tele, text = "Low Rocket Cargo")
TeleCargoLRocketCargolbl.grid(column=5, row=3, pady=15)


TeleHatchHRocketHatch_Var = IntVar()
def TeleHatchHRocketHatchP1():
    global TeleHatchHRocketHatch_Var
    TeleHatchHRocketHatch_Var.set(TeleHatchHRocketHatch_Var.get() + 1)

def TeleHatchHRocketHatchM1():
    if TeleHatchHRocketHatch_Var.get() > 0:
       TeleHatchHRocketHatch_Var.set(TeleHatchHRocketHatch_Var.get() - 1) 
       
    

TeleHatchHRocketHatch = Label(tele, text=TeleHatchHRocketHatch_Var.get(), textvariable = TeleHatchHRocketHatch_Var)
TeleHatchHRocketHatchP = Button(tele, text='+', command=TeleHatchHRocketHatchP1, bg='green4')
TeleHatchHRocketHatchM = Button(tele, text='-', command=TeleHatchHRocketHatchM1, bg='red4')
TeleHatchHRocketHatch.grid(column=2, row=1)
TeleHatchHRocketHatchP.grid(column=3, row=1)
TeleHatchHRocketHatchM.grid(column=1, row=1)
TeleHatchHRocketHatchlbl = Label(tele, text = "High Rocket Hatch")
TeleHatchHRocketHatchlbl.grid(column=0, row=1)

TeleHatchMRocketHatch_Var = IntVar()
def TeleHatchMRocketHatchP1():
    global TeleHatchMRocketHatch_Var
    TeleHatchMRocketHatch_Var.set(TeleHatchMRocketHatch_Var.get() + 1)

def TeleHatchMRocketHatchM1():
    if TeleHatchMRocketHatch_Var.get() > 0:
       TeleHatchMRocketHatch_Var.set(TeleHatchMRocketHatch_Var.get() - 1) 
       
    

TeleHatchMRocketHatch = Label(tele, text=TeleHatchMRocketHatch_Var.get(), textvariable = TeleHatchMRocketHatch_Var)
TeleHatchMRocketHatchP = Button(tele, text='+', command=TeleHatchMRocketHatchP1, bg='green4')
TeleHatchMRocketHatchM = Button(tele, text='-', command=TeleHatchMRocketHatchM1, bg='red4')
TeleHatchMRocketHatch.grid(column=2, row=2)
TeleHatchMRocketHatchP.grid(column=3, row=2)
TeleHatchMRocketHatchM.grid(column=1, row=2)
TeleHatchMRocketHatchlbl = Label(tele, text = "Med Rocket Hatch")
TeleHatchMRocketHatchlbl.grid(column=0, row=2)

TeleHatchLRocketHatch_Var = IntVar()
def TeleHatchLRocketHatchP1():
    global TeleHatchLRocketHatch_Var
    TeleHatchLRocketHatch_Var.set(TeleHatchLRocketHatch_Var.get() + 1)

def TeleHatchLRocketHatchL1():
    if TeleHatchLRocketHatch_Var.get() > 0:
       TeleHatchLRocketHatch_Var.set(TeleHatchLRocketHatch_Var.get() - 1) 
       
    

TeleHatchLRocketHatch = Label(tele, text=TeleHatchLRocketHatch_Var.get(), textvariable = TeleHatchLRocketHatch_Var)
TeleHatchLRocketHatchP = Button(tele, text='+', command=TeleHatchLRocketHatchP1, bg='green4')
TeleHatchLRocketHatchL = Button(tele, text='-', command=TeleHatchLRocketHatchL1, bg='red4')
TeleHatchLRocketHatch.grid(column=2, row=3)
TeleHatchLRocketHatchP.grid(column=3, row=3)
TeleHatchLRocketHatchL.grid(column=1, row=3)
TeleHatchLRocketHatchlbl = Label(tele, text = "Low Rocket Hatch")
TeleHatchLRocketHatchlbl.grid(column=0, row=3)

teleCargoHatch_Var = IntVar()
def teleCargoHatchP1():
    global teleCargoHatch_Var
    teleCargoHatch_Var.set(teleCargoHatch_Var.get() + 1)

def teleCargoHatchM1():
    if teleCargoHatch_Var.get() > 0:
       teleCargoHatch_Var.set(teleCargoHatch_Var.get() - 1) 
       
    

teleCargoHatch = Label(tele, text=teleCargoHatch_Var.get(), textvariable = teleCargoHatch_Var)
teleCargoHatchP = Button(tele, text='+', command=teleCargoHatchP1, bg='green4')
teleCargoHatchM = Button(tele, text='-', command=teleCargoHatchM1, bg='red4')
teleCargoHatch.grid(column=2, row=0)
teleCargoHatchP.grid(column=3, row=0)
teleCargoHatchM.grid(column=1, row=0)
teleCargoHatchlbl = Label(tele, text = "Cargo Ship Hatch")
teleCargoHatchlbl.grid(column=0, row=0)

teleCargoCargo_Var = IntVar()
def teleCargoCargoP1():
    global teleCargoCargo_Var
    teleCargoCargo_Var.set(teleCargoCargo_Var.get() + 1)

def teleCargoCargoM1():
    if teleCargoCargo_Var.get() > 0:
       teleCargoCargo_Var.set(teleCargoCargo_Var.get() - 1) 
       
    

teleCargoCargo = Label(tele, text=teleCargoCargo_Var.get(), textvariable = teleCargoCargo_Var)
teleCargoCargoP = Button(tele, text='+', command=teleCargoCargoP1, bg='green4')
teleCargoCargoM = Button(tele, text='-', command=teleCargoCargoM1, bg='red4')
teleCargoCargo.grid(column=7, row=0)
teleCargoCargoP.grid(column=8, row=0)
teleCargoCargoM.grid(column=6, row=0)
teleCargoCargolbl = Label(tele, text = "Cargo Ship Cargo")
teleCargoCargolbl.grid(column=5, row=0, pady=15)

teledropCargo_Var = IntVar()
def teledropCargoP1():
    global teledropCargo_Var
    teledropCargo_Var.set(teledropCargo_Var.get() + 1)

def teledropCargoM1():
    if teledropCargo_Var.get() > 0:
       teledropCargo_Var.set(teledropCargo_Var.get() - 1) 
       
    

teledropCargo = Label(tele, text=teledropCargo_Var.get(), textvariable = teledropCargo_Var)
teledropCargoP = Button(tele, text='+', command=teledropCargoP1, bg='green4')
teledropCargoM = Button(tele, text='-', command=teledropCargoM1, bg='red4')
teledropCargo.grid(column=7, row=4)
teledropCargoP.grid(column=8, row=4)
teledropCargoM.grid(column=6, row=4)
teledropCargolbl = Label(tele, text = "Dropped Cargo")
teledropCargolbl.grid(column=5, row=4)

teledropHatch_Var = IntVar()
def teledropHatchP1():
    global teledropHatch_Var
    teledropHatch_Var.set(teledropHatch_Var.get() + 1)

def teledropHatchM1():
    if teledropHatch_Var.get() > 0:
       teledropHatch_Var.set(teledropHatch_Var.get() - 1) 
       
    

teledropHatch = Label(tele, text=teledropHatch_Var.get(), textvariable = teledropHatch_Var)
teledropHatchP = Button(tele, text='+', command=teledropHatchP1, bg='green4')
teledropHatchM = Button(tele, text='-', command=teledropHatchM1, bg='red4')
teledropHatch.grid(column=2, row=4)
teledropHatchP.grid(column=3, row=4)
teledropHatchM.grid(column=1, row=4)
teledropHatchlbl = Label(tele, text = "Dropped Hatch")
teledropHatchlbl.grid(column=0, row=4, pady=15)

foul_Var = IntVar()
def foulP1():
    global foul_Var
    foul_Var.set(foul_Var.get() + 1)

def foulM1():
    if foul_Var.get() > 0:
       foul_Var.set(foul_Var.get() - 1) 
       
    

foul = Label(tele, text=foul_Var.get(), textvariable = foul_Var)
foulP = Button(tele, text='+', command=foulP1, bg='green4')
foulM = Button(tele, text='-', command=foulM1, bg='red4')
foul.grid(column=2, row=5)
foulP.grid(column=3, row=5)
foulM.grid(column=1, row=5)
foullbl = Label(tele, text = "Foul")
foullbl.grid(column=0, row=5, pady=15)

techFoul_Var = IntVar()
def techFoulP1():
    global techFoul_Var
    techFoul_Var.set(techFoul_Var.get() + 1)

def techFoulM1():
    if techFoul_Var.get() > 0:
       techFoul_Var.set(techFoul_Var.get() - 1) 
       
    

techFoul = Label(tele, text=techFoul_Var.get(), textvariable = techFoul_Var)
techFoulP = Button(tele, text='+', command=techFoulP1, bg='green4')
techFoulM = Button(tele, text='-', command=techFoulM1, bg='red4')
techFoul.grid(column=7, row=5)
techFoulP.grid(column=8, row=5)
techFoulM.grid(column=6, row=5)
techFoullbl = Label(tele, text = "Tech Foul")
techFoullbl.grid(column=5, row=5)

name = Entry(preMatch, width= 30)
name.bind('<Button-1>',popup_keyboard)
name.grid(column=1, row=0)
nameLBL = Label(preMatch, text = 'Name:')
nameLBL.grid(column=0, row=0,ipady=17)

comments= Text(postMatch, width=70, height=4)
comments.bind('<Button-1>', popup_keyboard)
comments.grid(column=0, row=4, columnspan=2, padx=30)
commentsLBL = Label(postMatch, text='Comments:')
commentsLBL.grid(column=0, row=3, pady=15, columnspan=3)
commentSpacingLBL = Label(postMatch, text=' ').grid(column=2, row=0, padx=10)
    
teamnum = ttk.Entry(preMatch, width=10)
teamnum.bind('<Button-1>', popup_keyboard)
teamnum.grid(column=3, row=0)
teamnumLBL = Label(preMatch, text='  Team# you are with:')
teamnumLBL.grid(row=0, column=2)

def send():
    sendMSG = messagebox.askokcancel('Are you sure?', 'If you are ready to send click ok. If you are not ready click cancel, and click send again when you are ready.')
    print(badData_State.get())
    print(sendMSG)
    if (sendMSG is True) & (badData_State.get() is False):
        print('calling Reinitscreen')
        reinitscreen()
        
        
    if (badData_State.get() is True) & (sendMSG is True):
        reinitscreen()

send_State = BooleanVar(False)
sendBTN = Button(postMatch, text='send', command=send)
sendBTN.grid(row=5, column=1, ipadx=100)
#define button effects



    #finish
#    dp start
#if len(sys.argv) > 1:
#    position = sys.argv[1]
#else:
#    position='R1'
#match_no='2'
#getNextMatch()

teamno = 1986
#a thing
window.mainloop()