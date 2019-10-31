import ctypes

# 対応したはいいもののwxPython側でちゃんと動いてくれないっぽいので
ENABLE_PERMONITOR_V2 = False

if ENABLE_PERMONITOR_V2:
    if ctypes.windll.user32.SetProcessDpiAwarenessContext(0x00000022) == 1:
        print("Successful to Enable PerMonitor(v2)")
    else:
        print("Failed to Enable PerMonitor(V2) LastError:", ctypes.windll.kernel32.GetLastError())


import wx
import wx.adv

from app.taskbar_icon import TaskBarIcon
from app.preferences.editor import PreferencesEditor
from app import app

icon = TaskBarIcon()

e = PreferencesEditor()
e.Show(None)

app.MainLoop()
icon.RemoveIcon()
