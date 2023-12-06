from tkinter import *
import random
import time 


root = Tk()


def time_o_day(): #coded by KD
    global hms  #contains [Hours, Minutes, Seconds]
    current = time.localtime()
    current = time.asctime(current)
    timeList = current.split(" ")
    hms = timeList[4].split(":")
    for i in range(3):
        hms[i] = int(hms[i])
    time_day.config(text=str(current))
    root.after(1000,time_o_day)

time_day=Label(root,text=' ')
time_day.grid(row=0,column=2)
time_o_day()  #needed to get value for hms immediately
root.after(1000,time_o_day)

##MH worked 3 hours to create current time, first 5 functions, and the first version of CB.txt
def timeReader(liftHours):  #MH
    if liftHours == '3':
        runningNow = three()
    elif liftHours == '3.5':
        runningNow = threeThirty()
    elif liftHours == '4':
        runningNow = four()
    return(runningNow)
        
def three():  #MH
    global hms
    if hms[0] <= 15:
        running = True
    elif hms[0] >= 9:
        running = True
    else:
        running = False
    return(running)

def threeThirty():  #MH
    global hms
    if hms[0] >= 16:
        running = False
    elif hms[0] == 15:
        if hms[1] >= 30:
            running = False
        else:
            running = True
    elif hms[0] <= 9:
        running = False
    else:
        running = True
    return(running)
    
def four():  #MH
    global hms
    if hms[0] >= 16:
        running = False
    elif hms[0] <= 9:
        running = False
    else:
        running = True
    return(running)

#input not used
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

## MH worked 2 hour to create liftStatus grid
def liftStatusGrid():  #MH
    global hms
    global closedlifts
    global openlifts
    global liftsRun
    liftsRun = []
    liftsNot = []
    for i in range(len(openlifts)):
        if timeReader(closingHour[i]):
            liftsRun.append(openlifts[i])
        else:
            liftsNot.append(openlifts[i])
    for i in range(len(closedlifts)):
        liftsNot.append(closedlifts[i])
    if len(liftsRun) > len(liftsNot):
        gridHeight = len(liftsRun)
    else:
        gridHeight = len(liftsNot)
    Label(root,text="open").grid(row = 0,column = 0)
    Label(root,text="closed").grid(row =0,column = 1)
    for label in root.grid_slaves():
        label.grid_forget()  #deletes all items in grid allowing for continuous updating
    for i in range(gridHeight):
        if i >= len(liftsRun):
            Label(root,text="").grid(row = i+1,column = 0)
        else:
            label = Label(root,text=liftsRun[i],bg='DarkOliveGreen1')
            label.grid(row = i+1,column = 0)
            #Button(root, text="O").grid(row=i+1, column=1)
        label = Label(root,text=liftsNot[i], bg='salmon1')
        label.grid(row = i+1,column = 1)
        #Button(root,text="O").grid(row=i+1, column=3)
    root.after(1000,liftStatusGrid)

def liftStatusGrid():  #MH
    global hms
    global closedlifts
    global openlifts
    global liftsRun
    liftsRun = []
    liftsNot = []
    for i in range(len(openlifts)):
        if timeReader(closingHour[i]):
            liftsRun.append(openlifts[i])
        else:
            liftsNot.append(openlifts[i])
    for i in range(len(closedlifts)):
        liftsNot.append(closedlifts[i])
    if len(liftsRun) > len(liftsNot):
        gridHeight = len(liftsRun)
    else:
        gridHeight = len(liftsNot)
    Label(root,text="open").grid(row = 0,column = 0)
    Label(root,text="closed").grid(row =0,column = 1)
    for i in range(gridHeight):
        if i >= len(liftsRun):
            Label(root,text="").grid(row = i+1,column = 0)
        else:
            Label(root,text=liftsRun[i],bg='DarkOliveGreen1').grid(row = i+1,column = 0)
            #Button(root, text="O").grid(row=i+1, column=1)
        Label(root,text=liftsNot[i], bg='salmon1').grid(row = i+1,column = 1)
        #Button(root,text="O").grid(row=i+1, column=3)
    root.after(10000,liftStatusGrid)
    


