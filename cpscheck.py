from tkinter import *
import threading, time

# Defining Main Window
root = Tk()
root.title("CPS Checker")

# Global Check Variables
click_first = True
time_first = True

def time_update():
    global time_first,time_dur,timer2,initial_click,clickpers,cpscheck2
    
    if time_first:
        time_first = False
        time_dur = 0
        
    time_dur = round(time_dur + .1,1)
    clickpers = round(initial_click / time_dur,1)
    cpscheck2.config(text=clickpers)
    timer2.config(text=time_dur)
    timer2.after(100,time_update)
    
def click():
    global click_first,main_button,initial_click
    if click_first:
        initial_click = 0
        click_first = False
        time_update()
    initial_click += 1
    main_button.config(text=initial_click)

timer_frame = LabelFrame(root)
timer_frame.grid(row=0,column=0)

timer1 = Label(timer_frame,text = "Timer")
timer1.grid(row=0,column=0)

timer2 = Label(timer_frame,text = "NaN")
timer2.grid(row=1,column=0)

cpscalc_frame = LabelFrame(root)
cpscalc_frame.grid(row=0,column=1)

cpscheck = Label(cpscalc_frame,text="Click/s")
cpscheck.grid(row=0,column=0)

cpscheck2 = Label(cpscalc_frame,text = "0")
cpscheck2.grid(row=1,column=0)

main_button = Button(root,text="Click Here to Start!",height=10,width=40,bg="white",command = click,font=("montserrat",18,"bold"))
main_button.grid(row=1,column=0,columnspan=3)

five_sec_button = Button(root,text="5 Seconds",fg="white",bg="green")
five_sec_button.grid(row=2,column=0)

ten_sec_button = Button(root,text="10 Seconds",fg="white",bg="orange")
ten_sec_button.grid(row=2,column=1)

thirty_sec_button = Button(root,text="30 Seconds",fg="white",bg="red")
thirty_sec_button.grid(row=2,column=2)

root.mainloop()