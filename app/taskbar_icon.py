import wx
import wx.adv
from .taskbar_menu import TaskBarMenu

class TaskBarIcon(wx.adv.TaskBarIcon):

    def __init__(self):
        super().__init__()
        self.SetIcon(wx.Icon("app.ico", wx.BITMAP_TYPE_ICO), "FF14SSAutoCopy")
    
    def CreatePopupMenu(self):
        return TaskBarMenu()