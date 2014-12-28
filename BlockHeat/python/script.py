import webiopi
import datetime

GPIO = webiopi.GPIO

FRONT = 23 # GPIO pin using BCM numbering
BACK = 24 # GPIO pin using BCM numbering

HOUR_ON  = 3  # Turn BlockHeat ON at 04:00
HOUR_OFF = 10 # Turn BlockHeat OFF at 10:00

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the front & back to output
    GPIO.setFunction(FRONT, GPIO.OUT)
    GPIO.setFunction(BACK, GPIO.OUT)

    # retrieve current datetime
    now = datetime.datetime.now()

    # test if we are between ON time and tun the light ON
    if ((now.hour >= HOUR_ON) and (now.hour < HOUR_OFF)):
        GPIO.digitalWrite(FRONT, GPIO.LOW)
        GPIO.digitalWrite(BACK, GPIO.LOW)

# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(FRONT) == GPIO.HIGH):
            GPIO.digitalWrite(FRONT, GPIO.LOW)

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 20)):
        if (GPIO.digitalRead(BACK) == GPIO.HIGH):
            GPIO.digitalWrite(BACK, GPIO.LOW)

    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(FRONT) == GPIO.LOW):
            GPIO.digitalWrite(FRONT, GPIO.HIGH)

    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 00)):
        if (GPIO.digitalRead(BACK) == GPIO.LOW):
            GPIO.digitalWrite(BACK, GPIO.HIGH)

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(FRONT, GPIO.HIGH)
    GPIO.digitalWrite(BACK, GPIO.HIGH)
