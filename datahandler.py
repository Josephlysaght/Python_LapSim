from tkinter import filedialog
import time
import pandas as pd 

def importfile():
   import_file_path = filedialog.askopenfilename()
   df = pd.read_csv (import_file_path, sep = '\t')
  