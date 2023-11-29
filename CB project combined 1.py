import time
import random 
from tkinter import *

root = Tk()

##MH worked 3 hours to create current time, first 5 functions, and the first version of CB.txt
def timeReader(liftHours, time1):  #MH
    if liftHours == '3':
        x1 = three(time1)
    elif liftHours == '3.5':
        x1 = threeThirty(time1)
    elif liftHours == '4':
        x1 = four(time1)
    return x1

def three(hms):  #MH
    if hms[0] <= 15:
        x = "lift open"
    elif hms[0] >= 9:
        x = "lift open"
    else:
        x = "lift closed"
    return(x)

def threeThirty(hms):  #MH
    if hms[0] >= 16:
        x = "lift closed"
    elif hms[0] == 15:
        if hms[1] >= 30:
            x = "lift closed"
        else:
            x = "lift open"
    elif hms[0] <= 9:
        x = "lift closed"
    else:
        x = "lift open"
    return(x)
    
def four(hms):  #MH
    if hms[0] >= 16:
        x = "lift closed"
    elif hms[0] <= 9:
        x = "lift closed"
    else:
        x = "lift open"
    return(x)

#input
def pickResort():  #MH
    inFails = True
    resorts = ['CB', 'MONARCH']
    while inFails:
        resort = input("enter CB or monarch: ")
        resort = resort.upper()
        resort = resort.lstrip()
        resort = resort.rstrip()
        if resort in resorts:
            inFails = False
    resort += ".txt"
    return resortIn

## MH worked 1 hour to create liftStatus grid
def liftStatusGrid():  #MH
    if len(openlifts) > len(closedlifts):
        gridNum = len(openlifts)
    else:
        gridNum = len(closedlifts)
    for i in range(gridNum):
        Label(root,text="open").grid(row = 0,column = 0)
        Label(root,text="closed").grid(row =0,column = 2)
        if i >= len(openlifts):
            Label(root,text="").grid(row = i+1,column = 0)
        else:
            Label(root,text=openlifts[i],bg='DarkOliveGreen1').grid(row = i+1,column = 0)
            Button(root, text="O").grid(row=i+1, column=1)
        Label(root,text=closedlifts[i], bg='salmon1').grid(row = i+1,column = 2)
        Button(root,text="O").grid(row=i+1, column=3)

##
def show():
    resort='CB.txt'
    
    with open(resort) as f:
        
        selected_lift=clicked.get()
        for line in f:
            line =line.strip('\n')
            infolist=line.split(' - ')
            if infolist[1]==selected_lift:
                grade=infolist[3]
            else:
                continue
    lowest_grade=grade
    label.config(text='The '+ selected_lift + ' serves ' + lowest_grade + ' runs.')

def rand_green():
    green_list=[]
    with open('CB.txt') as f:
        for line in f:
            line = line.strip('\n')
            infolist=line.split(' - ')
            if 'green' in infolist[3]:
                liftname=infolist[1]
                green_list.append(liftname)
            else:
                continue
    green=random.choice(green_list)
    random_lift.config(text='Take a lap on the ' + green + '.')
    
Button(root, text='Find me a lift that serves greens!', command=rand_green).grid(row=18,column=0)

def rand_blue():
    blue_list=[]
    with open('CB.txt') as f:
        for line in f:
            line = line.strip('\n')
            infolist=line.split(' - ')
            if 'blue' in infolist[3]:
                liftname=infolist[1]
                blue_list.append(liftname)
            else:
                continue
            
    blue=random.choice(blue_list)
    random_lift.config(text='Take a lap on the ' + blue + '.')

Button(root,text='Find me a lift that serves blues!', command=rand_blue).grid(row=18,column=2)

def rand_black():
    black_list=[]
    with open('CB.txt') as f:
        for line in f:
            line = line.strip('\n')
            infolist=line.split(' - ')
            if ' black' in infolist[3]:
                liftname=infolist[1]
                black_list.append(liftname)
            else:
                continue
            
    black=random.choice(black_list)
    random_lift.config(text='Take a lap on the ' + black + '.')
    
Button(root,text='Find me a lift that serves blacks!', command=rand_black).grid(row=18,column=3)

def rand_DB():
    DB_list=[]
    with open('CB.txt') as f:
        for line in f:
            line = line.strip('\n')
            infolist=line.split(' - ')
            if 'double-black' in infolist[3]:
                liftname=infolist[1]
                DB_list.append(liftname)
            else:
                continue
            
Button(root, text='Find me a lift that serves Double-Blacks!', command=rand_DB).grid(row=18,column=4)
##

#time MH
curr = time.localtime()  #current equals localtime() output
curr = time.asctime(curr)  #asctime() converts current to readable string
print(curr)
curr = curr.split(" ")
time = curr[3].split(":")
for i in range(3):
    time[i] = int(time[i])
print(time)  #time equals integer list of time in format: hours, minutes, seconds

options = []
with open('CB.txt') as f:
    for line in f:
        line = line.strip('\n')
        linelist=line.split(' - ')
        options.append(linelist[1])

clicked=StringVar()
clicked.set('Select a Lift')
drop = OptionMenu(root, clicked, *options)
drop.grid(row=0,column=6)
Button(root, text = 'What does this lift serve?', command=show).grid(row=1,column=6)
label=Label( root, text = ' ')
label.grid(row=2,column=6)
random_lift=Label(root, text = ' ')
random_lift.grid(row=4,column=6)

resort = 'CB.txt'  #temporary

## MH 1 hour on file programinng
with open(resort) as f:  #MH
    openlifts = []  #open lifts
    closedlifts = []  #lifts not open for the season
    liftmaint = []  #lifts down for maintanance
    for line in f:
        line = line.strip("\n")
        linelist = line.split(" - ")
        if linelist[0] == 'c':
            closedlifts.append([linelist[1]])
        elif linelist[0] == 'm':
            liftmaint.append([linelist[1]])
        else:
            status = timeReader(linelist[2], time)
            openlifts.append([linelist[1]])
print("open lifts: ", openlifts)
print("not running", closedlifts)

canvas = Canvas(root)
liftStatusGrid()

root.mainloop()