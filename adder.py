import RPi.GPIO as GPIO # Import the PRi.GPIO library
import time # Import the Time library
GPIO.setmode(GPIO.BCM) # BCM: Broadcom SOC channel
GPIO.setwarnings(False) # Do not print GPIO warning messages
# Define input A
A3 = 12 # 8's column for input A
A2 = 16 # 4's column for input A
A1 = 6 # 2's column for input A
A0 = 5 # 1's column for input A
# Define input B
B3 = 20 # 8's column for input B
B2 = 21 # 4's column for input B
B1 = 26 # 2's column for input B
B0 = 19 # 1's column for input B
# Define Sum S
LED_S3 = 25 # 8's column for SUM S
LED_S2 = 8 # 4's column for SUM S
LED_S1 = 11 # 2's column for SUM S
LED_S0 = 9 # 1's column for SUM S

GPIO.setup(A3, GPIO.OUT) # Setup A3 for GPIO.OUT
GPIO.setup(A2, GPIO.OUT) # Setup A2 for GPIO.OUT
GPIO.setup(A1, GPIO.OUT) # Setup A1 for GPIO.OUT
GPIO.setup(A0, GPIO.OUT) # Setup A0 for GPIO.OUT
GPIO.setup(B3, GPIO.OUT) # Setup B3 for GPIO.OUT
GPIO.setup(B2, GPIO.OUT) # Setup B2 for GPIO.OUT
GPIO.setup(B1, GPIO.OUT) # Setup B1 for GPIO.OUT
GPIO.setup(B0, GPIO.OUT) # Setup B0 for GPIO.OUT
GPIO.setup(LED_S3, GPIO.IN) # Setup LED_S3 for GPIO.IN
GPIO.setup(LED_S2, GPIO.IN) # Setup LED_S2 for GPIO.IN
GPIO.setup(LED_S1, GPIO.IN) # Setup LED_S1 for GPIO.IN
GPIO.setup(LED_S0, GPIO.IN) # Setup LED_S0 for GPIO.IN
# Convert DEC to BIN
A = int(input("Enter a decimal number for A [0, 15]: "))
B = int(input("Enter a decimal number for B [0, 15]: "))
Abin = [] # Define an array A
Bbin = [] # Define an array B
Abin = [0,0,0,0] # Initialize the array A
Bbin = [0,0,0,0] # Initialize the array B

n = 0
while A > 0:
    Remainder = int(A%2) # Execute MOD operation to get Remainder
    Abin[n] = Remainder # Save Remainder to the Array A
    A = int(A/2) # Divide DEC by 2 and save the Quotient
    n = n + 1 # Increase the array index number
    n = 0

while B > 0:
    Remainder = int(B%2) # Execute MOD operation to get Remainder
    Bbin[n] = Remainder # Save Remainder to the Array B
    B = int(B/2) # Divide DEC by 2 and save the Quotient
    n = n + 1 # Increase the array index number

print ("Binary value for A: ")
for x in reversed(Abin): # Print the array A in reverse order
    print(x)

print ("Binary value for B: ")
for y in reversed(Bbin): # Print the array B in reverse order
    print(y)

# Set the binary values A and B to 4-bit full Adder
GPIO.output(A3, Abin[3]) # 8's Column
GPIO.output(A2, Abin[2]) # 4's Column
GPIO.output(A1, Abin[1]) # 2's Column
GPIO.output(A0, Abin[0]) # 1's Column
GPIO.output(B3, Bbin[3]) # 8's Column
GPIO.output(B2, Bbin[2]) # 4's Column
GPIO.output(B1, Bbin[1]) # 2's Column
GPIO.output(B0, Bbin[0]) # 1's Column
# Output for SUM
print ("Binary value for S: ")
print (GPIO.input(LED_S3)) # Print LED_S3, 8's Column
print (GPIO.input(LED_S2)) # Print LED_S2, 4's Column
print (GPIO.input(LED_S1)) # Print LED_S1, 2's Column
print (GPIO.input(LED_S0)) # Print LED_S0, 1's Column