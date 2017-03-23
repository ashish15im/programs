__author__ = 'Ashish'
import wx
from new_001 import BlockWindow
labels="one two three four five six seven eight nine" . split()
class Flex_GridSizer(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Hello Sizers")
        sizer=wx.GridSizer(rows=3,cols=3,hgap=5,vgap=3)
        for label in labels:
            bw=BlockWindow(self,label=label)
            sizer.Add(bw,0,0,0)
        center=self.FindWindowByName("five")
        center.SetMinSize((150,150))
        right=self.FindWindowByName("four")
        right.SetMinSize((150,150))
        right=self.FindWindowByName("one")
        right.SetMinSize((150,150))
        right=self.FindWindowByName("three")
        right.SetMinSize((150,150))
        right=self.FindWindowByName("six")
        right.SetMinSize((150,150))
        self.SetSizer(sizer)
        self.Fit()

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=Flex_GridSizer()
    frame.Show()
    app.MainLoop()