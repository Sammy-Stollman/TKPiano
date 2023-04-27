#Sammy Stollman
#TKinter piano V1
#Date Created: 5/30/2019
#V2 Date: 6/3/2019
#V3 Date: 6/3/2019
#V4 Date: 6/5/2019
#V5 Date: 6/7/2019
'''Version 2 adds prebuilt songs and melodies with functions. It also adds keyboard
input to play the piano.I will try to add chords, but I do not know how 
to play mutiple winsounds at the same time. I will add a menu in a future 
version to play songs, but for now it will just be on screen buttons'''

'''Version 3 adds black keys I will try to add a new widow exclusively for
song buttons in order to watch the keys go down on the other screen'''

'''Version 4 adds a recording button that allows the user to record the notes that they play
and then it plays them back'''

'''Version 5 adds a slider to change the playback speed of the recorder to whatever 
the user wants. I also fixed some problems with the record stop function and play function'''
import time
import winsound
from tkinter import *
########
#Screens
########
root = Tk()
root.title("Piano")
root.geometry("1000x550+400+125")
root.config(bg = "pink")
root2 = Tk()
root2.title("Songs")
root2.geometry("300x550+100+125")
root2.config(bg = "sky blue")
########
#Boolean
########
global recordIt #I had to make it global up here for some reason
recordIt = False
######
#Label
######
L=Label(height = 3, text="Press a key to make a sound", bg = "medium turquoise")
L.grid()


