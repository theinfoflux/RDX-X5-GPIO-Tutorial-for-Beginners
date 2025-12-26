
import sys
import signal
import Hobot.GPIO as GPIO
import time
import tkinter as tk

# Handle CTRL+C
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# GPIO pin setup
output_pin = 37  # BOARD encoding

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)

# Functions to control the LED
def turn_on():
    GPIO.output(output_pin, GPIO.HIGH)
    status_label.config(text="LED is ON", fg="green")

def turn_off():
    GPIO.output(output_pin, GPIO.LOW)
    status_label.config(text="LED is OFF", fg="red")

# Build GUI
root = tk.Tk()
root.title("RDX X5 LED Control")

# Buttons
on_button = tk.Button(root, text="Turn ON", command=turn_on, width=15, bg="green", fg="white")
on_button.pack(pady=10)

off_button = tk.Button(root, text="Turn OFF", command=turn_off, width=15, bg="red", fg="white")
off_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="LED is OFF", font=("Helvetica", 14), fg="red")
status_label.pack(pady=20)

# Run the GUI loop
root.mainloop()

# Cleanup GPIO on exit
GPIO.cleanup()