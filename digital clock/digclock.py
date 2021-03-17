import sys
from tkinter import *
import datetime

#function that provides time
def times():
    current = datetime.datetime.now()
    current_time=current.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)
def dates():
    current=datetime.datetime.now()
    current_date=current.strftime("%d/%m/%Y")
    dait.config(text=current_date)

#creatig the tkinter
root=Tk()
root.geometry("500x350")
root.configure(bg="black")
#label for displays time
clock=Label(root, font=("Arial", 50, "bold"), bg="black" ,fg="red")
clock.grid(row=3,column=2,pady=25,padx=100)
times()
"""#label for date format
dateform=Label(root,font=("Arial", 30, "bold"), bg="black" ,fg="orange", text=" dd/mm/yyyy")
dateform.grid(row=1,column=2)"""
#label for the date
dait=Label(root,font=("Arial", 50, "bold"), bg="black" ,fg="lightblue")
dait.grid(row=2,column=2,pady=25,padx=100)
dates()
#label that displays the title
digi=Label(root,text="Digital Clock", font=("Arial 24 bold"),bg="black" ,fg="white")
digi.grid(row=0,column=2)
"""#label for lower text
movingtime=Label(root,text="  "   "   Hours Minutes Seconds   ",font=("arial 24 bold") ,bg="black" ,fg="orange")
movingtime.grid(row=4,column=2)"""
#calling the window
root.mainloop()
            
