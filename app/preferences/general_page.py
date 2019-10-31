import wx

class GeneralPanel(wx.Panel):
    def __init__(self, panel):
        super().__init__(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        sizer.Add(wx.StaticText(self, label="SSの保存先フォルダ:"))
        sizer.Add(wx.TextCtrl(self))
        

class GeneralPage(wx.StockPreferencesPage):
    def __init__(self):
        super().__init__(wx.StockPreferencesPage.Kind_General)
    def CreateWindow(self, parent):
        return GeneralPanel(parent)
