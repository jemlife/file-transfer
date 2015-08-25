import os
import datetime as dt
import time
import shutil

def copyFile(src, dst):
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
 
