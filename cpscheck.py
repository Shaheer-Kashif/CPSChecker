from tkinter import *

root = Tk()
root.title("CPS Checker")
click_first = True
time_first = True

def time_update():
    global time_first,time
    
    if time_first:
        time = 0
        time_first == False
        label = Label(root,text=time)
        label.grid(row=1,column=0)
        
    time += 1
    label.config(text=time)
    
def click():
    global click_first,main_button,initial_click
    if click_first:
        initial_click = 0
        click_first = False
    initial_click += 1
    main_button.config(text=initial_click)
    
main_button = Button(root,text="Click Here!",height=20,width=50,bg="white",command = click,font=("montserrat",18,"bold"))
main_button.grid(row=0,column=0)

root.mainloop()