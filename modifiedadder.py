import RPi.GPIO as GPIO  # Import the RPi.GPIO library
import time              # Import the Time library

GPIO.setmode(GPIO.BCM)   # BCM: Broadcom SOC channel
GPIO.setwarnings(False)  # Do not print GPIO warning messages

# Define input A
A3 = 12  # 8's column for input A
A2 = 16  # 4's column for input A
A1 = 6   # 2's column for input A
A0 = 5   # 1's column for input A

# Define input B
B3 = 20  # 8's column for input B
B2 = 21  # 4's column for input B
B1 = 26  # 2's column for input B
B0 = 19  # 1's column for input B

# Define Sum S (output LEDs)
LED_S3 = 25  # 8's column for SUM S
LED_S2 = 8   # 4's column for SUM S
LED_S1 = 11  # 2's column for SUM S
LED_S0 = 9   # 1's column for SUM S

# Set up GPIO pins
GPIO.setup(A3, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A0, GPIO.OUT)

GPIO.setup(B3, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(B0, GPIO.OUT)

GPIO.setup(LED_S3, GPIO.IN)
GPIO.setup(LED_S2, GPIO.IN)
GPIO.setup(LED_S1, GPIO.IN)
GPIO.setup(LED_S0, GPIO.IN)

# Input decimal values
A = int(input("Enter a decimal number for A [0, 15]: "))
B = int(input("Enter a decimal number for B [0, 15]: "))

# Convert A to binary
Abin = [0, 0, 0, 0]
n = 0
while A > 0:
    Remainder = int(A % 2)
    Abin[n] = Remainder
    A = int(A / 2)
    n += 1

# Convert B to binary
Bbin = [0, 0, 0, 0]
n = 0
while B > 0:
    Remainder = int(B % 2)
    Bbin[n] = Remainder
    B = int(B / 2)
    n += 1

print("Binary value for A:")
for x in reversed(Abin):
    print(x, end="")
print()

print("Binary value for B (before flipping):")
for y in reversed(Bbin):
    print(y, end="")
print()

# Flip all bits of B to get 1's complement
Bbin = [1 - bit for bit in Bbin]

print("Binary value for B (after flipping):")
for y in reversed(Bbin):
    print(y, end="")
print()

# Set binary values on GPIO for A
GPIO.output(A3, Abin[3])
GPIO.output(A2, Abin[2])
GPIO.output(A1, Abin[1])
GPIO.output(A0, Abin[0])

# Set binary values on GPIO for B (flipped)
GPIO.output(B3, Bbin[3])
GPIO.output(B2, Bbin[2])
GPIO.output(B1, Bbin[1])
GPIO.output(B0, Bbin[0])

# Print the output from LEDs
print("Binary value for S (A - B):")
print(GPIO.input(LED_S3))  # 8's column
print(GPIO.input(LED_S2))  # 4's column
print(GPIO.input(LED_S1))  # 2's column
print(GPIO.input(LED_S0))  # 1's column