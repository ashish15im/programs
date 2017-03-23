__author__ = 'Ashish'
import wx
import wx.grid
class SimpleGrid(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"A simple Grid Example",size=(480,600))
        grid=wx.grid.Grid(self)
        grid.CreateGrid(50,50)
        for row in range(20):
            for col in range(50):
                grid.SetCellValue(row,col,"cell in (%d,%d)" %(row,col))

app=wx.PySimpleApp()
frame=SimpleGrid()
frame.Show()
app.MainLoop()