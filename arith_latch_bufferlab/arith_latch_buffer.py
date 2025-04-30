import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# GPIO pin mappings
A_pins = [6, 13, 16, 12]     # 1’s, 2’s, 4’s, 8’s for A
B_pins = [19, 26, 21, 20]    # 1’s, 2’s, 4’s, 8’s for B
latch_pin = 23               # Enable latch
buffer_pin = 22              # Enable buffer

# Setup all pins as output
for pin in A_pins + B_pins + [latch_pin, buffer_pin]:
    GPIO.setup(pin, GPIO.OUT)

# Helper to convert decimal (0-15) to 4-bit binary list [LSB, ..., MSB]
def dec_to_bin_list(n):
    return [int(bit) for bit in format(n, '04b')][::-1]  # Reversed for LSB first

try:
    # --- Get user input ---
    latch_enable = int(input("Enable the latch? (1 or 0): "))
    buffer_enable = int(input("Enable the buffer? (1 or 0): "))
    A_decimal = int(input("Enter a decimal number for A [0–15]: "))
    B_decimal = int(input("Enter a decimal number for B [0–15]: "))

    # Validate inputs
    if not (0 <= A_decimal <= 15 and 0 <= B_decimal <= 15):
        raise ValueError("Inputs A and B must be between 0 and 15.")

    # Convert to 4-bit binary
    A_binary = dec_to_bin_list(A_decimal)
    B_binary = dec_to_bin_list(B_decimal)

    # Output A binary to GPIO pins
    for pin, value in zip(A_pins, A_binary):
        GPIO.output(pin, value)

    # Output B binary to GPIO pins
    for pin, value in zip(B_pins, B_binary):
        GPIO.output(pin, value)

    # Enable/disable latch and buffer
    GPIO.output(latch_pin, latch_enable)
    GPIO.output(buffer_pin, buffer_enable)

    # Optional delay to allow signal to stabilize
    time.sleep(0.5)

    print("Binary values sent. Observe LED outputs.")
    input("Press Enter to finish and cleanup GPIO...")

finally:
    GPIO.cleanup()
