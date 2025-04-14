import RPi.GPIO as GPIO
import time

# Define the clock pin
CLK = 12

# Setup GPIO
GPIO.setwarnings(False)         # Prevent "already in use" warnings
GPIO.setmode(GPIO.BOARD)        # Use physical pin numbering
GPIO.setup(CLK, GPIO.OUT)       # Set the CLK pin as output

# Generate clock pulses in an infinite loop
try:
    while True:
        GPIO.output(CLK, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(CLK, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopped by user")
    GPIO.cleanup()
