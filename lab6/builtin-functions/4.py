
import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")

num = int(input("Enter number: "))
delay = int(input("Enter delay in milliseconds: "))
delayed_sqrt(num, delay)
