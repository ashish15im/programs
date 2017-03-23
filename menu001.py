__author__ = 'Ashish'
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Title Bar")
        p=wx.Panel(self)
        self.CreateStatusBar()
        menu=wx.Menu()
        simple=menu.Append(-1,"This is just a string","This is just a help string")
        menu.AppendSeparator()
        exit=menu.Append(-1,"This is another str","This is another help str")
        self.Bind(wx.EVT_MENU,self.OnExit,exit)
        self.Bind(wx.EVT_MENU,self.OnSimple,simple)
        menuBar=wx.MenuBar()
        menuBar.Append(menu,"Menu")
        self.SetMenuBar(menuBar)

    def OnSimple(self,event):
        wx.MessageBox("You selected simple menu item")

    def OnExit(self,event):
        self.Close()

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()