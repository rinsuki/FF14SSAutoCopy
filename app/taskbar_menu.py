import wx
from .preferences.editor import PreferencesEditor
from . import app

class TaskBarMenu(wx.Menu):
    def __init__(self):
        super().__init__()
        self.Append(1, "設定")
        self.Append(wx.ID_EXIT, "終了")
        self.Bind(wx.EVT_MENU, self.onMenuItemClicked)
    
    def onMenuItemClicked(self, event):
        id = event.GetId()
        if id == 1:
            frame = PreferencesEditor()
            frame.Show(None)
        elif id == wx.ID_EXIT:
            app.ExitMainLoop()