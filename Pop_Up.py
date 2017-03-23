__author__ = 'Ashish'
import  wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Creating POp Pop-Ups")
        self.panel=p=wx.Panel(self)
        menu=wx.Menu()
        exit=menu.Append(-1,"Exit")
        self.Bind(wx.EVT_MENU,self.OnExit,exit)
        menuBar=wx.MenuBar()
        menuBar.Append(menu,"Menu")
        self.SetMenuBar(menuBar)
        wx.StaticText(p,-1,"Click Right to show pop-up")
        self.popupMenu=wx.Menu()

        for text in "One two three four five".split():
            item=self.popupMenu.Append(-1,text)
            self.Bind(wx.EVT_MENU,self.OnPopUpItemSelected,item)
        p.Bind(wx.EVT_CONTEXT_MENU,self.OnShowPopUp)

    def OnShowPopUp(self,event):
        pos=event.GetPosition()
        pos=self.panel.ScreenToClient(pos)
        self.panel.PopupMenu(self.popupMenu,pos)


    def OnPopUpItemSelected(self,event):
        item=self.popupMenu.FindItemById(event.GetId())
        text=item.GetText()
        wx.MessageBox("You selectes item '%s'" % text)

    def OnExit(self,event):
        self.Close()

if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()