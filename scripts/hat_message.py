import time
from sense_hat import SenseHat
sense = SenseHat()
# this script will print a message to the Pi Sense HAT

yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

speed = 0.05
print "Message: "
message = raw_input("")

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
time.sleep(1)
sense.show_letter('!', yellow, back_colour=red)
time.sleep(1)
sense.clear()