###############
#Note Functions
###############
def C(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal from AllKeys list and raised so they reset
    ButtonC.config(state = ACTIVE, relief = SUNKEN) #Makes button visabilly pushed down
    winsound.PlaySound("Piano Octave\C.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(1)
def D(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonD.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\D.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(2)
def E(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonE.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\E.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(3)
def F(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonF.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\F.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(4)
def G(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonG.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\G.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(5)
def A(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonA.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\A.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(6)
def B(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonB.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\B.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(7)
def C2(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonC2.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\C2.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(8)
def CSharp(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal from BlackKeys list and raised so they reset
    ButtonCsharp.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\Csharp.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(9)
def DSharp(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonDsharp.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\Dsharp.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(10)
def FSharp(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonFsharp.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\Fsharp.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(11)
def GSharp(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonGsharp.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\Gsharp.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(12)
def ASharp(event=0):
    for x in AllKeys:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset
    ButtonAsharp.config(state = ACTIVE, relief = SUNKEN)
    winsound.PlaySound("Piano Octave\Asharp.wav", winsound.SND_ALIAS|winsound.SND_ASYNC)
    if recordIt:
        listOfNotes.append(13)
   
''' Each function above plays the note and the SND_ASYNC allows a different
sound to be played before the first sound is finished. They are all the same except for
the sound they play and the RecordingNumbers they produce.'''
###############
#Song Functions
###############
def mrSandman(speed = 0.4, num = 2):
    SandmanButton.config(state = NORMAL, relief = RAISED)
    while num>0:
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
        num=num-1
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all keys normal and raised so they reset

def LittleLamb(speed = 0.4):
    E()
    time.sleep(speed)
    D()
    time.sleep(speed)
    C()
    time.sleep(speed)
    D()
    time.sleep(speed)
    E()
    time.sleep(speed)
    E()
    time.sleep(speed)
    E()
    time.sleep(speed*2)
    D()
    time.sleep(speed)
    D()
    time.sleep(speed)
    D()
    time.sleep(speed*2)
    E()
    time.sleep(speed)
    G()
    time.sleep(speed)
    G()
    time.sleep(speed*2)
    E()
    time.sleep(speed)
    D()
    time.sleep(speed)
    C()
    time.sleep(speed)
    D()
    time.sleep(speed)
    E()
    time.sleep(speed)
    E()
    time.sleep(speed)
    E()
    time.sleep(speed)
    E()
    time.sleep(speed)
    D()
    time.sleep(speed)
    D()
    time.sleep(speed)
    E()
    time.sleep(speed)
    D()
    time.sleep(speed)
    C()
    time.sleep(speed*2)
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset'''  
        
def Chain(speed = 0.3): 
    D()
    time.sleep(speed)
    E()
    time.sleep(speed)
    G()
    time.sleep(speed)
    G()
    time.sleep(speed)
    A()
    time.sleep(speed)
    E()
    time.sleep(speed)
    E()
    time.sleep(speed*2)
    D()
    time.sleep(speed)
    E()
    time.sleep(speed)
    G()
    time.sleep(speed)
    G()
    time.sleep(speed)
    A()
    time.sleep(speed)
    E()
    time.sleep(speed/2)
    D()
    time.sleep(speed/2)
    E()
    time.sleep(speed*2)
    D()
    time.sleep(speed)
    E()
    time.sleep(speed)
    B()
    time.sleep(speed*2)
    A()
    time.sleep(speed)
    G()
    time.sleep(speed)
    A()
    time.sleep(speed)
    G()
    time.sleep(speed)
    E()
    time.sleep(speed)
    E()
    time.sleep(speed)
    G()
    time.sleep(speed)
    E()
    time.sleep(speed)
    E()
    time.sleep(speed)
    D()
    time.sleep(speed/2)
    E()
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset''' 
####################
#Recording Functions
####################
def record():
    global listOfNotes
    listOfNotes = []
    global recordIt #Record it is global to be used in note functions; Mr. Pietal told me to put in a boolean value in order to get the values an easier way.
    recordIt = True #Boolean value to append things to list
    print ("Recording")
    Recorder.config(width = 12, text = "Stop Recording", command = recordStop)
def recordStop():
    '''For all of the values in the listOfNotes list, it will go through each one and 
    if they are equal to the values we set before, they will play the coresponding note'''
    global listOfNotes
    print ("Stopped Recording")
    global recordIt
    recordIt = False #Stops code from repeating itself
    print (listOfNotes)
    Recorder.config(width = 5, command = record, text = "Record")
def Play():    
    global listOfNotes
    print (playbackSpeed.get())
    TimeWait = 1-(playbackSpeed.get()/13)
    print ("The amount of time between each note is \n", TimeWait, "seconds")
    for notes in range(len(listOfNotes)): #Nathan helped me with this line of code because originaly I had for notes in listOfNotes which took the index of the integers in the list instead of how much was in the list
        if listOfNotes[notes] == 1: #If the note is played, it will corespond to a number and then be played back by the computer in the note function again
            ButtonC.config(relief=SUNKEN)
            C()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 2:
            D()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 3:
            E()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 4:
            F()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 5:
            G()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 6:
            A()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 7:
            B()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 8:
            C2()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 9:
            CSharp()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 10:
            DSharp()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 11:
            FSharp()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 12:
            GSharp()
            time.sleep(TimeWait)
        elif listOfNotes[notes] == 13:
            ASharp()
            time.sleep(TimeWait)
    for x in Buttons:
        x.config(state = NORMAL, relief = RAISED) #Makes all buttons normal and raised so they reset''' 
########
#Buttons
########
ButtonC = Button(root, bg="white", height = 20, width = 10, command = C, text = "1")
ButtonD = Button(root, bg="white", height = 20, width = 10, command = D, text = "2")
ButtonE = Button(root, bg="white", height = 20, width = 10, command = E, text = "3")
ButtonF = Button(root, bg="white", height = 20, width = 10, command = F, text = "4")
ButtonG = Button(root, bg="white", height = 20, width = 10, command = G, text = "5")
ButtonA = Button(root, bg="white", height = 20, width = 10, command = A, text = "6")
ButtonB = Button(root, bg="white", height = 20, width = 10, command = B, text = "7")
ButtonC2 = Button(root, bg="white", height = 20, width = 10, command = C2, text = "8")

SandmanButton = Button(root2, bg="black", height = 5, width = 10, command = mrSandman, text = "Mr \n Sandman", fg = "yellow")
SandmanButton.grid(row = 1, column = 12)
#Note: These buttons are on root2 so the keys can be pressed while the other buttons are; does not work but I will leave them on a seperate screen
LittleLambButton = Button(root2, bg="white", height = 5, width = 10, command = LittleLamb, text = "Mary Had a \n Little Lamb", fg = "black")
LittleLambButton.grid(row = 1, column = 0, columnspan = 2)

ChainButton = Button(root2, bg="yellow", height = 5, width = 10, command = Chain, text = "The Chain")
ChainButton.grid(row = 1, column = 24)

ButtonCsharp = Button(root, bg="black", height = 17, width = 5, command = CSharp, text = "!", fg = "white")
ButtonDsharp = Button(root, bg="black", height = 17, width = 5, command = DSharp, text = "@", fg = "white")
ButtonFsharp = Button(root, bg="black", height = 17, width = 5, command = FSharp, text = "$", fg = "white")
ButtonGsharp = Button(root, bg="black", height = 17, width = 5, command = GSharp, text = "%", fg = "white")
ButtonAsharp = Button(root, bg="black", height = 17, width = 5, command = ASharp, text = "^", fg = "white")

Recorder = Button(root, bg = "red", height = 2, width = 5, text = "Record", fg = "white", relief = FLAT, command = record)
PlayButton = Button (root, bg = "green", height = 2, width = 4, text = "Play", command = Play)

######
#Scale
######
playbackSpeed = DoubleVar()
playbackSpeed.set(1)
slider = Scale(root, label = "Playback Speed", orient = HORIZONTAL, to = 10, variable = playbackSpeed)
slider.grid(row = 3, column = 0)

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
root.bind('!', CSharp)
root.bind('@', DSharp)
root.bind('$', FSharp)
root.bind('%', GSharp)
root.bind('^', ASharp)

######
#Lists
######
AllKeys = [ButtonC, ButtonD, ButtonE, ButtonF, ButtonG, ButtonA, ButtonB, ButtonC2, ButtonCsharp, ButtonDsharp, ButtonFsharp, ButtonGsharp, ButtonAsharp]
Buttons = [ButtonC, ButtonD, ButtonE, ButtonF, ButtonG, ButtonA, ButtonB, ButtonC2]
BlackKeys =[ButtonCsharp, ButtonDsharp, ButtonFsharp, ButtonGsharp, ButtonAsharp]
global listOfNotes
listOfNotes = [] #Make a list to append all values to

################
#Griding buttons
################
for x in range(8):
    Buttons[x].grid(row=1,column=x+1)
#^Makes all of the 8 white buttons in a row next to each other^
for i in range (2):
    BlackKeys[i].grid(row=1, column = i+1, columnspan = 2)
#^Makes two black keys next to eachother in the center of the white keys^
for i in range (2,5):
    BlackKeys[i].grid(row=1, column = i+2, columnspan = 2)
#^Makes three more black keys next to eachother, but seperated from the first two black keys^ 
Recorder.grid(row = 1, column = 0)
PlayButton.grid(row = 2, column =0)
root.mainloop()