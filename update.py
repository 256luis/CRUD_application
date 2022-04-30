from tkinter import messagebox

""" palitan mo muna root password argument sa main file para makaconnect sa db"""
# 'cursor' pangalan ng db cursor variable
def update(cursor):
    # validate nyo data ininsert ng user gamit try-catch
    #try:
    #except:
        # palagay sa message box kung anong field(e.g. branch id) kung mali data (kung multiple, yung pinakauna)
        #messagebox.showinfo("Error", "Record successfully added")
        
    # notify user
    messagebox.showinfo("Form notification", "Record successfully updated")