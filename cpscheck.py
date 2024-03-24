from tkinter import *
import threading, time

# Defining Main Window
root = Tk()
root.title("CPS Checker")

# Global Check Variables
click_first = True
time_first = True

def time_update():
    global time_first,time_dur,label
    
    if time_first:
        time_dur = 0
        time_first = False
        label = Label(root,text=time)
        label.grid(row=1,column=0)
        
    time_dur = round(time_dur + .1,1)
    label.config(text=time_dur)
    label.after(100,time_update)
    
    
def click():
    global click_first,main_button,initial_click
    if click_first:
        time_update()
        initial_click = 0
        click_first = False
    initial_click += 1
    main_button.config(text=initial_click)

        
main_button = Button(root,text="Click Here!",height=10,width=40,bg="white",command = click,font=("montserrat",18,"bold"))
main_button.grid(row=0,column=0)

root.mainloop()