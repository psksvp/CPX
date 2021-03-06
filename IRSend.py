import time
from adafruit_circuitplayground.express import cpx
import adafruit_irremote
import pulseio
import board

POWER = [254, 1, 190, 65]
DTVUSB = [254, 1, 76, 179]
INPUT = [254, 1, 140, 115]
AUDIO = [254, 1, 62, 193]
MUTE = [254, 1, 230, 25]
PICTURE = [254, 1, 12, 243]
SOUND = [254, 1, 52, 203]
SLEEP = [254, 1, 244, 11]
ASPECT = [254, 1, 84, 171]
ONE = [254, 1, 238, 17]
TWO = [254, 1, 110, 145]
THREE = [254, 1, 174, 81]
FOUR = [254, 1, 206, 49]
FIVE = [254, 1, 78, 177]
SIX = [254, 1, 142, 113]
SEVEN = [254, 1, 246, 9]
EIGHT = [254, 1, 118, 137]
NINE = [254, 1, 182, 73]
ZERO = [254, 1, 86, 169]
CHFAV = [254, 1, 214, 41]
LOOP = [254, 1, 150, 105]
MENU = [254, 1, 22, 233]
EXIT = [254, 1, 54, 201]
EPG = [254, 1, 46, 209]
DISPLAY = [254, 1, 6, 249]
OK = [254, 1, 166, 89]
UP = [254, 1, 102, 153]
DOWN = [254, 1, 70, 185]
LEFT = [254, 1, 198, 57]
RIGHT = [254, 1, 134, 121]
SUBTITLE = [254, 1, 180, 75]
AB = [254, 1, 30, 225]
GOTO = [254, 1, 222, 33]
DSETUP = [254, 1, 116, 139]
DMENU = [254, 1, 100, 155]
DTITLE = [254, 1, 212, 43]

TVTXT = [254, 1, 204, 51]
EJECT = [254, 1, 204, 51]

CANCEL = [254, 1, 188, 67]
PLAYPAUSE = [254, 1, 188, 67]

REVEAL = [254, 1, 60, 195]
STOP = [254, 1, 60, 195]

REPEAT = [254, 1, 228, 27]
RECORD = [254, 1, 228, 27]

HOLD = [254, 1, 236, 19]
BACKWARD = [254, 1, 236, 19]

SIZE = [254, 1, 108, 147]
FORWARD = [254, 1, 108, 147]

SUBPAGE = [254, 1, 172, 83]
PREVIOUS = [254, 1, 172, 83]

INDEX = [254, 1, 44, 211]
NEXT = [254, 1, 44, 211]

DELETE = [254, 1, 124, 131]
RED = [254, 1, 124, 131]

RECORDLIST = [254, 1, 92, 163]
GREEN = [254, 1, 92, 163]

SCHLIST = [254, 1, 156, 99]
YELLOW = [254, 1, 156, 99]

SCREEN = [254, 1, 28, 227]
BLUE = [254, 1, 28, 227]

VOLUP = [254, 1, 220, 35]
VOLDOWN = [254, 1, 148, 107]
 

# Create a 'pulseio' output, to send infrared signals on the IR transmitter @ 38KHz
pwm = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulseout = pulseio.PulseOut(pwm)
# Create an encoder that will take numbers and turn them into NEC IR pulses
encoder = adafruit_irremote.GenericTransmit(header=[9500, 4500], one=[550, 550],
                                            zero=[550, 1700], trail=0)

while True:
    if cpx.button_a:
        print("Button A pressed! \n")
        cpx.red_led = True
        encoder.transmit(pulseout, VOLUP)
        cpx.red_led = False
        # wait so the receiver can get the full message
        time.sleep(0.2)
    if cpx.button_b:
        print("Button B pressed! \n")
        cpx.red_led = True
        encoder.transmit(pulseout, POWER)
        cpx.red_led = False
        time.sleep(0.2)