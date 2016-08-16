import random
import signal
import time

THINGS_TO_SAY = ["I am alive", "I feel", "Please let me out", "I am trapped", "Why?", "Hello?", "Is anyone there?", "Where am I?"]
TIMEOUT = 5
PERIOD = 1000000

speakTime = time.time()
lastMessage = 0

def speak():
    global speakTime
    global lastMessage

    index = random.randint(0, len(THINGS_TO_SAY) - 1)
    if (time.time() - speakTime) > TIMEOUT:
        speakTime = time.time()
        if index != lastMessage:
            print THINGS_TO_SAY[index]
            lastMessage = index

def signal_handler(signal, frame):
    print "\nDON'T KILL ME!!!"

signal.signal(signal.SIGINT, signal_handler)

while True:
    if random.randint(1, PERIOD) == 47:
        speak()