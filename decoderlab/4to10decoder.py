import RPi.GPIO as GPIO # Import the PRi.GPIO library
import time # Import the Time library
GPIO.setmode(GPIO.BCM) # BCM: Broadcome SOC channel, cf. BOARD
GPIO.setwarnings(False) # Do not print GPIO warning messages
LED_8 = 12 # Use BCM pin 12 for 8's Column
LED_4 = 16 # Use BCM pin 16 for 4's Column
LED_2 = 20 # Use BCM pin 20 for 2's Column
LED_1 = 21 # Use BCM pin 21 for 1's Column
DEC_9 = 7 # Use BCM pin 7 for Decimal_9
DEC_8 = 8 # Use BCM pin 8 for Decimal_8
DEC_7 = 25 # Use BCM pin 25 for Decimal_7
DEC_6 = 9 # Use BCM pin 9 for Decimal_6
DEC_5 = 11 # Use BCM pin 11 for Decimal_5
DEC_4 = 5 # Use BCM pin 5 for Decimal_4
DEC_3 = 6 # Use BCM pin 6 for Decimal_3
DEC_2 = 13 # Use BCM pin 13 for Decimal_2
DEC_1 = 19 # Use BCM pin 19 for Decimal_1
DEC_0 = 26 # Use BCM pin 26 for Decimal_0

GPIO.setup(LED_8,GPIO.OUT) # Setup pin 12 for GPIO.OUT
GPIO.setup(LED_4,GPIO.OUT) # Setup pin 16 for GPIO.OUT
GPIO.setup(LED_2,GPIO.OUT) # Setup pin 20 for GPIO.OUT
GPIO.setup(LED_1,GPIO.OUT) # Setup pin 21 for GPIO.OUT
GPIO.setup(DEC_9,GPIO.IN) # Setup pin 7 for GPIO.IN
GPIO.setup(DEC_8,GPIO.IN) # Setup pin 8 for GPIO.IN
GPIO.setup(DEC_7,GPIO.IN) # Setup pin 25 for GPIO.IN
GPIO.setup(DEC_6,GPIO.IN) # Setup pin 9 for GPIO.IN
GPIO.setup(DEC_5,GPIO.IN) # Setup pin 11 for GPIO.IN
GPIO.setup(DEC_4,GPIO.IN) # Setup pin 5 for GPIO.IN
GPIO.setup(DEC_3,GPIO.IN) # Setup pin 6 for GPIO.IN
GPIO.setup(DEC_2,GPIO.IN) # Setup pin 13 for GPIO.IN
GPIO.setup(DEC_1,GPIO.IN) # Setup pin 19 for GPIO.IN
GPIO.setup(DEC_0,GPIO.IN) # Setup pin 26 for GPIO.IN

# Convert DEC to BIN
DEC = input("Enter a number (0 - 9): ")
DEC = int(DEC)
nBin = [] # Define an Array
nBin = [0,0,0,0] # Initialize the Array
n = 0
while DEC > 0:
    Remainder = int(DEC%2) # Execute Mod operation to get Remainder
    nBin[n] = Remainder # Save Remainder to the Array
    DEC=int(DEC/2) # Divide DEC by 2 and save the Quotient
    n = n + 1 # Increase the Array index number
for x in reversed(nBin):
    print(x)

# Set the binary value to LED
GPIO.output(LED_8,nBin[3]) # 8's Column
GPIO.output(LED_4,nBin[2]) # 4's Column
GPIO.output(LED_2,nBin[1]) # 2's Column
GPIO.output(LED_1,nBin[0]) # 1's Column

print ("Check out which DEC is true/false (on/off).")
print ('DEC_9 = ',not(GPIO.input(DEC_9)))
print ('DEC_8 = ',not(GPIO.input(DEC_8)))
print ('DEC_7 = ',not(GPIO.input(DEC_7)))
print ('DEC_6 = ',not(GPIO.input(DEC_6)))
print ('DEC_5 = ',not(GPIO.input(DEC_5)))
print ('DEC_4 = ',not(GPIO.input(DEC_4)))
print ('DEC_3 = ',not(GPIO.input(DEC_3)))
print ('DEC_2 = ',not(GPIO.input(DEC_2)))
print ('DEC_1 = ',not(GPIO.input(DEC_1)))
print ('DEC_0 = ',not(GPIO.input(DEC_0)))
time.sleep(3)