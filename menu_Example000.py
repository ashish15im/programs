__author__ = 'Ashish'
import wx
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"I m creating menu bar")
        p=wx.Panel(self)
        menuBar=wx.MenuBar()#creating menu bar
        menu0=wx.Menu()
        menuBar.Append(menu0,"Left menu Bar")#appending to the menu bar
        menu1=wx.Menu()
        menuBar.Append(menu1,"Center menu Bar")
        menu2=wx.Menu()
        menuBar.Append(menu2,"Left menu Bar")
        self.SetMenuBar(menuBar)#SetmenuBar attach menubar to frame
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=Frame()
    frame.Show()
    app.MainLoop()