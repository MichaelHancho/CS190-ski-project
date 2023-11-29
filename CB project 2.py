import time  #started at 
from tkinter import *

##worked 3 hours to create current time, first 5 functions, and the first version of CB.txt

#time
curr = time.localtime()  #current equals localtime() output
curr = time.asctime(curr)  #asctime() converts current to readable string
curr = curr.split(" ")
time = curr[3].split(":")
for i in range(3):
    time[i] = int(time[i])
print(time)  #time equals integer list of time in format: hours, minutes, seconds

root = Tk()


def timeReader(liftHours, time1):
    if liftHours == '3':
        x1 = three(time1)
    elif liftHours == '3.5':
        x1 = threeThirty(time1)
    elif liftHours == '4':
        x1 = four(time1)
    return x1

def three(hms):
    if hms[0] <= 15:
        x = "lift open"
    elif hms[0] >= 9:
        x = "lift open"
    else:
        x = "lift closed"
    return(x)

def threeThirty(hms):
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
    
def four(hms):
    if hms[0] >= 16:
        x = "lift closed"
    elif hms[0] <= 9:
        x = "lift closed"
    else:
        x = "lift open"
    return(x)

#input
def pickResort():
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
    
resort = 'CB.txt'  #temporary


##worked 1 hour on file programinng

with open(resort) as f:
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

##1 hour to create the open/closed grid
canvas = Canvas(root,width=100,height=100)

if len(openlifts) > len(closedlifts):
    gridNum = len(openlifts)
else:
    gridNum = len(closedlifts)
    
for i in range(gridNum):
    Label(root,text="open").grid(row = 0,column = 0)
    Label(root,text="closed").grid(row =0,column = 1)
    if i >= len(openlifts):
        Label(root,text="").grid(row = i+1,column = 0)
    else:
        Label(root,text=openlifts[i]).grid(row = i+1,column = 0)
    Label(root,text=closedlifts[i]).grid(row = i+1,column = 1)

root.mainloop()
