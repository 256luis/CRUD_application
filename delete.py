from tkinter import messagebox

""" palitan mo muna root password argument sa main file para makaconnect sa db"""
# 'cursor' pangalan ng db cursor variable
def delete(cursor):
    # notify user
    messagebox.showinfo("Form notification", "Record successfully deleted")