import RPi.GPIO as GPIO # Import the RPi.GPIO library
import time # Import the Time library
GPIO.setmode(GPIO.BCM) # BCM: Broadcom SOC channel, cf. BOARD
GPIO.setwarnings(False) # Do not print GPIO warning messages
# Selection bits
S2 = 25 # Use BCM pin number 25 for S2
S1 = 8 # Use BCM pin number 8 (CE0) for S1
S0 = 7 # Use BCM pin number 7 (CE1) for S0
# Data inputs
D0 = 5 # Use BCM pin number 5 for D0
D1 = 6 # Use BCM pin number 6 for D1
D2 = 13 # Use BCM pin number 13 for D2
D3 = 19 # Use BCM pin number 19 for D3
D4 = 21 # Use BCM pin number 21 for D4
D5 = 20 # Use BCM pin number 20 for D5
D6 = 16 # Use BCM pin number 16 for D6
D7 = 12 # Use BCM pin number 12 for D7
# Output F
F = 26 # Use BCM pin number 26 for output


GPIO.setup(S0,GPIO.OUT) # Setup pin 7 for GPIO.OUT
GPIO.setup(S1,GPIO.OUT) # Setup pin 8 for GPIO.OUT
GPIO.setup(S2,GPIO.OUT) # Setup pin 25 for GPIO.OUT
GPIO.setup(D0,GPIO.OUT) # Setup pin 5 for GPIO.OUT
GPIO.setup(D1,GPIO.OUT) # Setup pin 6 for GPIO.OUT
GPIO.setup(D2,GPIO.OUT) # Setup pin 13 for GPIO.OUT
GPIO.setup(D3,GPIO.OUT) # Setup pin 19 for GPIO.OUT
GPIO.setup(D4,GPIO.OUT) # Setup pin 21 for GPIO.OUT
GPIO.setup(D5,GPIO.OUT) # Setup pin 20 for GPIO.OUT
GPIO.setup(D6,GPIO.OUT) # Setup pin 16 for GPIO.OUT
GPIO.setup(D7,GPIO.OUT) # Setup pin 12 for GPIO.OUT
GPIO.setup(F,GPIO.IN) # Setup pin 26 for GPIO.IN


# Convert DEC to BIN
D = input("Enter a decimal number for the input D [0, 256] (D7,D6,D5,D4,D3,D2,D1,D0):")
D = int(D) # Convert into an integer number
Dbin = [] # define an array D
Dbin = [0,0,0,0,0,0,0,0] # Initialize the array D
n = 0
while (D > 0):
    Remainder = int(D%2) # Execute MOD operation to get Remainder
    Dbin[n] = Remainder # Save Remainder to the Array D
    D = int(D/2) # Divide DEC by 2 and save the quotient
    n = n + 1 # Increase the array index number
print ("Binary value for D: ")
for x in reversed(Dbin): # Print the array D in reverse order
    print (x)
# Set the binary value D to Multiplexer
GPIO.output(D0,Dbin[0])
GPIO.output(D1,Dbin[1])
GPIO.output(D2,Dbin[2])
GPIO.output(D3,Dbin[3])
GPIO.output(D4,Dbin[4])
GPIO.output(D5,Dbin[5])
GPIO.output(D6,Dbin[6])
GPIO.output(D7,Dbin[7])


# Convert DEC to BIN
S = input("Enter a decimal number for the select bits S [0, 7] (S2,S1,S0):")
S = int(S) # Convert into an integer number
Sbin = [] # define an array S
Sbin = [0,0,0] # Initialize the array S
n = 0
while (S > 0):
    Remainder = int(S%2) # Execute MOD operation to get Remainder
    Sbin[n] = Remainder # Save Remainder to the Array S
    S = int(S/2) # Divide DEC by 2 and save the quotient
    n = n + 1 # Increase the array index number
print ("Binary value for S: ")
for x in reversed(Sbin): # Print the array S in reverse order
    print (x)

# Set the binary value S to Multiplexer
GPIO.output(S0,Sbin[0])
GPIO.output(S1,Sbin[1])
GPIO.output(S2,Sbin[2])

print ("F- output: ",GPIO.input(F))
GPIO.cleanup()