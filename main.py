import sys
import os
import time

try:
    sys.path.append('/home/zshang/Program/LLKey/AndroidViewClient/src')
except:
    pass

from com.dtmilano.android.adb import adbclient
import com.dtmilano.android.viewclient as viewclient

device, serialno = viewclient.ViewClient.connectToDeviceOrExit(verbose=True)

device.touch(900, 945, adbclient.DOWN_AND_UP)
