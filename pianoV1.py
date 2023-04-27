#Sammy Stollman
#TKinter piano V1
#Date Created: 5/30/2019
import winsound
from tkinter import *
#######
#Screen
#######
root = Tk()
root.title("Piano")
root.geometry("1000x500")
L=Label(text="Press a key to make a sound")
L.grid()

##########
#Functions
##########
def PlayC():
   winsound.PlaySound("C.wav", winsound.SND_ALIAS|winsound.SND_ASYNC) 
def PlayD():
   winsound.PlaySound("D.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def PlayE():
   winsound.PlaySound("E.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def PlayF():
   winsound.PlaySound("F.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def PlayG():
   winsound.PlaySound("G.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def PlayA():
   winsound.PlaySound("A.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def PlayB():
   winsound.PlaySound("B.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def PlayC2():
   winsound.PlaySound("C2.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
''' Each function plays the note and the SND_ASYNC allows a different
sound to be played before the first sound is finished.'''
########
#Buttons
########
ButtonC = Button(root, bg="white", height = 20, width = 10, command = PlayC)
ButtonD = Button(root, bg="white", height = 20, width = 10, command = PlayD)
ButtonE = Button(root, bg="white", height = 20, width = 10, command = PlayE)
ButtonF = Button(root, bg="white", height = 20, width = 10, command = PlayF)
ButtonG = Button(root, bg="white", height = 20, width = 10, command = PlayG)
ButtonA = Button(root, bg="white", height = 20, width = 10, command = PlayA)
ButtonB = Button(root, bg="white", height = 20, width = 10, command = PlayB)
ButtonC2 = Button(root, bg="white", height = 20, width = 10, command = PlayC2)
#ButtonCsharp = Button(root, bg="black", height = 15, width = 10)
#ButtonDsharp = Button(root, bg="black", height = 15, width = 10)
#ButtonDsharp1 = Button(root, bg="black", height = 15, width = 10)

#####
#List
#####
Buttons = [ButtonC, ButtonD, ButtonE, ButtonF, ButtonG, ButtonA, ButtonB, ButtonC2]
################
#Griding buttons
################
for x in range(8):
    Buttons[x].grid(row=1,column=x+2)
    '''Makes all of the 8 white buttons in a row next to each other'''
#ButtonDsharp.grid(row = 1,column = 1, columnspan = 2)
#ButtonCsharp.grid(row = 1,column = 2, columnspan = 2)

root.mainloop()
