from tkinter import*#started at 3:20 pm on 11/27/23 by KD stopped at 5:20 pm for a total of 2 hrs
import random #11-12 am on 11/29/23 by KD 1 hr
import time#6:30 on 11/29/23 finished at 8:30, 2hrs KD

root=Tk()

current = time.localtime()  #current equals localtime() output
current = time.asctime(current)
time_day=Label(root,text=" ")
time_day.grid(row=9,column=2)

def time_o_day():#updates time
    current = time.localtime()  #current equals localtime() output
    current = time.asctime(current)
    time_day.config(text=str(current))
    root.after(1000,time_o_day)
root.after(1,time_o_day)
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
            
            
    
options=['East River Express','Paradise Express','Teocali Lift','Red Lady Express','West Wall Lift','Aspen Carpet','Pine Carpet','Spruce Carpet','High Lift T-Bar','Peachtree Lift','North Face Lift T-Bar','Gold Link Lift','Painter Boy Lift','Prospect Lift']

clicked=StringVar()

clicked.set('Select a Lift')

drop = OptionMenu(root, clicked, *options)
drop.grid(row=0,column=2)

Button(root, text = 'What does this lift serve?', command=show).grid(row=1,column=2)

label=Label( root, text = ' ')
label.grid(row=2,column=2)
random_lift=Label(root, text = ' ')
random_lift.grid(row=4,column=2)

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
    
Button(root, text='Find me a lift that serves greens!', command=rand_green).grid(row=3,column=0)
        


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

Button(root,text='Find me a lift that serves blues!', command=rand_blue).grid(row=3,column=1)

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
    
    
Button(root,text='Find me a lift that serves blacks!', command=rand_black).grid(row=3,column=2)
            

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
            
    DB=random.choice(DB_list)
    random_lift.config(text='take a lap on the ' + DB + '.')
    
    
Button(root, text='Find me a lift that serves Double-Blacks!', command=rand_DB).grid(row=3,column=3)

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
    grub=random.choice(food_list)
    random_lift.config(text='Get some food on the ' + grub + '.')
    
Button(root,text='Find me some food!',command=food).grid(row=3,column=4)

what_lift=Label(root,text=' ')
what_lift.grid(column=0,row=8,columnspan=5)


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
    
Button(root,text='What lifts serve Greens?',command=green_lifts).grid(row=7,column=0)

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

Button(root,text='What lifts serve Blues?',command=blue_lifts).grid(row=7,column=1)

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
    
Button(root,text='What lifts serve Blacks?',command=black_lifts).grid(row=7,column=2)

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
    
Button(root,text='What lifts serve Double Blacks?',command=DB_lifts).grid(row=7,column=3)

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
    
Button(root,text='What lifts provide food service?',command=food_serv).grid(row=7,column=4)

root.mainloop()