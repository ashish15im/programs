__author__ = 'Ashish'
__author__ = 'Ashish'
__author__ = 'Ashish'
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Title Bar")
        p=wx.Panel(self)
        self.btn=wx.Button(p,-1,"Enable",(20,20))
        self.Bind(wx.EVT_BUTTON,self.OnToggleItem,self.btn)
        self.txt=wx.TextCtrl(p,-1,"New Item insertion ")
        btn=wx.Button(p,-1,"Add Menu Item")
        self.Bind(wx.EVT_BUTTON,self.OnAddItem,btn)
        sizer=wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.txt,0,wx.ALL,20)
        sizer.Add(btn,0,wx.TOP | wx.RIGHT,20)
        p.SetSizer(sizer)
        self.menu=menu=wx.Menu()
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
    def OnAddItem(self,event):
        item=self.menu.Append(-1,self.txt.GetValue())
        self.Bind(wx.EVT_MENU,self.OnNewItemSelected,item)

    def OnNewItemSelected(self,event):
        wx.MessageBox("You selected a new item")
        item=self.GetMenuBar().FindItemById(event.GetId())
        text=item.GetText()
        wx.MessageBox("You selected '%s' item"% text )

    def OnToggleItem(self,event):
        menubar=self.GetMenuBar()
        enabled=menubar.IsEnabled(wx.NewId())
        menubar.Enable(wx.NewId(),not enabled)
        self.btn.SetLabel((enabled and "Enable"or"Disable")+"Item")
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()