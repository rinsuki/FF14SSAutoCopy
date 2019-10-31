import wx
from .general_page import GeneralPage

class PreferencesEditor(wx.PreferencesEditor):
    def __init__(self):
        super().__init__()
        self.AddPage(GeneralPage())
        self.AddPage(GeneralPage())
        self.AddPage(GeneralPage())