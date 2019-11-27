#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import win32api
import time
def move_click(x, y, t=0):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                         win32con.MOUSEEVENTF_LEFTUP, X, Y, 0, 0)
    if t == 0:
        time.sleep(random.random()*2+1)
    else:
        time.sleep(t)
    return 0

move_click(30,30)

def resolution():
    return win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1)