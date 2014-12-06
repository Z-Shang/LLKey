import sys
import os
import time
import pygame
from pygame.locals import *

try:
    sys.path.append('/home/zshang/Program/LLKey/AndroidViewClient/src')
except:
    pass

from com.dtmilano.android.adb import adbclient
import com.dtmilano.android.viewclient as viewclient

#Button Config:
# L1 L2 L3 L4 CEN  R1 R2 R3 R4
# Y1 Y2 Y3 Y4 YCEN Y4 Y3 Y2 Y1
Y1 = 275
Y2 = 530
Y3 = 750
Y4 = 900
XL1 = 225
XL2 = 275
XL3 = 425
XL4 = 645
XR1 = 1155
XR2 = 1375
XR3 = 1515
XR4 = 1575
XCen = 900
YCen = 945
XPause = 1665
YPause = 45

#Key Config
L1 = K_q
L2 = K_w
L3 = K_e
L4 = K_r
KC = K_SPACE #Center
R1 = K_u
R2 = K_i
R3 = K_o
R4 = K_p
KP = K_BACKSPACE #Pause

BG_COLOR = (255, 255, 255)
WINDOW_SIZE = (480, 320)

def getKey(key):
    if key == L1:
        return 1
    elif key == L2:
        return 2
    elif key == L3:
        return 3
    elif key == L4:
        return 4
    elif key == KC:
        return 5
    elif key == R1:
        return 6
    elif key == R2:
        return 7
    elif key == R3:
        return 8
    elif key == R4:
        return 9
    elif key == KP:
        device.touch(XPause, YPause, adbclient.DOWN_AND_UP)
    return -1

def main():
    device, serialno = viewclient.ViewClient.connectToDeviceOrExit(verbose=True)
    def KeyDown(k):
        if k == 1:
            device.touch(XL1, Y1, -1, adbclient.DOWN)
        elif k == 2:
            device.touch(XL2, Y2, -1, adbclient.DOWN)
        elif k == 3:
            device.touch(XL3, Y3, -1, adbclient.DOWN)
        elif k == 4:
            device.touch(XL4, Y4, -1, adbclient.DOWN)
        elif k == 5:
            device.touch(XCen, YCen, -1, adbclient.DOWN)
        elif k == 6:
            device.touch(XR1, Y4, -1, adbclient.DOWN)
        elif k == 7:
            device.touch(XR2, Y3, -1, adbclient.DOWN)
        elif k == 8:
            device.touch(XR3, Y2, -1, adbclient.DOWN)
        elif k == 9:
            device.touch(XR4, Y1, -1, adbclient.DOWN)

    def KeyUp(k):
        if k == 1:
            device.touch(XL1, Y1, -1, adbclient.UP)
        elif k == 2:
            device.touch(XL2, Y2, -1, adbclient.UP)
        elif k == 3:
            device.touch(XL3, Y3, -1, adbclient.UP)
        elif k == 4:
            device.touch(XL4, Y4, -1, adbclient.UP)
        elif k == 5:
            device.touch(XCen, YCen, -1, adbclient.UP)
        elif k == 6:
            device.touch(XR1, Y4, -1, adbclient.UP)
        elif k == 7:
            device.touch(XR2, Y3, -1, adbclient.UP)
        elif k == 8:
            device.touch(XR3, Y2, -1, adbclient.UP)
        elif k == 9:
            device.touch(XR4, Y1, -1, adbclient.UP)

    #pygame init
    pygame.init()
    pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("LL Key")
    screen = pygame.display.get_surface()
    screen.fill(BG_COLOR)

    firstFrame = True

    keyPressed = []

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    k = getKey(event.key)
                    if k < 0:
                        sys.exit()
                    keyPressed.append([k, True])
                    KeyDown(k)
                    print(repr(k) + ' Down')
                elif event.type == pygame.KEYUP:
                    print(keyPressed)
                    k = getKey(event.key)
                    if k < 0:
                        sys.exit()
                    for i in range(0, len(keyPressed)):
                        if keyPressed[i][0] == k:
                            if not keyPressed[i][1]:
                                print(repr(k) + ' Up')
                                KeyUp(k)
                            keyPressed.remove(keyPressed[i])
                            break
                    for i in range (0, len(keyPressed)):
                         keyPressed[i][1] = False

        except KeyboardInterrupt as e:
            break

main()