##
def show(): #coded by KD
    resort='CB.txt'
    try:
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
            f.close()
    except Exception as e:
         label.config(text=str(e))

def rand_green(): #coded by KD
    green_list=[]
    try:
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
        f.close()
    except Exception as e:
        random_lift.config(text=str(e))
        
def rand_blue():#coded by KD
    blue_list=[]
    try:                       
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
        f.close()
    except exception as e:
        random_lift.config(text=str(e))

def rand_black(): #coded by KD
    black_list=[]
    try:
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
        f.close()
    except exception as e:
        random_lift.config(text=str(e))

def rand_DB(): #coded by KD
    DB_list=[]
    try:
        with open('CB.txt') as f:
            for line in f:
                line = line.strip('\n')
                infolist=line.split(' - ')
                if 'double-black' in infolist[3]:
                    liftname=infolist[1]
                    DB_list.append(liftname)
                else:
                    continue
        DB=random.choice(DB_list)
        random_lift.config(text='Take a lap on the ' + DB + '.')
        f.close()
    except exception as e:
        random_lift.config(text=str(e))


## MH 1 hour on file programinng
resort = 'CB.txt'  #temporary

with open(resort) as f:  #MH
    openlifts = []  #open lifts
    closedlifts = []  #lifts not open for the season
    closingHour= []
    options = []
    for line in f:
        options.append(line[1])
        line = line.strip("\n")
        linelist = line.split(" - ")
        if linelist[0] == 'c':
            closedlifts.append([linelist[1]])
        else:
            #status = timeReader(linelist[2], time)
            openlifts.append([linelist[1]])
            closingHour.append(linelist[2])

liftStatusGrid()

canvas = Canvas(root)
liftStatusGrid()

Button(root, text='Find me a lift that serves greens!', command=rand_green).grid(row=2,column=3)#lines 212 to 216 coded by KD
Button(root,text='Find me a lift that serves blues!', command=rand_blue).grid(row=3,column=3)
Button(root,text='Find me a lift that serves blacks!', command=rand_black).grid(row=4,column=3)
Button(root, text='Find me a lift that serves Double-Blacks!', command=rand_DB).grid(row=5,column=3)
Label(root,text='Random Lift Generator:').grid(row=1,column=3)



##
clicked=StringVar() #lines 242 to 254 coded by KD
clicked.set('Select a Lift')
drop = OptionMenu(root, clicked, *options)
drop.grid(row=2,column=2)
Button(root, text = 'What does this lift serve?', command=show).grid(row=3,column=2)
label=Label( root, text = ' ')
label.grid(row=4,column=2)
random_lift=Label(root, text = ' ')
random_lift.grid(row=8,column=3)
Label(root,text='Random Lift:').grid(row=7,column=3)
what_lift=Label(root,text=' ')
what_lift.grid(column=2,row=11,columnspan=6,)
Label(root,text='Lift Information:').grid(row=1,column=2)

def food(): #coded by KD
    food_list=[]
    try:
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
        f.close()
    except exception as e:
        random_lift.config(text=str(e))
        
Button(root,text='Find me some food!',command=food).grid(row=6,column=3)

def green_lifts(): #coded by KD
    green_list=[]
    try:
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
        f.close()
    except exception as e:
        what_lift.config(text=str(e))


def blue_lifts(): #coded by KD
    blue_list=[]
    try:
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
        f.close()
    except exception as e:
        what_lift.config(text=str(e))

def black_lifts(): #coded by KD
    black_list=[]
    try:
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
        f.close()
    except exception as e:
        what_lift.config(text=str(e))    


def DB_lifts(): #coded by KD
    DB_list=[]
    try:
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
        f.close()
    except exception as e:
        what_lift.config(text=str(e))  


