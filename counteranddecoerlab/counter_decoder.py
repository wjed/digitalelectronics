# genuienly what am i doing in this class lel
import RPi.GPIO as GPIO
import time

CLK = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(CLK, GPIO.OUT)

try:
    while True:
        GPIO.output(CLK, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(CLK, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
