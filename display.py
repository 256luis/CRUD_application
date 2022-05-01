from tkinter import END

def displayData(cursor, table): # function used to show all the records in the database
    cursor.execute("SELECT * FROM PACKAGE")
    
    records = cursor.fetchall()
    
    # delete current data in table
    for item in table.get_children():
        table.delete(item)
    
    # show all data
    for row in records:
        table.insert("", END, values=row)
    