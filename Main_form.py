import tkinter
from tkinter import *
screen1=tkinter.Tk()
screen1.title('main')


var = StringVar(screen1)
var.set("Camera") 
label=tkinter.Label(screen1,textvariable=var)
label.place(x=80, y=15)

var1 = StringVar(screen1)
var1.set("--select--") 
option = OptionMenu(screen1, var1, "  --select--", "webcam", "driodcam",)
option.pack()
option.place(x=190, y=10)

def start_stop():
    if btn_text=="Start":
        action.configure(text = "Stop") 
        #btn_text.set("Stop")
    else:
        action.configure(text = "Start") 
        #btn_text.set("Start")

btn_text=StringVar(screen1)
btn_text.set("Start")
action= tkinter.Button(screen1, text =btn_text, command =start_stop() )
action.place(x=320, y=10)            

    
#def click():
    #action.configure(text = "Start") 


screen1.geometry("500x200+10+20")
screen1.mainloop()
