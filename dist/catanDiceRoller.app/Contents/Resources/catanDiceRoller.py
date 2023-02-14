import random
import tkinter as tk
from time import sleep
from playsound import playsound
from PIL import Image, ImageTk

class var(object):
    pass

redDie=["1","2","3","4","5","6"]
yellowDie=["1","2","3","4","5","6"]
eventDie=["Barbarian Ship","Barbarian Ship","Barbarian Ship","Blue Castle","Green Castle","Yellow Castle"]
redChoice=""
yellowChoice=""
eventChoice=""
total=0
confirmChoice=False
twochance=1
threechance=2
fourchance=3
fivechance=4
sixchance=5
sevenchance=6
eightchance=5
ninechance=4
tenchance=3
elevenchance=2
twelvechance=1
rollcount=0

#open image - general
bg = Image.open('dicerollerbg960.png')
logo = Image.open('catanlogo.jpg')
rollbutton = Image.open('rollbutton.png')

#open images - dice
red1pil = Image.open('red1.png')
red2pil = Image.open('red2.png')
red3pil = Image.open('red3.png')
red4pil = Image.open('red4.png')
red5pil = Image.open('red5.png')
red6pil = Image.open('red6.png')
yellow1pil = Image.open('yellow1.png')
yellow2pil = Image.open('yellow2.png')
yellow3pil = Image.open('yellow3.png')
yellow4pil = Image.open('yellow4.png')
yellow5pil = Image.open('yellow5.png')
yellow6pil = Image.open('yellow6.png')
eventBARBSHIPpil = Image.open('eventBARBSHIP2d.png')
eventGREENpil = Image.open('eventGREEN2d.png')
eventBLUEpil = Image.open('eventBLUE2d.png')
eventYELLOWpil = Image.open('eventYELLOW2d.png')

vlist = var()
vlist.redDie = redDie
vlist.yellowDie = yellowDie
vlist.eventDie = eventDie
vlist.redChoice = redChoice
vlist.yellowChoice = yellowChoice
vlist.eventChoice = eventChoice
vlist.total = total
vlist.confirmChoice = confirmChoice
vlist.twochance = twochance
vlist.threechance = threechance
vlist.fourchance = fourchance
vlist.fivechance = fivechance
vlist.sixchance = sixchance
vlist.sevenchance = sevenchance
vlist.eightchance = eightchance
vlist.ninechance = ninechance
vlist.tenchance = tenchance
vlist.elevenchance = elevenchance
vlist.twelvechance = twelvechance
vlist.rollcount = rollcount
vlist.red1pil = red1pil
vlist.red2pil = red2pil
vlist.red3pil = red3pil
vlist.red4pil = red4pil
vlist.red5pil = red5pil
vlist.red6pil = red6pil
vlist.yellow1pil = yellow1pil
vlist.yellow2pil = yellow2pil
vlist.yellow3pil = yellow3pil
vlist.yellow4pil = yellow4pil
vlist.yellow5pil = yellow5pil
vlist.yellow6pil = yellow6pil
vlist.eventBARBSHIPpil = eventBARBSHIPpil
vlist.eventGREENpil = eventGREENpil
vlist.eventBLUEpil = eventBLUEpil
vlist.eventYELLOWpil = eventYELLOWpil
vlist.rollbutton = rollbutton
vlist.isHoverRollButton = False

root = tk.Tk()
root.title('Catan Cities & Knights Game Dice Roller - By Ben Liu')

#convert dice PIL images to tkinter PhotoImage
red1 = ImageTk.PhotoImage(image=red1pil)
red2 = ImageTk.PhotoImage(image=red2pil)
red3 = ImageTk.PhotoImage(image=red3pil)
red4 = ImageTk.PhotoImage(image=red4pil)
red5 = ImageTk.PhotoImage(image=red5pil)
red6 = ImageTk.PhotoImage(image=red6pil)
yellow1 = ImageTk.PhotoImage(image=yellow1pil)
yellow2 = ImageTk.PhotoImage(image=yellow2pil)
yellow3 = ImageTk.PhotoImage(image=yellow3pil)
yellow4 = ImageTk.PhotoImage(image=yellow4pil)
yellow5 = ImageTk.PhotoImage(image=yellow5pil)
yellow6 = ImageTk.PhotoImage(image=yellow6pil)
eventBARBSHIP = ImageTk.PhotoImage(image=eventBARBSHIPpil)
eventGREEN = ImageTk.PhotoImage(image=eventGREENpil)
eventBLUE = ImageTk.PhotoImage(image=eventBLUEpil)
eventYELLOW = ImageTk.PhotoImage(image=eventYELLOWpil)

