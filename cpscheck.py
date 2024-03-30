from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

# Defining Main Window
root = Tk()
root.title("CPS Checker")
root.config(bg = "#8D98A7")

root.resizable(False, False)

# Global Check Variables
click_first = True
time_first = True
time_range = None

# App Icons
turtle = ImageTk.PhotoImage(Image.open("icons/turtle.png"))
mouse = ImageTk.PhotoImage(Image.open("icons/mouse.png"))
rabbit = ImageTk.PhotoImage(Image.open("icons/rabbit.png"))
cheetah = ImageTk.PhotoImage(Image.open("icons/cheetah.png"))

# Game Reset Function (Occurs After Timer Ends)
def game_reset():
    global click_first,time_first,time_range,time_dur,initial_click
    
    # Resetting All Variables
    click_first = True
    time_first = True
    time_range = None
    time_dur = 0
    initial_click = 0
    
# Result Window after Timer Ends
def update_window():
    
    # Getting the Images
    global turtle,mouse,rabbit,cheetah
    
    # Calling Game Reset
    game_reset()
    
    # Creating a New Window and defining its color
    new_window = Toplevel()
    new_window.config(bg="#8D98A7")
    
    new_window.resizable(False, False)
        
    # Creating a Text LabelFrame and Putting Text Inside It
    TextFrame = LabelFrame(new_window,bg="#8D98A7",borderwidth=0)
    textlabel = Label(TextFrame , text= "Error",font=("helvetica",20,"bold"))
    stat_label = Label(TextFrame,text="Placeholder",font=("helvetica",12))
    
    # Placing the Text
    textlabel.grid(row=0,column=0)
    stat_label.grid(row=1,column=0)
    
    # Checking CPS and defining Icon Label and Modifying Text according to it
    if clickpers <= 3.33:
        icon = Label(new_window,image = turtle)
        textlabel.config(text="You are a Turtle.")
        stat_label.config(text="Too slow, You only clicked with the Speed of "+str(clickpers)+" CPS")
        
    elif clickpers > 3.33 and clickpers <= 6.66:
        textlabel.config(text="You are a Mouse.")
        stat_label.config(text="Not Bad, You clicked with the Speed of "+str(clickpers)+" CPS")
        icon = Label(new_window,image = mouse)
        
    elif clickpers > 6.66 and clickpers <= 9.99:
        textlabel.config(text= "You are a Rabbit.")
        stat_label.config(text="Pretty Good, You clicked with the Speed of "+str(clickpers)+" CPS")
        icon = Label(new_window,image = rabbit)
        
    elif clickpers > 9.99:
        textlabel.config(text="You are a Cheetah.")
        stat_label.config(text="Dang that's fast!, You clicked with the Speed of "+str(clickpers)+" CPS")
        icon = Label(new_window,image = cheetah)
    
    # Placing the Icon Label and the Text LabelFrame
    icon.grid(row=0,column=0,padx=5)
    TextFrame.grid(row=0,column=1,padx=5)
    
    # Resetting the buttons to the default values
    timer2.config(text="0")
    cpscheck2.config(text="0")
    
    # Disabling Button for 2 seconds
    main_button.config(text="Click Here to Start!",state=DISABLED)
    root.after(2000, enable_button)
    
def time_update():
    # Making Variables Global so they can be accessible throughout the Program
    global time_first,time_dur,timer2,initial_click,clickpers,cpscheck2
    
    # Checking If it's the first time in the fuction, if it is: Create and assign values.
    if time_first:
        time_first = False
        time_dur = 0
    
    # If the current time is less than the time range
    if time_dur < time_range:
        
        # Incrementing time by .1 and rounding it off 
        time_dur = round(time_dur + .1,1)
        
        # Calculation CPS(Click Per Second)
        clickpers = round(initial_click / time_dur,1)
        
        # Changing Button's text
        cpscheck2.config(text=clickpers)
        timer2.config(text=time_dur)
        
        # Recursion after every .1 second
        timer2.after(100,time_update)
        
    # Otherwise, Stat Window Opens Up 
    else:
        update_window()
        
        
# Function for Enabling Button after the intial 2s timer is over after it shows the result
def enable_button():
    main_button.config(text="Click Here to Start!",state=NORMAL)
    
# Click Function
def click():
    global time_range,initial_click
    
    # Checks if the timer is set or not
    if time_range == None:
        messagebox.showinfo("Error","Please Select a Timer First")
    else:
        # Making Variables Global so they are accessible across the program
        global click_first,main_button,initial_click
        
        # Defining Click Variable if it's the first time
        if click_first:
            initial_click = 0
            click_first = False
            
            # Initiating Timer Function
            time_update()
            
        # Incrementing and Placing the Click Amount
        initial_click += 1
        main_button.config(text=initial_click)
    
# Set Timer Button
def settimer(sec):
    global time_range,click_first
    
    # Checks if the timer is already set and game has been initiated, If True it won't do anything
    if time_range != None and not(click_first):
        pass
    
    # Otherwise It functions
    else:
        time_range = sec
        main_button.config(text="Click Here to Start!\nTimer: "+str(time_range)+"s")

# Timer Section Frame
timer_frame = LabelFrame(root,borderwidth=0,bg="#8D98A7")
timer_frame.grid(row=0,column=0,sticky=E)

timer_frame.option_add('*Label*background', "#8D98A7")

timer1 = Label(timer_frame,text = "Timer",font=("helvetica",15,"bold"))
timer1.grid(row=0,column=0)

timer2 = Label(timer_frame,text = "0",font=("helvetica",15))
timer2.grid(row=1,column=0)

# A Horizontal Line for formatting purposes
filler = LabelFrame(root,bg="#3C3C3C",width=4,height=70,borderwidth=0)
filler.grid(row=0,column=1)

# CPS Calculator Frame
cpscalc_frame = LabelFrame(root,borderwidth=0,bg="#8D98A7")
cpscalc_frame.grid(row=0,column=2,sticky=W+E)

cpscalc_frame.option_add('*Label*background', "#8D98A7")

cpscheck = Label(cpscalc_frame,text="Click/s",font=("helvetica",15,"bold"))
cpscheck.grid(row=0,column=0)

cpscheck2 = Label(cpscalc_frame,text = "0",font=("helvetica",15))
cpscheck2.grid(row=1,column=0)

# Main Click Button
main_button = Button(root,text="Click Here to Start!",height=10,width=40,bg="#2C363F",fg="white",command = click,font=("montserrat",18,"bold"))
main_button.grid(row=1,column=0,columnspan=3)

# Defining Timer Buttons and Placing them
five_sec_button = Button(root,text="5 Seconds",fg="black",bg="#2CF6B3",width=17,command = lambda : settimer(5),font=("helvetica",15,"bold"))
five_sec_button.grid(row=2,column=0)

ten_sec_button = Button(root,text="10 Seconds",fg="black",bg="#FFB627",width=18,command = lambda : settimer(10),font=("helvetica",15,"bold"))
ten_sec_button.grid(row=2,column=1)

thirty_sec_button = Button(root,text="30 Seconds",fg="black",bg="#DC493A",width=17,command = lambda : settimer(30),font=("helvetica",15,"bold"))
thirty_sec_button.grid(row=2,column=2)

root.mainloop()