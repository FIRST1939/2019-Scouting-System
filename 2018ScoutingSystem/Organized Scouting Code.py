# imports
from tkinter import * 
from tkinter.ttk import * 
from tkinter import ttk

#descibing the pi
window = Tk() 
window.title("2018 Scouting System")
window.geometry('800x480')

#font for the labels
style = ttk.Style()
style.theme_settings("default",{"TNotebook.Tab":{"configure":{"padding":[20,20]}}})
labelfont = ('times', 20)

#notebook stuff
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Auto')
tab_control.add(tab2, text='Tele')
tab_control.add(tab3, text='Climb')
tab_control.add(tab4, text='Post-Match')
tab_control.pack(expand=1, fill='both')

#Extended bar
EXB_state = BooleanVar()
EXB_state.set(False)
EXB = ttk.Checkbutton(tab3, text='Extended Bar?', var=DBT_state)
EXB.grid(column=0, row=1)

#Deployed single ramp
DPR_state = BooleanVar()
DPR_state.set(False)
DPR = ttk.Checkbutton(tab3, text='Deployed Single Ramp?', var=RDB_state)
DPR.grid(column=0, row=2)

#deployed double ramp
DPR2_state = BooleanVar()
DPR2_state.set(False)
DPR2 = ttk.Checkbutton(tab3, text='Deployed Double Ramp? ', var=TIP_state)
DPR2.grid(column=1, row=2)

#parked?
PRK_state = BooleanVar()
PRK_state.set(False)
PRK = ttk.Checkbutton(tab3, text='Parked?', var=RTP_state)
PRK.grid(column=0, row=3)

#deadbot
DBT_state = BooleanVar()
DBT_state.set(False)
DBT = ttk.Checkbutton(tab4, text='Deadbot?', var=DBT_state)
DBT.grid(column=0, row=2)

#recovered deadbot
RDB_state = BooleanVar()
RDB_state.set(False)
RDB = ttk.Checkbutton(tab4, text='Recovered?', var=RDB_state)
RDB.grid(column=1, row=2)

#tipped
TIP_state = BooleanVar()
TIP_state.set(False)
TIP = ttk.Checkbutton(tab4, text='Tipped? ', var=TIP_state)
TIP.grid(column=0, row=3)

#recovered tipped bot
RTP_state = BooleanVar()
RTP_state.set(False)
RTP = ttk.Checkbutton(tab4, text='Recovered?', var=RTP_state)
RTP.grid(column=1, row=3)

#cross line attempt
CLT_state = BooleanVar()
CLT_state.set(False)
CLT = ttk.Checkbutton(tab1, text=('Cross Line Attempt'), var=CLT_state)
CLT.grid(column=0, row=0)

#cross line success
CLS_state = BooleanVar() 
CLS_state.set(False)
CLS = ttk.Checkbutton(tab1, text=('Cross line Success'), var=CLS_state )
CLS.grid(column=1, row=0)

#Correct Scale Auto
CSA_state = BooleanVar() 
CSA_state.set(False)
CSA = ttk.Checkbutton(tab1, text=('Correct Switch Attempt'), var=CSA_state)
CSA.grid(column=0, row=1)

# wrong scale attempt
WSA_state = BooleanVar() 
WSA_state.set(False)
WSA = ttk.Checkbutton(tab1, text=('Wrong Switch Attempt'), var=WSA_state)
WSA.grid(column=0, row=2)

#correct scale attempt
ACS_state = BooleanVar() 
ACS_state.set(False)
ACS = ttk.Checkbutton(tab1, text=('Correct Scale Attempt'), var=ACS_state)
ACS.grid(column=0, row=3)

#wrong switch attempt
WCS_state = BooleanVar() 
WCS_state.set(False)
WCS = ttk.Checkbutton(tab1, text=('Wrong Scale Attempt'), var=WCS_state)
WCS.grid(column=0, row=4)

#ended auto with a cube
EAC_state = BooleanVar() 
EAC_state.set(False)
EAC = ttk.Checkbutton(tab1, text=('Ended Auto with a Cube'), var=EAC_state)
EAC.grid(column=0, row=5)

#climb combobox
combo = ttk.Combobox(tab3) 
combo['values']= ( "Didn't Try", "Center", "Side", "Used Ramp", "Failed") 
combo.current(0)
combo.grid(column=1, row=0)

# cube pickup capability combobox
combo2 = ttk.Combobox(tab4)
combo2['values']= ("Didn't use cubes", "recived cubes from exchange/portal", "picked up cubes from ground", "picked up cubes from ground, and recived cubes from portal/exchange")
combo2.current(0)
combo2.grid(column=1, row=5)

# cube placement capability combobox
combo3 = ttk.Combobox(tab4)
combo3['values']= ("Can score on high scale", "Can score on medium scale", "can score on low scale", "can score on switch", "can score on exchange", "can't/didn't use cubes")
combo3.current(5)

#comments label
lbl3 = ttk.Label(tab4, text='Comments')
lbl3.config(font=labelfont)
lbl3.grid(column=0, row=6)

#Reminder label
lbl2 = ttk.Label(tab4, text='Remember to be gracious!')
lbl2.config(font=labelfont)
lbl2.grid(column=1, row=4)

#how do they get cubes label
lbl4 = ttk.Label(tab4, text='How do they get cubes?')
lbl4.config(font=labelfont)
lbl4.grid(column=0, row=5)

#where can they score label
lbl5 = ttk.Label(tab4, text='Where can they score? Choose the one that is the highest.')
lbl5.config(font=labelfont)

#climb label
lbl = ttk.Label(tab3, text="Climb?")
lbl.config(font=labelfont)
lbl.grid(column=0, row=0)

#card radio buttons
rad1 = ttk.Radiobutton(tab4,text='Not Carded', value=1)
rad2 = ttk.Radiobutton(tab4,text='Yellow Card?', value=2)
rad3 = ttk.Radiobutton(tab4,text='Red Card?', value=3)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)

#send button
def clicked():
    ttk.messagebox.showinfo('Sent', 'Your scouting data was sent. Find your robot in the next round. Please remeber to always be gracious and professional at competions! Do NOT click this button again until the end of the next round. If you do you will be fed to the Killer Rabbot.')
    print(ttk.selected.get())

btn = ttk.Button(tab4, text="Send", command=clicked)
btn.grid(column=5, row=7)

window.mainloop()


