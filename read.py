#read
from display import displayData
# tip lng, macacall itong function everytime may sinelect na option sa filter combobox
def func_read(cursor):
    connection = displayData.getconnection()
    cursor = cnt.execute()

    cursor.execute('Select * from' )#data()#
    #placeholder lng
    # para mapadali buhay mo, check mo code sa displayData function kung pano mag clear at insert ng rows sa table('records') ng app
    for row in cursor:
        print('row - %r' % (row,))
#filterbox
import tkninter as tk
from tkinter import ttk

window = tk.Tk() 
window.title('Combobox') 
window.geometry('500x250') 

ttk.Label(window, text = "Branch ID", 
          font = ("Times New Roman", 12)).grid(column = 0, 
          row = 5, padx = 5, pady = 25)
          
n = tk.StringVar() 
ID = ttk.Combobox(window, width = 20, textvariable = n) 

ID['values'] = (cursor) 
  
country.grid(column = 1, row = 5) 
country.current()

window.mainloop() 

#search box
pattern = simpledialog.askstring('Search', 'What to search?')

results = []
for line in data.split('\n'):
    if pattern in line:
        results.append(line)
results = "".join(results)
