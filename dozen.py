#   dozenal clock
#
#   outputs the current time in base 12
#   djanatyn

import time
a = [0,0,0,0,0]
x = 0
def add(x):         # increases the value of a variable - if it overflows it puts a flag
    if(x < 9):
	x = x + 1
    elif(x == 9):
	x = "a"
    elif(x == "a"):
	x = "b"
    elif(x == "b"): # this is true if it bumps up to the next place value
	x = "inc"       # a flag to let the program know to increment the *next* place value and set the current to zero
    return x

def inc():                  # increments the value of the overall time
    global a,x
    a[x] = add(a[x])        # increment the time by one dozsecond
    while(a[x] == "inc"):   # while the current number needs to bump the left place value
        a[x] = 0            # set the current place value to zero
        x = x + 1           # move to the left place value
        a[x] = add(a[x])    # add one to that place value
    x = 0                   # go back to the rightmost place value once all this is finished

tm = time.localtime()
secs_elapsed = tm[5]+(tm[4]*60)+(tm[3]*3600)    # calculates the total number of seconds elapsed today
s = secs_elapsed % 12
while(s!= 0):
    a[x] = s
    secs_elapsed = (secs_elapsed - s)/12
    x = x + 1
    s = secs_elapsed % 12

while(True):
    inc()                       # increment the time
    #time.sleep(.3472222)       # time changed for demonstration purposes (this makes the dozday one day long)
    time.sleep(.1)              
    print a[4],":",a[3],":",a[2],":",a[1],":",a[0] # outputs the time after all operations are complete
