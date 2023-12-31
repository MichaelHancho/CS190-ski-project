import time

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
    

#time
curr = time.localtime()  #current equals localtime() output
curr = time.asctime(curr)  #asctime() converts current to readable string
curr = curr.split(" ")
time = curr[3].split(":")
for i in range(3):
    time[i] = int(time[i])
print(time)  #time equals integer list of time in format: hours, minutes, seconds


resort = 'CB.txt'  #temporary

with open(resort) as f:
    openlifts = []
    for line in f:
        line = line.strip("\n")
        linelist = line.split(" - ")
        if linelist[0] == 'c':
            continue
        else:
            status = timeReader(linelist[2], time)
        openlifts.append([linelist[1],status])
print(openlifts)