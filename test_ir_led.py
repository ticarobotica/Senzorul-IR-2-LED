from machine import Pin, PWM
from time import sleep
from ir_rx import NEC_16
import test_rgb

"""
7 - minus
21 - plus
68 - stanga
64 - dreapta
"""

pin_r=PWM(Pin(19, Pin.OUT))
pin_r.duty_u16(0)

pin_b=PWM(Pin(18, Pin.OUT))
pin_b.duty_u16(0)

pin_ir=Pin(27, Pin.IN)

cul_red=0
cul_blue=0
nr_led=1
cul_led=0


def aprinde_led(nr_led, cul_led):
    if nr_led==1:
        pin_b.duty_u16(cul_led)
        pin_r.duty_u16(0)
    if nr_led==2:
        pin_r.duty_u16(cul_led)
        pin_b.duty_u16(0)
    
def telecomanda(data, addr, ctrl):
    global nr_led
    global cul_blue, cul_red, cul_led
    print(end="\r")
    aprinde_led(nr_led, cul_led)
    if data>0:
        print("Ledul activ este  ---> " ,nr_led, " ", end="\r")
        if data==12: # tasta 1 
            nr_led=1
        elif data==24: # tasta 2
            nr_led=2
        elif data==7: # minus
            if nr_led==1:
                cul_blue-=5000
                if cul_blue<0:
                    cul_blue=0
                cul_led=cul_blue
                
            elif nr_led==2:
                cul_red-=5000
                if cul_red<0:
                    cul_red=0
                cul_led=cul_red
            else:
                pass
        elif data==21: # plus 
            if nr_led==1:
                cul_blue+=5000
                if cul_blue>65535:
                    cul_blue=65535
                cul_led=cul_blue
            elif nr_led==2:
                cul_red+=5000
                if cul_red>65535:
                    cul_red=65535
                cul_led=cul_red
            else:
                pass
        else:
            if nr_led==1:
                cul_led=cul_blue
            else:
                cul_led=cul_red
   
        
        

senzor_ir=NEC_16(pin_ir, telecomanda)

