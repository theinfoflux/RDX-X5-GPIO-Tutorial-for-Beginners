import sys
import signal
import Hobot.GPIO as GPIO
import tkinter as tk

# ------------------ Signal Handling ------------------
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# ------------------ GPIO Setup ------------------
LED_PIN = 37      # BOARD pin for LED
IR_PIN = 11       # BOARD pin for IR sensor

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(IR_PIN, GPIO.IN)

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("IR Sensor & LED Control")
root.geometry("420x420")
root.configure(bg="#1e1e1e")

# Title
title_label = tk.Label(
    root,
    text="IR SENSOR & LED CONTROL",
    font=("Helvetica", 18, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title_label.pack(pady=15)

# Motion Status Frame
motion_frame = tk.Frame(root, bg="#2b2b2b")
motion_frame.pack(fill="x", padx=20, pady=10)

motion_label = tk.Label(
    motion_frame,
    text="NO MOTION DETECTED",
    font=("Helvetica", 14, "bold"),
    fg="#aaaaaa",
    bg="#2b2b2b"
)
motion_label.pack(pady=15)

# LED Status Frame
led_frame = tk.Frame(root, bg="#2b2b2b")
led_frame.pack(fill="x", padx=20, pady=10)

led_status_label = tk.Label(
    led_frame,
    text="LED TURNED OFF",
    font=("Helvetica", 14, "bold"),
    fg="#ff4d4d",
    bg="#2b2b2b"
)
led_status_label.pack(pady=15)

# ------------------ Functions ------------------
def turn_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    led_status_label.config(text="LED TURNED ON", fg="#00ff99")

def turn_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    led_status_label.config(text="LED TURNED OFF", fg="#ff4d4d")

def clear_motion_message():
    motion_label.config(text="")

def check_motion():
    if GPIO.input(IR_PIN) == GPIO.LOW:
        GPIO.output(LED_PIN, GPIO.HIGH)
        motion_label.config(text="MOTION DETECTED", fg="#4da6ff")
        led_status_label.config(text="LED TURNED ON", fg="#00ff99")
        root.after(4000, clear_motion_message)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        motion_label.config(text="NO MOTION DETECTED", fg="#aaaaaa")
        led_status_label.config(text="LED TURNED OFF", fg="#ff4d4d")

    root.after(200, check_motion)

# ------------------ Control Buttons ------------------
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=25)

on_button = tk.Button(
    button_frame,
    text="TURN LED ON",
    command=turn_on,
    width=16,
    font=("Helvetica", 12, "bold"),
    bg="#00b377",
    fg="white",
    relief="flat"
)
on_button.grid(row=0, column=0, padx=10)

off_button = tk.Button(
    button_frame,
    text="TURN LED OFF",
    command=turn_off,
    width=16,
    font=("Helvetica", 12, "bold"),
    bg="#cc0000",
    fg="white",
    relief="flat"
)
off_button.grid(row=0, column=1, padx=10)

# ------------------ Start Motion Detection ------------------
check_motion()

root.mainloop()

GPIO.cleanup()

