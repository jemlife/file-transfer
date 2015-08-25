import wx
import os
import shutil
import datetime as dt
import time
import sqlite3





    
class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        transferButton = wx.Menu()
        browseButton = wx.Menu()
        initiateButton = wx.Menu()
        initiateItem = initiateButton.Append(wx.ID_COPY, 'Initiate', 'Status msg...')
        transferItem = transferButton.Append(wx.ID_COPY, 'Transfer', 'Status msg...')
        openItem = browseButton.Append(wx.ID_OPEN, '/Users/Jem/Desktop/folder A', 'status msg...')
        openItem2 = browseButton.Append(wx.ID_OPEN, '/Users/Jem/Desktop/folder B', 'status msg...')
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status msg...')

        menuBar.Append(fileButton, 'File')

        menuBar.Append(browseButton, 'Browse')
              
        

        menuBar.Append(transferButton, 'Transfer')
      

        menuBar.Append(initiateButton, 'Initiate')
                             

        

        self.SetMenuBar(menuBar)



        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)

        self.Bind(wx.EVT_MENU, self.OnOpen, openItem2)

    
        self.Bind(wx.EVT_MENU, self.OnTransfer, transferItem)

        self.Bind(wx.EVT_MENU, self.OnInitiate, initiateItem)

        

            
        
        self.SetTitle('File Transfer')
        self.Show(True)


        

    def openDB():
        connection = sqlite3.connect("file_transfer.db")

        c = connection.cursor()
        sql = "SELECT * FROM file_check"

     




    def readData():
        for row in c.execute(sql):
            print row

    def tableCreate():
      c.execute("CREATE TABLE file_check(ID INT, filename TEXT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")





    def dataEntry():
        date = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        c.execute("INSERT INTO file_check (ID, filename, unix, datestamp, keyword, value) VALUES (?, ?, ?, ?, ?, ?)",
                  (idfordb, filename, time.time(), date, keyword, value))
        connection.commit()


    def OnInitiate(self, e):
           now = dt.datetime.now()
           ago = now-dt.timedelta(minutes=1440)
           src = '/Users/Jem/Desktop/folder A'
           dst = '/Users/Jem/Desktop/folder B'
         
           for file in os.listdir(src):
                 full_path = os.path.join(src, file )
                 path = os.path.getmtime(src)
                 st = os.stat(full_path)    
                 mtime = dt.datetime.fromtimestamp(st.st_mtime)
                 shutil.copy(full_path, dst)
                 if mtime > ago:
                    print('%s modified %s'%(path, time))
                


    def OnTransfer(self, e):
          src = "/Users/Jem/Desktop/folder A"
          dst = "/Users/Jem/Desktop/folder B"
          for file in os.listdir(src):
            path = os.path.join(src, file)
            shutil.copy(path, dst)
        


    def OnOpen(self,e):
            """ Open a file"""
            self.dirname = ''
            dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'r')
                self.control.SetValue(f.read())
                f.close()
            dlg.Destroy()
        
    

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()

    
           








