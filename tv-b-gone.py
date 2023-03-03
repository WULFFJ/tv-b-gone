#Circuit Python TV-B-Gone
#SEEED Xiao RP2040

import array
import time
import digitalio
import board
import pwmio
import pulseio
from digitalio import DigitalInOut, Direction, Pull


#Code starts immediately.  Use a button that will cut off the ground from making a ciruit or switch.


while True:
        
   
        time.sleep(0.5)  # Give a half second before starting
   

        # gooooo!
        f = open("/codes.txt", "r")
        for line in f:
            code = eval(line)
            print(code)
                
            pwm = pwmio.PWMOut(board.D10, frequency = code['freq'],duty_cycle=2 ** 15, variable_frequency=True)
            pwm.frequency = code['freq']
            try:
                repeat = code['repeat']
                delay = code['repeat_delay']
            except KeyError:  # by default, repeat once only!
                repeat = 1
                delay = 0
            # The table holds the on/off pairs
            table = code['table']
            pulses = []  # store the pulses here
            # Read through each indexed element
            for i in code['index']:
                pulses += table[i]  # and add to the list of pulses
            pulses.pop()  # remove one final 'low' pulse
                
            pulse = pulseio.PulseOut(pwm)
                
            for i in range(repeat):
                pulse.send(array.array('H', pulses))
                time.sleep(delay)

            pulse.deinit()

        f.close()

