#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:02:26 2018

@author: samuelcolombo
"""

from tkinter import *

class CounterClass:
    point = 0
    root = Tk()
    app = Frame(root)

    def __init__(self):
        self.root.title("Appetiser Page")
        self.root.geometry("1920x1080")

        self.app.grid()

        Label(self.app, text = "", width = 75, height = 20).grid(row = 1, column = 0, sticky = N)

        self.DisplayLabel = Label(self.app, text = self.point)
        self.DisplayLabel.grid(column = 2, row = 2, sticky = W)
        self.DisplayLabel.config(height = 10, width = 10 )

        self.Plus1Button = Button(self.app, text = "+", command=self.plus1, bg="green")
        self.Plus1Button.grid(column = 3, row = 2, sticky = W)
        self.Plus1Button.config(height = 10, width = 10 )

        self.Neg1Button = Button(self.app, text = "-", command=self.neg1, bg="green")
        self.Neg1Button.grid(column = 1, row = 2, sticky = W)
        self.Neg1Button.config(height = 10, width = 10 )

        self.root.mainloop()
    
        
   
    def plus1(self):
        if self.point < 58:
            self.point += 1
            self.DisplayLabel["text"]=str(self.point)

        
    def neg1(self):
        if self.point  > 0:
            self.point -= 1
            self.DisplayLabel["text"]=str(self.point)
    

if __name__ == "__main__":
    CounterClass()