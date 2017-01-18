from pymouse import PyMouse
from time import sleep
import factory
import calib
import serial
import cPickle

mouse = PyMouse()

# Screen resolution length and height.
resL, resH = mouse.screen_size()[0], mouse.screen_size()[1]
lengthCenter, heightCenter = resL/2, resH/2

print mouse.screen_size()

# Place the cursor at the center of the screen initially.
mouse.move(lengthCenter, heightCenter)

mouse.move(lengthCenter + 0,heightCenter + 100)
sleep(1)
mouse.move(lengthCenter + 100,heightCenter + 100)
sleep(1)
mouse.move(lengthCenter + 100,heightCenter + 0)
sleep(1)
mouse.move(lengthCenter + 0,heightCenter + 0)

