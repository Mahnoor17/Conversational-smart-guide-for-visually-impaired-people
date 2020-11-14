import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import Integrated 


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.geometry("750x1200")
        self.window.title(window_title)
        self.video_source = video_source
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
        label.place(x=370, y=30)
        var1 = tkinter.IntVar()
        var2 = tkinter.IntVar()
        var3 = tkinter.IntVar()
        c1 = tkinter.Checkbutton(window, text='Face Detection',variable=var1, onvalue=1, offvalue=0, font=("Helvetica", 10))
        c1.place(x=370, y=50)
        c2 = tkinter.Checkbutton(window, text='Face Recognition',variable=var2, onvalue=1, offvalue=0, font=("Helvetica", 10))
        c2.place(x=370, y=70)
        c3 = tkinter.Checkbutton(window, text='Object Detection',variable=var3, onvalue=1, offvalue=0, font=("Helvetica", 10))
        c3.place(x=370, y=90)
        action_btnStart=tkinter.Button(window, text="Start Video", width=20, height=1, command=self.start_video, font=("Helvetica", 11))
        action_btnStart.place(x=100, y=150)
        action_btnStop=tkinter.Button(window, text="Stop Video", width=20, height=1,  command=self.stop_video, font=("Helvetica", 11))
        action_btnStop.place(x=290, y=150)
        self.window.mainloop()
        
    def start_video(self):
        self.vid = MyVideoCapture(self.video_source)
        self.canvas = tkinter.Canvas(width = 600, height = 350)
        self.canvas.pack(padx=20, pady=200)
        self.delay = 20
        self.update()
        
    def stop_video(self):
        self.vid.__del__()
        
    #def start_stop():
     #   if btn_text=="Start":
     #        action_btnStart.configure(text = "Stop") 
            #btn_text.set("Stop")
     #  else:
     #      action_btnStart.configure(text = "Start")
    
            
 
    def update(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.window.after(self.delay, self.update)
 
 
class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
 
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                frame=Integrated.annotate(frame)
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

