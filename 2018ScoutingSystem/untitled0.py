from tkinter import *
window = Tk()
window.title("hi")
window.geometry('300x250')


    tab_control = ttk.Notebook(window)
preMatcth = ttk.Frame(tab_control)
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

crossHABLine_State = BooleanVar(False)
crossHABLine = Checkbutton(sandstorm, text='Cross HAB Line', var=crossHABLine_State)
crossHABLine.grid(row=0, column=0)

dangerousSSDriving_State = BooleanVar(False)
dangerousSSDriving = Checkbutton(sandstorm, text='Drove Dangerously during Sandstorm', var=dangerousSSDriving_State)  
dangerousSSDriving.grid(row=5, column =5)