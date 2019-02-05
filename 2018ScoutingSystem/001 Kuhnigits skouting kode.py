'need to add all the counters'
'need to add data base'
'need to format everything'
'need to keep the counters from going negative'
'need to add databese'

# imports
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import os
#import match_dbconn

#descibing the pi
window = Tk() 
window.geometry('800x480')

#font for the labels
style = ttk.Style()
style.theme_settings("default",{"TNotebook.Tab":{"configure":{"padding":[20,20]}}})
labelfont = font.Font(family= "times", size= 20)
window.option_add("*Font", labelfont)
labelfont = ('times', 15)
labelfont2 = ('times', 5)

###some defines
#def printVar():
#    print('Initals')
#    print(Init.get())
#    print(' ')
#    print('Extended bar')
#    print(EXB_state.get())
#    print(' ')
#    print('Deployed single ramp')
#    print(DPR_state.get())
#    print(' ')
#    print('Deployed Double Ramp')
#    print(DPR2_state.get())
#    print(' ')
#    print('Parked')
#    print(PRK_state.get())
#    print(' ')
#    print('Deadbot')
#    print(DBT_state.get())
#    print(' ')
#    print('Recovered deadbot')
#    print(RDB_state.get())
#    print(' ')
#    print('Tipped')
#    print(TIP_state.get())
#    print(' ')
#    print('Recovered Tip')
#    print(RTP_state.get())
#    print(' ')
#    print('Cross line attempt')
#    print(CLT_state.get())
#    print(' ')
#    print('Cross line success')
#    print(CLS_state.get())
#    print(' ')
#    print('Correct Switch attempt')
#    print(CSA_state.get())
#    print(' ')
#    print('Wrong Switch Attempt')
#    print(WSA_state.get())
#    print(' ')
#    print('Correct Scale Attempt')
#    print(ACS_state.get())
#    print(' ')
#    print('Wrong Scale Attempt')
#    print(WCS_state.get())
#    print(' ')
#    print('Ended Auto With a cube')
#    print(EAC_state.get())
#    print(' ')
#    print('Climb')
#    print(combo.get())
#    print(' ')
#    print('Pickup Box')
#    print(combo2.get())
#    print(' ')
#    print('PLace Box')
#    print(combo3.get())
#    print(' ')
#    print('Cards')
#    print(selected.get())
#    print(' ')
#    print('Defense')
#    print(combo4.get())
#    print(' ')
#    print('Correct Switch Success Auto')
#    print(CSS_Var.get())
#    print(' ')
#    print('Wrong Switch Success Auto')
#    print(WSS_Var.get())
#    print(' ')
#    print('Correct Scale Success Auto')
#    print(CSCS_Var.get())
#    print(' ')
#    print('Wrong Scale Success Auto')
#    print(WSCS_Var.get())
#    print(' ')
#    print('Own Switch Sucess Teleop')
#    print(OSS_Var.get())
#    print(' ')
#    print('Opposing Switch Teleop')
#    print(OPSS_Var.get())
#    print(' ')
#    print('Scale Teleop')
#    print(SS_Var.get())
#    print(' ')
#    print('Vault')
#    print(VLT_Var.get())
#    print(' ')
#    print('Dropped Blocks')
#    print(DB_Var.get())
#    print(' ')
#    print('Foul')
#    print(FOUL_state.get())
#    print(' ')
#    print('Tech Foul')
#    print(TFL_state.get())
#    print(' ')
#    print('Comments')
#    print(txt.get())
#    
#def getTeam():
#    team_no = match_dbconn.getMatchInfo(match_no,position)
#    title_str = "MATCH NO: %s TEAM NO: %s  Postion %s" %(match_no,team_no,position)
#    window.title(title_str)
#    print(team_no)
#    global teamno
#    teamno = team_no
#    
#def getNextMatch():
#    new_match_no = match_dbconn.getNextMatch();
#    print('new match %s',new_match_no)
#    global match_no
#    global position
#    print('current match %s',match_no)
#    if new_match_no != match_no:
#        print('reinitialize screens')
#        match_no = new_match_no
#        getTeam()
#        btn.state = ENABLED
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
#                               CLT_state.get(), #AutoCrossLineTry
#                               CLS_state.get(), #AutoCrossLineSuccess
#                               CSA_state.get(), #AutoBoxToSwitchTry
#                               CSS_Var.get(),   #AutoBoxToSwitchCount
#                               WSA_state.get(), #AutoBoxToWrongSwitchTry
#                               WSS_Var.get(),   #SutoBoxToWrongSwitchCount
#                               ACS_state.get(), #AutoBoxToScaleTry
#                               CSCS_Var.get(),  #AutoBoxToScaleCount
#                               WCS_state.get(), #AutoBoxToWrongScaleTry
#                               WSCS_Var.get(),  #AutoBoxToWrongScaleCount
#                               EAC_state.get(), #autoEndWithNewCube
#                               OSS_Var.get(),   #teleBoxToSwitchCount
#                               SS_Var.get(),    #teleBoxToScaleCount
#                               OPSS_Var.get(),  #teleBoxToOpponentSwitchCount
#                               VLT_Var.get(),   #teleBoxToExchangeCount
#                               DB_Var.get(),    #teleBoxDroppedBoxCount
#                               combo4.get(),    #teleDefenseType
#                               TIP_state.get(), #tippedBot
#                               DBT_state.get(), #deadBot
#                               RTP_state.get(), #recoveredTippedBot
#                               RDB_state.get(), #recoveredDeadBot
#                               FOUL_state.get(),#penaltyStandardFoul
#                               TFL_state.get(), #penaltyTechnicalFoul
#                               penalty_yellow,  #penaltyYelloCard
#                               penalty_red,     #penaltyRedCard
#                               PRK_state.get(), #endParked
#                               combo.get(),     #endClimbedType
#                               DPR_state.get(),  #endClimbedRampSingle
#                               DPR2_state.get(), #endClimbedRampDouble
#                               EXB_state.get(), #endClimbedExtendBar
#                               combo2.get(),    #endCubeAttainment
#                               combo3.get(),    #endScoringAbility
#                               txt.get())    
#def reinitScreen():
#    Init.delete(0,END)
#    txt.delete(0,END)
#    EXB_state.set(0)
#    DPR_state.set(0)
#    DPR2_state.set(0)
#    PRK_state.set(0)
#    TIP_state.set(0)
#    RTP_state.set(0)
#    CLT_state.set(0)
#    CLS_state.set(0)
#    CSA_state.set(0)
#    WSA_state.set(0)
#    ACS_state.set(0)
#    WCS_state.set(0)
#    EAC_state.set(0)
#    combo.set('Didn\'t Try')
#    combo2.set('Didn\'t use cubes')
#    combo3.set('Can\'t/didn\'t use cubes')
#    combo4.set("Didn't")
#    CSS_Var.set(0)
#    WSS_Var.set(0)
#    WSCS_Var.set(0)
#    OSS_Var.set(0)
#    OPSS_Var.set(0)
#    SS_Var.set(0)
#    VLT_Var.set(0)
#    DB_Var.set(0)
#    selected.set(0)
#    FOUL_state.set(0)
#    TFL_state.set(0)

