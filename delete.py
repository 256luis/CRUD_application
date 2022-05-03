from tkinter import messagebox
from display import displayData

""" palitan mo muna root password argument sa main file para makaconnect sa db"""
def delete(db, cursor, records):
    data = records.item(records.focus(),"values")[1]
    cursor.execute(f"Delete FROM package WHERE brnch_id = {data}")
    # commit changes
    db.commit() 

    # show data on table
    displayData(cursor, records)
    
    # notify user
    messagebox.showinfo("Form notification", "Record successfully deleted")