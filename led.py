import RPi.GPIO as GPIO
import time
numTimes=int(input("Enter Total number of blinks:"))
speed = float(input("Enter length of each blink(seconds):"))
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 			# Using board pin numbering
GPIO.setup(11, GPIO.OUT)			# LED 1 (Long leg = Pin 11 and short leg = Pin 6 or 9)
GPIO.setup(13, GPIO.OUT)			# LED 2 (Long leg = Pin 13 and short leg = Pin 14 or 20)
def Blink(numTimes,speed):
    for i in range(numTimes):
        print("Iteration",(i+1))
        GPIO.output(11,True)
        GPIO.output(13,True)
        time.sleep(speed)
        GPIO.output(11,False)
        GPIO.output(13,False)
        time.sleep(speed)
Blink(numTimes,speed)
GPIO.cleanup()
print("Done")