#notebook stuff
tab_control = ttk.Notebook(window)
tab5 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab5, text='Pre-Match')
tab_control.add(tab1, text='Auto')
tab_control.add(tab2, text='Tele')
tab_control.add(tab3, text='Climb')
tab_control.add(tab4, text='Post-Match')
tab_control.pack(expand=1, fill='both')

#keyboard
def popup_keyboard(event):
    os.popen('matchbox-keyboard','r',4096)
    
#initials
Init = ttk.Entry(tab5, width= 3)
Init.bind('<Button-1>',popup_keyboard)
Init.grid(column=2, row=0)
LBL16 = Label(tab5, text = 'Initials')
LBL16.grid(column=1, row=0)



#Extended bar
EXB_state = IntVar()
EXB_state.set(0)
EXB = Checkbutton(tab3, text='Extended Bar?', var=EXB_state)
EXB.grid(column=0, row=1, ipady= 25)
EXB.config(anchor= NE)

#Deployed single ramp
DPR_state = BooleanVar(False)
DPR = Checkbutton(tab3, text='Deployed Single Ramp?', var=DPR_state)
DPR.grid(column=0, row=2, ipady= 25)

#deployed double ramp
DPR2_state = BooleanVar()
DPR2_state.set(False)
DPR2 = Checkbutton(tab3, text='Deployed Double Ramp? ', var=DPR2_state)
DPR2.grid(column=1, row=2)

#parked?
PRK_state = BooleanVar()
PRK_state.set(False)
PRK = Checkbutton(tab3, text='Parked?', var=PRK_state)
PRK.grid(column=0, row=3, ipady= 25)

