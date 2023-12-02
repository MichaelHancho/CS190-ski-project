from tkinter import *
import random
import time 


root = Tk()

current=time.localtime()
current=time.asctime(current)
time_day=Label(root,text=' ')
time_day.grid(row=0,column=2)

def time_o_day():
    current=time.localtime()
    current=time.asctime(current)
    time_day.config(text=str(current))
    root.after(1000,time_o_day)
root.after(1,time_o_day)

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
    print(DB_list)
    DB=random.choice(DB_list)
    random_lift.config(text='Take a lap on the ' + DB + '.')

## MH worked 1 hour to create liftStatus grid
def liftStatusGrid():  #MH
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
            Label(root,text=openlifts[i],bg='DarkOliveGreen1').grid(row = i+1,column = 0)
            #Button(root, text="O").grid(row=i+1, column=1)
        Label(root,text=closedlifts[i], bg='salmon1').grid(row = i+1,column = 1)
        #Button(root,text="O").grid(row=i+1, column=3)
    return gridNum


## MH 1 hour on file programinng
resort = 'CB.txt'  #temporary
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
            #status = timeReader(linelist[2], time)
            openlifts.append([linelist[1]])
print("open lifts: ", openlifts)
print("not running", closedlifts)

canvas = Canvas(root)
gridHeight = liftStatusGrid()
print(gridHeight)

Button(root, text='Find me a lift that serves greens!', command=rand_green).grid(row=2,column=3)
Button(root,text='Find me a lift that serves blues!', command=rand_blue).grid(row=3,column=3)
Button(root,text='Find me a lift that serves blacks!', command=rand_black).grid(row=4,column=3)
Button(root, text='Find me a lift that serves Double-Blacks!', command=rand_DB).grid(row=5,column=3)
Label(root,text='Random Lift Generator:').grid(row=1,column=3)



##

#time MH
curr = time.localtime()  #current equals localtime() output
curr = time.asctime(curr)  #asctime() converts current to readable string
print(curr)
curr = curr.split(" ")
time_ = curr[4].split(":")
for i in range(3):
    time_[i] = int(time_[i])
print(time_)  #time equals integer list of time in format: hours, minutes, seconds

options = []
with open('CB.txt') as f:
    for line in f:
        line = line.strip('\n')
        linelist=line.split(' - ')
        options.append(linelist[1])

clicked=StringVar()
clicked.set('Select a Lift')
drop = OptionMenu(root, clicked, *options)
drop.grid(row=2,column=2)
Button(root, text = 'What does this lift serve?', command=show).grid(row=3,column=2)
label=Label( root, text = ' ')
label.grid(row=4,column=2)
random_lift=Label(root, text = ' ')
random_lift.grid(row=7,column=4)
Label(root,text='Random Lift:').grid(row=7,column=3)
what_lift=Label(root,text=' ')
what_lift.grid(column=2,row=11,columnspan=6,)
Label(root,text='Lift Information:').grid(row=1,column=2)

def food():
    food_list=[]
    with open('CB.txt') as f:
        for line in f:
            line = line.strip('\n')
            infolist=line.split(' - ')
            if 'food' in infolist[3]:
                liftname=infolist[1]
                food_list.append(liftname)
            else:
                continue
    food=random.choice(food_list)
    random_lift.config(text='Get some food on the ' + food + '.')
    
Button(root,text='Find me some food!',command=food).grid(row=6,column=3)

def green_lifts():
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
    what_lift.config(text='These lifts serve Greens:' + str(green_list))
    


def blue_lifts():
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
    what_lift.config(text='These lifts serve Blues:' + str(blue_list))



def black_lifts():
    black_list=[]
    with open('CB.txt') as f:
        for line in f:
            line = line.strip('\n')
            infolist=line.split(' - ')
            if 'black' in infolist[3]:
                liftname=infolist[1]
                black_list.append(liftname)
            else:
                continue
    what_lift.config(text='These lifts serve Blacks:' + str(black_list))
    


def DB_lifts():
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
    what_lift.config(text='These lifts serve Double Blacks:' + str(DB_list))
    


def food_serv():
    grub_list=[]
    with open('CB.txt') as f:
        for line in f:
            line = line.strip('\n')
            infolist=line.split(' - ')
            if 'food' in infolist[3]:
                liftname=infolist[1]
                grub_list.append(liftname)
            else:
                continue
    what_lift.config(text='These lifts provide food service:' + str(grub_list))
    
Button(root,text='What lifts provide food service?',command=food_serv).grid(row=10,column=2)
Button(root,text='What lifts serve Double Blacks?',command=DB_lifts).grid(row=9,column=2)
Button(root,text='What lifts serve Blacks?',command=black_lifts).grid(row=8,column=2)
Button(root,text='What lifts serve Blues?',command=blue_lifts).grid(row=7,column=2)
Button(root,text='What lifts serve Greens?',command=green_lifts).grid(row=6,column=2)
Label(root,text='Lift Finder:').grid(row=5,column=2)

Label(root,text='Enter a ski from your ski quiver (press enter to add skis to your quiver):').grid(row=13,column=2)
skis=Entry(root)
skis.grid(row=13,column=3)

quiver=[]
def ski_quiver(event):
    global quiver
    
    ski_pair=skis.get()
    quiver.append(ski_pair)
    ski_val=str(skis.get())
    leng=len(ski_val)
    skis.delete(0,str(leng))
    
    return quiver

root.bind('<Return>',ski_quiver)
SkiOfDay=Label(root,text=' ')
SkiOfDay.grid(row=14,column=3)

def ski_picker():
    global quiver
    ski_of_the_day=random.choice(quiver)
    SkiOfDay.config(text='ski your ' + ski_of_the_day + ' today')
    
Button(root,text='Pick My Skis!',command=ski_picker).grid(row=14,column=2)

def clear_all():
    global quiver
    list_len=int(len(quiver))
    for i in range(0,list_len):
        quiver.pop()
    
    random_lift.config(text='')
    what_lift.config(text='')
    label.config(text='')
    SkiOfDay.config(text='')
    
Button(root,text='CLEAR ALL',command=clear_all).grid(row=14,column=4)

Label(root,text='Ski Picker:').grid(row=12,column=2,columnspan=3)

root.mainloop()