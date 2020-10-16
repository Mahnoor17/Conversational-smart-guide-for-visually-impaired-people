import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time


class App:
    def __init__(self, window, window_title, video_source=1):
        self.window = window
        self.window.geometry("750x1200")
        self.window.title(window_title)
        self.video_source = video_source
        self.label1 =tkinter.Label(text="Register a Person", fg='black',  font=("Helvetica", 16))
        self.label1.pack(anchor=tkinter.CENTER, expand=True)
        self.label2=tkinter.Label(text="Name", font=(12))
        self.label2.place(x=190, y=130)
        self.textBox=tkinter.Entry(text="Name", bd=5, width=45)
        self.textBox.place(x=320, y=130)
         # open video source (This will try to open the Droidcam)
        self.vid = MyVideoCapture(self.video_source)
 
        self.canvas = tkinter.Canvas(window, width = 600, height = 350)
        self.canvas.pack()

        
        self.btn_captureImage=tkinter.Button(window, text="Capture Image", width=30, height=2, command=self.snapshot)
        self.btn_captureImage.pack(anchor=tkinter.CENTER, expand=True)
 
         # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 20
        self.update()
 
        self.window.mainloop()
 
    def snapshot(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
 
    def update(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
        self.window.after(self.delay, self.update)
 
 
class MyVideoCapture:

    def __init__(self, video_source=1):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
 
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