#deadbot
DBT_state = BooleanVar()
DBT_state.set(False)
DBT = Checkbutton(tab4, text='Deadbot?', var=DBT_state)
DBT.grid(column=0, row=2, ipady= 10)

#recovered deadbot
RDB_state = BooleanVar()
RDB_state.set(False)
RDB = Checkbutton(tab4, text='Recovered?', var=RDB_state)
RDB.grid(column=1, row=2)

#tipped
TIP_state = BooleanVar()
TIP_state.set(False)
TIP = Checkbutton(tab4, text='Tipped? ', var=TIP_state)
TIP.grid(column=0, row=3, ipady= 10)

#recovered tipped bot
RTP_state = BooleanVar()
RTP_state.set(False)
RTP = Checkbutton(tab4, text='Recovered?', var=RTP_state)
RTP.grid(column=1, row=3)

#cross line attempt
CLT_state = BooleanVar()
CLT_state.set(False)
CLT = Checkbutton(tab1, text=('Cross Line Attempt'), var=CLT_state)
CLT.grid(column=0, row=0)

#cross line success
CLS_state = BooleanVar() 
CLS_state.set(False)
CLS = Checkbutton(tab1, text=('Cross line Success'), var=CLS_state )
CLS.grid(column=1, row=0, ipady=17)

#Correct Scale Auto
CSA_state = BooleanVar() 
CSA_state.set(False)
CSA = Checkbutton(tab1, text=('Correct Switch Attempt'), var=CSA_state)
CSA.grid(column=0, row=1, ipady=20)

# wrong scale attempt
WSA_state = BooleanVar() 
WSA_state.set(False)
WSA = Checkbutton(tab1, text=('Wrong Switch Attempt'), var=WSA_state)
WSA.grid(column=0, row=2)

#correct scale attempt
ACS_state = BooleanVar() 
ACS_state.set(False)
ACS = Checkbutton(tab1, text=('Correct Scale Attempt'), var=ACS_state)
ACS.grid(column=0, row=3, ipady=20)

#wrong switch attempt
WCS_state = BooleanVar() 
WCS_state.set(False)
WCS = Checkbutton(tab1, text=('Wrong Scale Attempt'), var=WCS_state)
WCS.grid(column=0, row=4)

#ended auto with a cube
EAC_state = BooleanVar() 
EAC_state.set(False)
EAC = Checkbutton(tab1, text=('Ended Auto with a New Cube'), var=EAC_state)
EAC.grid(column=0, row=5, ipady=15)

#climb combobox
combo = ttk.Combobox(tab3) 
combo['values']= ( "Didn't Try", "Center", "Side", "Used Ramp", "Failed", "Attempt") 
combo.current(0)
combo.grid(column= 1, row= 0)
combo.config(font=labelfont)

# cube pickup capability combobox
combo2 = ttk.Combobox(tab4)
combo2['values']= ("Didn't use cubes", "Only used cube they started with","Recived cubes from exchange/portal", "Picked up cubes from ground", "Picked up cubes from ground and recived cubes from portal/exchange")
combo2.current(0)
combo2.grid(column= 1, row= 4, columnspan= 2)
combo2.config(width= 50)
combo2.config(font=labelfont)

# cube placement capability combobox
combo3 = ttk.Combobox(tab4)
combo3['values']= ("Can score on high scale", "Can score on medium scale", "Can score on low scale", "Can score on switch", "Can score on exchange", "Can't/didn't use cubes")
combo3.current(5)
combo3.grid(column= 1, row= 5, columnspan= 2)
combo3.config(width= 50)
combo3.config(font=labelfont)

#comments label
lbl3 = Label(tab4, text='Comments')
#lbl3.config(font=labelfont)
lbl3.grid(column=0, row=7, ipady=10)

#Reminder label
lbl2 = Label(tab4, text='Remember to be gracious!')
#lbl2.config(font=labelfont)
lbl2.grid(column=1, row=6)

#how do they get cubes label
lbl4 = Label(tab4, text='How do they get cubes?')
#lbl4.config(font=labelfont)
lbl4.grid(column=0, row=4, ipady= 10)

#climb label
lbl = Label(tab3, text="Climb?")
#lbl.config(font=labelfont)
lbl.grid(column=0, row=0, ipady= 25)

lbl6 = Label(tab4, text='Pick the highest they did')
lbl6.grid(column=0, row=5, ipady= 10)

#card radio buttons
selected = IntVar()

