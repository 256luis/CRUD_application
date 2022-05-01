from tkinter import messagebox
from MySQLdb import DataError
from MySQLdb import IntegrityError
from MySQLdb import OperationalError
from display import displayData

""" palitan mo muna root password argument sa main file para makaconnect sa db"""
def update(db, cursor, textFields, datePickers, records):
    try:
        # lagay dito sql commands; pa handle ng faulty data (wrong data types, unique constraints, foreign key constraints)
        print(cursor) # placeholder
    except:
        print(cursor)# placeholder
    else:  # try clause did not raise an exception
        # commit changes
        db.commit()
        
        # show data on table
        displayData(cursor, records)
        
        # notify user
        messagebox.showinfo("Form notification", "Record successfully updated")