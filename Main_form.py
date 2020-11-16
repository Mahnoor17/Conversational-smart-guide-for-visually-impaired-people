import tkinter
from cv2 import cv2
import PIL.Image, PIL.ImageTk
import time
import numpy as np
from functools import partial
from threading import Thread
from Facedetection import Face_detection as Fd
from Objectdetection import Object_detection as Od
from SpeechRecognition import speech_to_text as St
from SpeechRecognition import text as Ts
import FaceRecognition_form as Fr

#def annotate(image):

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.geometry("750x1200")
        self.window.title(window_title)
        self.video_source = video_source
        label=tkinter.Label(window,text="Camera",  font=("Helvetica", 12) )
        label.place(x=80, y=30)
        var1 = tkinter.StringVar(window)
        var1.set("--select--") 
        option = tkinter.OptionMenu(self.window, var1, "  --select--", "webcam", "driodcam")
        option.pack()
        option.place(x=170, y=25)
        label=tkinter.Label(window,text="Modules", font=("Helvetica", 12) )
        label.place(x=520, y=30)
        fd = tkinter.IntVar()
        fr = tkinter.IntVar()
        od = tkinter.IntVar()
        ar = tkinter.IntVar()
        fe = tkinter.IntVar()
        sr = tkinter.IntVar()
        ts = tkinter.IntVar()
        st = tkinter.IntVar()
        ng= tkinter.IntVar()
        ii = tkinter.IntVar()
        sg = tkinter.IntVar()
        
        c1 = tkinter.Checkbutton(window, text='Face Detection',variable=fd, font=("Helvetica", 10))
        c1.place(x=420, y=50)
        
        c2 = tkinter.Checkbutton(window, text='Face Recognition',variable=fr, onvalue=1, offvalue=0, font=("Helvetica", 10))
        c2.place(x=420, y=70)
        c3 = tkinter.Checkbutton(window, text='Object Detection',variable=od, onvalue=1, offvalue=0, font=("Helvetica", 10))
        c3.place(x=420, y=90)
        c4 = tkinter.Checkbutton(window, text='Activity Recognition',variable=ar, font=("Helvetica", 10))
        c4.place(x=420, y=110)
        c5= tkinter.Checkbutton(window, text='Facial Expression',variable=fe, font=("Helvetica", 10))
        c5.place(x=420, y=130)
        c6 = tkinter.Checkbutton(window, text='Scene Recognition',variable=sr, font=("Helvetica", 10))
        c6.place(x=420, y=150)
        c7 = tkinter.Checkbutton(window, text='Text to speech',variable=ts, font=("Helvetica", 10))
        c7.place(x=560, y=50)
        c8 = tkinter.Checkbutton(window, text='speech to text',variable=st, font=("Helvetica", 10))
        c8.place(x=560, y=70)
        c9= tkinter.Checkbutton(window, text='Natural Language genartion',variable=ng, font=("Helvetica", 10))
        c9.place(x=560, y=90)
        c10 = tkinter.Checkbutton(window, text='Intent Identification',variable=ii, font=("Helvetica", 10))
        c10.place(x=560, y=110)
        c11 = tkinter.Checkbutton(window, text='Summary generation',variable=sg, font=("Helvetica", 10))
        c11.place(x=560, y=130)
        action_btnStart=tkinter.Button(window, text="Start Video", width=20, height=1, command=partial(self.start_video,od,st,ts,fd), font=("Helvetica", 11))
        action_btnStart.place(x=70, y=150)
        action_btnStop=tkinter.Button(window, text="Stop Video", width=20, height=1,  command=self.stop_video, font=("Helvetica", 11))
        action_btnStop.place(x=220, y=150)
        self.text = tkinter.Text(fg="gray",font=("Helvetica", 10))
        self.text.place(x=150,y=600,height=20,width=400)
        self.text.insert(tkinter.END,"speechtotext/texttospeech")
        self.text.configure(state=tkinter.DISABLED)
        def on_click(event):
            self.text.configure(state=tkinter.NORMAL)
            self.text.delete('1.0', tkinter.END)

            # make the callback only work once
            self.text.unbind('<Button-1>', on_click_id)

        on_click_id = self.text.bind('<Button-1>', on_click)
        btn_register=tkinter.Button(window, text="Register Face", width=20, height=1,command=self.a, font=("Helvetica", 11))
        btn_register.place(x=270, y=650)

        self.window.mainloop()
        
        
    def start_video(self,od,st,ts,fd):
        self.vid = MyVideoCapture(self.video_source)
        
        self.canvas = tkinter.Canvas(self.window,width = 600, height = 350)
        self.canvas.pack(padx=20, pady=200)
        self.delay = 10
        
        self.update(od,st,ts,fd)
    def stop_video(self):
        #elf.vid.release()
        
       '''def start_stop():
            if btn_text=="Start":
                action_btnStart.configure(text = "Stop") 
            #btn_text.set("Stop")
            else:
                action_btnStart.configure(text = "Start")'''
    
            
    
    def update(self,od,st,ts,fd):
        
        
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if(fd.get()):
            frame=Fd.detectFace(frame)
        if(od.get()):
            frame=Od.detectObject(frame)
        if(st.get()):
            
            txt=St.recognizeSpeech()
            self.text.configure(state=tkinter.NORMAL)
            self.text.delete('1.0',tkinter.END)
            self.text.insert(tkinter.END,txt)
        if(ts.get()):
            txt=self.text.get('1.0',tkinter.END) 
            Ts.text(txt)  
        
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
        self.window.after(self.delay, self.update,od,st,ts,fd)
    def a(self):
        self.window.destroy()
        Fr.regiserFace()

 
class MyVideoCapture:

    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        self.vid.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        self.FPS = 1/30
        self.FPS_MS = int(self.FPS * 1000)
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
 
     # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
 
 # Create a window and pass it to the Application object
App(tkinter.Tk(), "Conversational Application")