rad1 = Radiobutton(tab4,text='Not Carded', value=0, variable=selected)
rad2 = Radiobutton(tab4,text='Yellow Card?', value=1, variable=selected)
rad3 = Radiobutton(tab4,text='Red Card?', value=2, variable=selected)
rad1.grid(column=0, row=1, ipady= 10)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)

#defense time estimate
deflbl = Label(tab2, text='Estimated time spent playing defense')
deflbl.grid(column=0, row=5, ipady= 20)
combo4 = ttk.Combobox(tab2)
combo4['values']= ("Didn't", "less than 30 secs", "30 secs to 1 minute", "more than 1 min")
combo4.current(0)
combo4.grid(column= 2, row= 5, columnspan= 3)
combo4.config(width= 25)

#correct switch success spindown
CSS_Var = IntVar()
def plus1(score):
    (score + 1)

def minus1(score):
    if score > 0:
       (score - 1) 
       
    

CSS = Label(tab1, text=CSS_Var.get(), textvariable = CSS_Var, bg="yellow")
CSSBP = Button(tab1, text='+', command=plus1(CSS_Var.get()), bg="blue")
CSSBM = Button(tab1, text='-', command=minus1(CSS_Var.get()),bg="red")
CSS.grid(column=3, row=1)
CSSBP.grid(column=4, row=1)
CSSBM.grid(column=2, row=1)
lbl7 = Label(tab1, text = "Correct Switch Successes")
lbl7.grid(column=1, row=1)

#wrong switch success spindown
WSS_Var = IntVar()
def WSSP1():
    global WSS_Var
    WSS_Var.set(WSS_Var.get() + 1)

def WSSM1():
    if WSS_Var.get() > 0:
       WSS_Var.set(WSS_Var.get() - 1)

WSS = Label(tab1, text=WSS_Var.get(), textvariable = WSS_Var)
WSSBP = Button(tab1, text='+', command=WSSP1)
WSSBM = Button(tab1, text='-', command=WSSM1)
WSS.grid(column=3, row=2, ipady=20)
WSSBM.grid(column=2, row=2)
WSSBP.grid(column=4, row=2)
lbl8 = Label(tab1, text = "Wrong Switch Successes")
lbl8.grid(column=1, row=2)

#correct scale success spindown
CSCS_Var = IntVar()
def CSCSP1():
    global CSCS_Var
    CSCS_Var.set(CSCS_Var.get() + 1)

def CSCSM1():
    if CSCS_Var.get() > 0:
       CSCS_Var.set(CSCS_Var.get() - 1)

CSCS = Label(tab1, text=CSCS_Var.get(), textvariable = CSCS_Var)
CSCSBP = Button(tab1, text='+', command=CSCSP1)
CSCSBM = Button(tab1, text='-', command=CSCSM1)
CSCS.grid(column=3, row=3, ipady=20)
CSCSBP.grid(column=4, row=3)
CSCSBM.grid(column=2, row=3)
lbl9 = Label(tab1, text = "Correct Scale Successes")
lbl9.grid(column=1, row=3)

#wrong scale success spindown
WSCS_Var = IntVar()
def WSCSP1():
    global WSCS_Var
    WSCS_Var.set(WSCS_Var.get() + 1)

def WSCSM1():
    if WSCS_Var.get() > 0:
       WSCS_Var.set(WSCS_Var.get() - 1)

WSCS = Label(tab1, text=WSCS_Var.get(), textvariable = WSCS_Var)
WSCSBP = Button(tab1, text='+', command=WSCSP1)
WSCSBM = Button(tab1, text='-', command=WSCSM1)
WSCS.grid(column=3, row=4, ipady=20)
WSCSBP.grid(column=4, row=4)
WSCSBM.grid(column=2, row=4)
lbl10 = Label(tab1, text = "Wrong Scale Successes")
lbl10.grid(column=1, row=4)

#own switch success spindown
OSS_Var = IntVar()
def OSSP1():
    global OSS_Var
    OSS_Var.set(OSS_Var.get() + 1)

def OSSM1():
    if OSS_Var.get() > 0:
       OSS_Var.set(OSS_Var.get() - 1)

OSS = Label(tab2, text=OSS_Var.get(), textvariable = OSS_Var)
OSSBP = Button(tab2, text='+', command=OSSP1)
OSSBM = Button(tab2, text='-', command=OSSM1)
OSS.grid(column=2, row=0, ipady= 20)
OSSBP.grid(column=3, row=0)
OSSBM.grid(column=1, row=0)
lbl11 = Label(tab2, text = "Cubes Delivered To Own Switch")
lbl11.grid(column=0, row=0)

