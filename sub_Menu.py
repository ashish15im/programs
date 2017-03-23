__author__ = 'Ashish'
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Sub Menu's")
        p=wx.Panel(self)
        menu=wx.Menu()

        subMenu=wx.Menu()
        subMenu.Append(-1,"Sub item-1")
        subMenu.Append(-1,"Sub item-2")
        subMenu.Append(-1,"Sub item-3")
        menu.AppendMenu(-1,"subMenu",subMenu)


        menu.AppendSeparator()
        exit=menu.Append(-1,"EXIT")
        self.Bind(wx.EVT_MENU,self.OnExit,exit)

        menuBar=wx.MenuBar()
        menuBar.Append(menu,"Menu")
        self.SetMenuBar(menuBar)

    def OnExit(self,event):
        wx.MessageBox("I am closing")
        self.Close()

if __name__=="__main__":
    app=wx.PySimpleApp()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