vlist.red1 = red1
vlist.red2 = red2
vlist.red3 = red3
vlist.red4 = red4
vlist.red5 = red5
vlist.red6 = red6
vlist.yellow1 = yellow1
vlist.yellow2 = yellow2
vlist.yellow3 = yellow3
vlist.yellow4 = yellow4
vlist.yellow5 = yellow5
vlist.yellow6 = yellow6
vlist.eventBARBSHIP = eventBARBSHIP
vlist.eventGREEN = eventGREEN
vlist.eventBLUE = eventBLUE
vlist.eventYELLOW = eventYELLOW

vlist.red_die = None
vlist.yellow_die = None
vlist.event_die = None

canvas = tk.Canvas(root, width=960, height=720)
canvas.grid(columnspan=10, rowspan=10)

#displaying background
bg = ImageTk.PhotoImage(bg)
canvas.create_image(0, 0, anchor=tk.NW, image=bg)

def rollButtonHover(e):
    vlist.rollbutton = ImageTk.PhotoImage(Image.open('rollbuttonHOVER.png'))
    rollbutton_btn.config(image=vlist.rollbutton)
    vlist.isHoverRollButton = True

def rollButtonLeave(e):
    vlist.rollbutton = ImageTk.PhotoImage(Image.open('rollbutton.png'))
    rollbutton_btn.config(image=vlist.rollbutton)
    vlist.isHoverRollButton = False

#displaying roll button
vlist.rollbutton = ImageTk.PhotoImage(vlist.rollbutton)
rollbutton_btn = tk.Button(root, command=lambda:roll(vlist),image=vlist.rollbutton)
rollbutton_btn.bind("<Enter>", rollButtonHover)
rollbutton_btn.bind("<Leave>", rollButtonLeave)
rollbutton_btn.grid(column=10, row=3)

#function displaying red die
def displayRed(vlist):
    print("Red Die: {}".format(vlist.redChoice))
    if vlist.confirmChoice == True:
        if vlist.redChoice == "1":
            vlist.red_die = canvas.create_image(70, 390, anchor=tk.NW, image=vlist.red1)
        elif vlist.redChoice == "2":
            vlist.red_die = canvas.create_image(70, 390, anchor=tk.NW, image=vlist.red2)
        elif vlist.redChoice == "3":
            vlist.red_die = canvas.create_image(70, 390, anchor=tk.NW, image=vlist.red3)
        elif vlist.redChoice == "4":
            vlist.red_die = canvas.create_image(70, 390, anchor=tk.NW, image=vlist.red4)
        elif vlist.redChoice == "5":
            vlist.red_die = canvas.create_image(70, 390, anchor=tk.NW, image=vlist.red5)
        elif vlist.redChoice == "6":
            vlist.red_die = canvas.create_image(70, 390, anchor=tk.NW, image=vlist.red6)

#function displaying yellow die
def displayYellow(vlist):
    print("Yellow Die: {}".format(vlist.yellowChoice))
    if vlist.confirmChoice == True:
        if vlist.yellowChoice == "1":
            vlist.yellow_die = canvas.create_image(360, 390, anchor=tk.NW, image=vlist.yellow1)
        elif vlist.yellowChoice == "2":
            vlist.yellow_die = canvas.create_image(360, 390, anchor=tk.NW, image=vlist.yellow2)
        elif vlist.yellowChoice == "3":
            vlist.yellow_die = canvas.create_image(360, 390, anchor=tk.NW, image=vlist.yellow3)
        elif vlist.yellowChoice == "4":
            vlist.yellow_die = canvas.create_image(360, 390, anchor=tk.NW, image=vlist.yellow4)
        elif vlist.yellowChoice == "5":
            vlist.yellow_die = canvas.create_image(360, 390, anchor=tk.NW, image=vlist.yellow5)
        elif vlist.yellowChoice == "6":
            vlist.yellow_die = canvas.create_image(360, 390, anchor=tk.NW, image=vlist.yellow6)