#opposing switch success spindown
OPSS_Var = IntVar()
def OPSSP1():
    global OPSS_Var
    OPSS_Var.set(OPSS_Var.get() + 1)

def OPSSM1():
    if OPSS_Var.get() > 0:
       OPSS_Var.set(OPSS_Var.get() - 1)

OPSS = Label(tab2, text=OPSS_Var.get(), textvariable = OPSS_Var)
OPSSBP = Button(tab2, text='+', command=OPSSP1)
OPSSBM = Button(tab2, text='-', command=OPSSM1)
OPSS.grid(column=6, row=0, ipady= 20)
OPSSBP.grid(column=7, row=0)
OPSSBM.grid(column=5, row=0)
lbl12 = Label(tab2, text = "Cubes Delivered To Opposing Switch")
lbl12.grid(column=4, row=0)

#scale spindown
SS_Var = IntVar()
def SSP1():
    global SS_Var
    SS_Var.set(SS_Var.get() + 1)

def SSM1():
    if SS_Var.get() > 0:
       SS_Var.set(SS_Var.get() - 1)

SS = Label(tab2, text=SS_Var.get(), textvariable = SS_Var)
SSBP = Button(tab2, text='+', command=SSP1)
SSBM = Button(tab2, text='-', command=SSM1)
SS.grid(column=2, row=2, ipady= 20)
SSBP.grid(column=3, row=2)
SSBM.grid(column=1, row=2)
lbl13 = Label(tab2, text = "Cubes Delivered To Scale")
lbl13.grid(column=0, row=2)

#vault spindown
VLT_Var = IntVar()
def VLTP1():
    global OSS_Var
    VLT_Var.set(VLT_Var.get() + 1)

def VLTM1():
    if VLT_Var.get() > 0:
       VLT_Var.set(VLT_Var.get() - 1)

VLT = Label(tab2, text=VLT_Var.get(), textvariable = VLT_Var)
VLTBP = Button(tab2, text='+', command=VLTP1)
VLTBM = Button(tab2, text='-', command=VLTM1)
VLTBM.grid(column=5, row=2)
VLTBP.grid(column=7, row=2)
VLT.grid(column=6, row=2)
lbl14 = Label(tab2, text = "Cubes Delivered To Vault")
lbl14.grid(column=4, row=2)

#dropped blocks spindown
DB_Var = IntVar()
def DBP1():
    global DB_Var
    DB_Var.set(DB_Var.get() + 1)

def DBM1():
    if DB_Var.get() > 0:
       DB_Var.set(DB_Var.get() - 1)

DB = Label(tab2, text=DB_Var.get(), textvariable = DB_Var)
DBBP = Button(tab2, text='+', command=DBP1)
DBBM = Button(tab2, text='-', command=DBM1)
DB.grid(column=2, row=4, ipady= 20)
DBBP.grid(column=3, row=4)
DBBM.grid(column=1, row=4)
lbl15 = Label(tab2, text = "Dropped blocks")
lbl15.grid(column=0, row=4)

#foul
FOUL_state = BooleanVar() 
FOUL_state.set(False)
FOUL = Checkbutton(tab2, text=('Foul?'), var=FOUL_state)
FOUL.grid(column=0, row=6, ipady= 20)

#tech foul
TFL_state = BooleanVar() 
TFL = Checkbutton(tab2, text=('Tech Foul?'), var=TFL_state)
TFL.grid(column=4, row=6)

#send button
def clicked():
    messagebox.showinfo('Sent', 'Your scouting data was sent. Find your robot in the next round. Please remeber to always be gracious and professional at competions! Do NOT click this button again until the end of the next round. If you do you will be fed to the Killer Rabbot.')
    sendToDatabase()
    reinitScreen()
    btn.state = DISABLED
    
#send button    
btn = ttk.Button(tab4, text="Send", command=clicked)
btn.grid(column=3, row=8)

#comments box
txt = ttk.Entry(tab4, width= 25)
txt.bind('<Button-1>',popup_keyboard)
txt.grid(column=1, row=7)

#dp start
#if len(sys.argv) > 1:
#    position = sys.argv[1]
#else:
#    position='R1'
#match_no='2'
#getNextMatch()
#
#teamno = 1986
#a thing
window.mainloop()