def food_serv(): #coded by KD
    grub_list=[]
    try:
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
        f.close
    except exception as e:
        what_lift.config(text=str(e))
        
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
def ski_quiver(event): #coded by KD
    global quiver
    
    ski_pair=skis.get()
    quiver.append(ski_pair)
    ski_val=str(skis.get())
    leng=len(ski_val)
    skis.delete(0,str(leng))
    
    return quiver

root.bind('<Return>',ski_quiver)
SkiOfDay=Label(root,text='')
SkiOfDay.grid(row=14,column=3)
Label(root,text='Ski of the day').grid(row=14,column=2)

def ski_picker(): #coded by KD
    global quiver
    ski_of_the_day=random.choice(quiver)
    SkiOfDay.config(text=str(ski_of_the_day))
    
Button(root,text='Pick My Skis!',command=ski_picker).grid(row=13,column=4)

def clear_all():    #coded by KD
    global quiver
    list_len=int(len(quiver))
    for i in range(0,list_len):
        quiver.pop()
    
    random_lift.config(text='')
    what_lift.config(text='')
    label.config(text='')
    SkiOfDay.config(text='')

## snowflake animation closing sequence
def flake1():
    for i in range(120):
        canvas.create_rectangle(10,10,20,20,tag='flake1'+str(i), fill=random.choice(snowColors))

def flake2():
    for i in range(70):
        canvas.create_rectangle(30,20,40,30, tag='flake2'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(40,10,50,20, tag='flake2'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(50,20,60,30, tag='flake2'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(40,30,50,40, tag='flake2'+str(i), fill=random.choice(snowColors))

def flake3():
    for i in range(20):
        canvas.create_rectangle(90,30,100,40,tag='flake3'+str(i), fill='snow')
        canvas.create_rectangle(80,20,90,30, tag='flake3'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(100,20,110,30, tag='flake3'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(80,40,90,50, tag='flake3'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(100,40,110,50, tag='flake3'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(90,10,100,20, tag='flake3'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(90,50,100,60, tag='flake3'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(70,30,80,40, tag='flake3'+str(i), fill=random.choice(snowColors))
        canvas.create_rectangle(110,30,120,40, tag='flake3'+str(i), fill=random.choice(snowColors))
        
def genFlakes():
    global canvas
    flakes = [flake1(),flake2(),flake3()]
    for j in flakesAll:
        canvas.moveto(j,random.randint(0,1920),random.randint(-1440,-20))

def moveFlakes():
    global flakesAll
    for j in flakesAll:
        canvas.move(j, 0, 5)
    root.after(100, moveFlakes)

def timedClose(): #closing window while timedClose is running will cause an error
    global canvas
    window = Toplevel(root)
    canvas = Canvas(window, width='1000', height='1000')
    Button(window,text='exit',command=root.destroy).pack()
    Label(window, text='thanks for coming', font=("courier", 44)).pack()
    root.after(50000, root.destroy)
    root.after(100, genFlakes)
    root.after(100, moveFlakes)
    canvas.pack()

snowColors = ['sky blue','snow','powder blue']
color = random.choice(snowColors)
flakesAll = []
for i in range(120):
    flakesAll.append('flake1' + str(i))
for j in range(70):
    flakesAll.append('flake2' + str(j))
for k in range(30):
    flakesAll.append('flake3' + str(k))
print(flakesAll)

Button(root,text='EXIT',command=timedClose).grid(row=0,column=4)


##

    
Button(root,text='CLEAR ALL',command=clear_all).grid(row=14,column=4)

Label(root,text='Ski Picker:').grid(row=12,column=2,columnspan=3)


root.mainloop()

#started at 3:20 pm on 11/27/23 by KD stopped at 5:20 pm for a total of 2 hrs
#11-12 am on 11/29/23 by KD 1 hr
#6:30 on 11/29/23 finished at 8:30, 2hrs KD
#11:00 to 12:00 on 12/1/23 1 hr KD
#8:00 pm on 12/1/23 KD finished at 10:00 pm total 2 hrs
#11:00 am to 12:00 pm on 12/4/23 by KD for 1 hr
#5:00 pm to 6:00 pm by KD 1 HR (debugged original Pre snowflake program)  
#total Hrs=10 by KD