#function displaying event die
def displayEvent(vlist):
    print("Event Die: {}\n---\n".format(vlist.eventChoice))
    if vlist.confirmChoice == True:
        if vlist.eventChoice == "Barbarian Ship":
            vlist.event_die = canvas.create_image(650, 390, anchor=tk.NW, image=vlist.eventBARBSHIP)
        elif vlist.eventChoice == "Green Castle":
            vlist.event_die = canvas.create_image(650, 390, anchor=tk.NW, image=vlist.eventGREEN)
        elif vlist.eventChoice == "Blue Castle":
            vlist.event_die = canvas.create_image(650, 390, anchor=tk.NW, image=vlist.eventBLUE)
        elif vlist.eventChoice == "Yellow Castle":
            vlist.event_die = canvas.create_image(650, 390, anchor=tk.NW, image=vlist.eventYELLOW)

def roll(vlist):
    vlist.rollbutton = ImageTk.PhotoImage(Image.open('rollbutton.png'))
    rollbutton_btn.config(image=vlist.rollbutton)
    root.update()
    sleep(0.05)
    vlist.rollbutton = ImageTk.PhotoImage(Image.open('rollbuttonHOVER.png'))
    rollbutton_btn.config(image=vlist.rollbutton)
    root.update()
    sleep(0.05)
    vlist.rollbutton = ImageTk.PhotoImage(Image.open('rollbutton.png'))
    rollbutton_btn.config(image=vlist.rollbutton)
    root.update()
    if vlist.rollcount >= 35:
        vlist.twochance=1
        vlist.threechance=2
        vlist.fourchance=3
        vlist.fivechance=4
        vlist.sixchance=5
        vlist.sevenchance=6
        vlist.eightchance=5
        vlist.ninechance=4
        vlist.tenchance=3
        vlist.elevenchance=2
        vlist.twelvechance=1
        vlist.rollcount=0
    if vlist.rollcount <= 34:
        vlist.confirmChoice = False
        while vlist.confirmChoice == False:
            vlist.redChoice=vlist.redDie[random.randint(0,len(vlist.redDie)-1)]
            vlist.yellowChoice=vlist.yellowDie[random.randint(0,len(vlist.yellowDie)-1)]
            vlist.eventChoice=vlist.eventDie[random.randint(0,len(vlist.eventDie)-1)]
            vlist.total=int(vlist.redChoice)+int(vlist.yellowChoice)
            if vlist.total == 2:
                if vlist.twochance > 0:
                    vlist.twochance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 3:
                if vlist.threechance > 0:
                    vlist.threechance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 4:
                if vlist.fourchance > 0:
                    vlist.fourchance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 5:
                if vlist.fivechance > 0:
                    vlist.fivechance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 6:
                if vlist.sixchance > 0:
                    vlist.sixchance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 7:
                if vlist.sevenchance > 0:
                    vlist.sevenchance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 8:
                if vlist.eightchance > 0:
                    vlist.eightchance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 9:
                if vlist.ninechance > 0:
                    vlist.ninechance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 10:
                if vlist.tenchance > 0:
                    vlist.tenchance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 11:
                if vlist.elevenchance > 0:
                    vlist.elevenchance -= 1
                    vlist.confirmChoice = True
            elif vlist.total == 12:
                if vlist.twelvechance > 0:
                    vlist.twelvechance -= 1
                    vlist.confirmChoice = True             
        canvas.delete(vlist.red_die)
        canvas.delete(vlist.yellow_die)
        canvas.delete(vlist.event_die)
        root.update()
        playsound('diceroll{}.mp3'.format(str(random.randint(1,4))), block=False)
        sleep(1.05)
        displayRed(vlist)
        root.update()
        sleep(0.1)
        displayYellow(vlist)
        root.update()
        sleep(0.1)
        displayEvent(vlist)
        root.update()
        vlist.rollcount += 1

        if vlist.isHoverRollButton == True:
            vlist.rollbutton = ImageTk.PhotoImage(Image.open('rollbuttonHOVER.png'))
            rollbutton_btn.config(image=vlist.rollbutton)
            root.update()
        
        #DEBUGGING
        print("twochance: {}".format(vlist.twochance))
        print("threechance: {}".format(vlist.threechance))
        print("fourchance: {}".format(vlist.fourchance))
        print("fivechance: {}".format(vlist.fivechance))
        print("sixchance: {}".format(vlist.sixchance))
        print("sevenchance: {}".format(vlist.sevenchance))
        print("eightchance: {}".format(vlist.eightchance))
        print("ninechance: {}".format(vlist.ninechance))
        print("tenchance: {}".format(vlist.tenchance))
        print("elevenchance: {}".format(vlist.elevenchance))
        print("twelvechance: {}\n".format(vlist.twelvechance))
        print("rollcount: {}\n---\n".format(vlist.rollcount))

root.mainloop()
