from time import sleep
from gpiozero import Button, LED
from threading import Thread

beebutton = Button(26)
beeled = LED(19)

lightgate = Button(16)

sunbutton = Button(21)
sunled = LED(20)

shutdown = False
solved_bee = False
solved_rain = False
solved_sun = False
count = 0
state = 0
falling = False


def watch_bee():
    global shutdown, solved_bee
    while not shutdown:
        if beebutton.is_pressed:
            solved_bee = True
            print('bee is solved')
            beeled.on()
    
def watch_rain():
    global shutdown, solved_rain, count, falling
    while not shutdown:
        while count < 5:
            if lightgate.is_pressed:
                count += 1
        solved_rain = True
        print('rain is solved')
        falling = True
        while falling:
            # falling_rain business
            print('falling rain business')

def watch_sun():
    global shutdown, solved_sun, state
    while not shutdown:
        if sunbutton.is_pressed:
            state = (state+1)%2
        if state == 1:
            sunled.on()
            solved_sun = True
            print('sun is solved')
        if state == 0:
            sunled.off()
            solved_sun = False
            print('sun is unsolved')
    
def flower():
    print('flowers blossom')
    # tom's code in here

def reset():
    global solved_bee, solved_rain, solved_sun, count, state, falling
    solved_bee = False
    solved_rain = False
    solved_sun = False
    count = 0
    state = 0
    beeled.off()
    falling = False

    
thread1 = Thread(target = watch_bee, args = ())
thread2 = Thread(target = watch_rain, args = ())
thread3 = Thread(target = watch_sun, args = ())
thread1.start()
thread2.start()
thread3.start()

reset()    
while True:
    if solved_bee and solved_rain and solved_sun:
        flower()
        sleep(15)
        reset()
