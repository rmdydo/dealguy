import RPi.GPIO as GPIO
import time


def toggle(switch, delay=0, duration=10):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(switch, GPIO.OUT)
    time.sleep(delay)
    GPIO.output(switch, 1)
    time.sleep(duration)
    GPIO.output(switch, 0)
