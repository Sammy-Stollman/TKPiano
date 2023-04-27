#Sammy Stollman
#TKinter piano V1
#Date Created: 5/30/2019
#V2 Date: 6/3/2019
'''Version 2 adds prebuilt songs and melodies with functions. It also adds keyboard
input to play the piano.I will try to add chords, but I do not know how 
to play mutiple winsounds at the same time. I will add a menu in a future 
version to play songs, but for now it will just be on screen buttons'''
import time
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
def C(event=0):
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonC.config(state = ACTIVE, relief = SUNKEN) #Makes button visabilly pushed down
    winsound.PlaySound("Piano Octave\C.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def D(event=0):
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonD.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\D.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def E(event=0):
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonE.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\E.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def F(event=0):
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonF.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\F.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def G(event=0):
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonG.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\G.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def A(event=0):
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonA.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\A.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def B(event=0):
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonB.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\B.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
def C2(event=0):
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonC2.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\C2.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
   
''' Each function above plays the note and the SND_ASYNC allows a different
sound to be played before the first sound is finished.'''

def mrSandman(speed = 0.4, num = 2):
    x = 2
    while x>0:
        C()
        time.sleep(speed)
        E()
        time.sleep(speed)
        G()
        time.sleep(speed)
        B()
        time.sleep(speed)
        A()
        time.sleep(speed)
        G()
        time.sleep(speed)
        E()
        time.sleep(speed)
        C()
        time.sleep(speed)
        D()
        time.sleep(speed)
        F()
        time.sleep(speed)
        A()
        time.sleep(speed)
        C2()
        time.sleep(speed)
        B()
        time.sleep(1+speed)
        x=x-1
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset

'''def LittleLamb(speed = 0.4):
    x = 2
    while x>0:
        C()
        time.sleep(speed)
        E()
        time.sleep(speed)
        G()
        time.sleep(speed)
        B()
        time.sleep(speed)
        A()
        time.sleep(speed)
        G()
        time.sleep(speed)
        E()
        time.sleep(speed)
        C()
        time.sleep(speed)
        D()
        time.sleep(speed)
        F()
        time.sleep(speed)
        A()
        time.sleep(speed)
        C2()
        time.sleep(speed)
        B()
        time.sleep(1)
        x=x-1
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset'''    
########
#Buttons
########
ButtonC = Button(root, bg="white", height = 20, width = 10, command = C)
ButtonD = Button(root, bg="white", height = 20, width = 10, command = D)
ButtonE = Button(root, bg="white", height = 20, width = 10, command = E)
ButtonF = Button(root, bg="white", height = 20, width = 10, command = F)
ButtonG = Button(root, bg="white", height = 20, width = 10, command = G)
ButtonA = Button(root, bg="white", height = 20, width = 10, command = A)
ButtonB = Button(root, bg="white", height = 20, width = 10, command = B)
ButtonC2 = Button(root, bg="white", height = 20, width = 10, command = C2)
SandmanButton = Button(root, bg="black", height = 5, width = 10, command = mrSandman, text = "Mr \n Sandman", fg = "yellow")
SandmanButton.grid(row = 1, column = 12)
#ButtonCsharp = Button(root, bg="black", height = 15, width = 5)
#ButtonDsharp = Button(root, bg="black", height = 15, width = 10)
#ButtonDsharp1 = Button(root, bg="black", height = 15, width = 10)

#################################
#Binding Buttons to Keyboard keys
#################################
root.bind('1', C)
root.bind('2', D)
root.bind('3', E)
root.bind('4', F)
root.bind('5', G)
root.bind('6', A)
root.bind('7', B)
root.bind('8', C2)

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
