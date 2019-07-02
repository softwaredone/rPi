#Blinkie 1
from gpiozero import LED
from time import sleep

led = LED(25)
multiplier = 0.1
short_delay = 1
long_delay = 3

code = {
    'A':[0,1],
    'B':[1,0,0,0],
    'C':[1,0,1,0],
    'D':[1,0,0],
    'E':[0],
    'F':[0,0,1,0],
    'G':[1,1,0],
    'H':[0,0,0,0],
    'I':[0,0],
    'J':[0,1,1,1],
    'K':[1,0,1],
    'L':[0,1,0,0],
    'M':[1, 1],
    'N':[1,0],
    'O':[1,1,1],
    'P':[0,1,1,0],
    'Q':[1,1,0,1],
    'R':[0,1,0],
    'S':[0,0,0],
    'T':[1],
    'U':[0,0,1],
    'V':[0,0,0,1],
    'W':[0,1,1],
    'X':[1,0,0,1],
    'Y':[1,0,1,1],
    'Z':[1,1,0,0],
    '1':[0,1,1,1,1],
    '2':[0,0,1,1,1],
    '3':[0,0,0,1,1],
    '4':[0,0,0,0,1],
    '5':[0,0,0,0,0],
    '6':[1,0,0,0,0],
    '7':[1,1,0,0,0],
    '8':[1,1,1,0,0],
    '9':[1,1,1,1,0],
    '0':[1,1,1,1,1]  
        }

def dit():
    led.on()
    sleep(short_delay * multiplier)
    led.off()
    sleep(short_delay * multiplier)


def da():
    led.on()
    sleep(long_delay * multiplier)
    led.off()
    sleep(short_delay * multiplier)

def character_space():
    sleep(3*short_delay * multiplier)
    
def word_space():
    sleep(7*short_delay * multiplier)

def character(symbols):
    for symbol in symbols:
        if(symbol == 1):
            da()
        else:
            dit()
    character_space()

def word(w):
    for c in w:
        character(code[c])
    word_space()

def sentence(s):
    for c in s:
        print(c)
        if(c == ' '):
            word_space()
        else:
            character(code[c])
    word_space()

while True:         
    sentence('HELLO MARKO')
