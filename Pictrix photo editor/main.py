import cv2
import tkinter as tk
from PIL import Image, ImageTk
import subprocess

# create a tkinter window
root = tk.Tk()
root.title("Image Loading..")
root.configure(bg="black")
# open the video file
cap = cv2.VideoCapture('loader.mp4')

# define the duration of the video in seconds
duration = 7

# define a function to display the video frames in tkinter window
def show_frame():
    ret, frame = cap.read()
    if ret:
        # convert the frame to an RGB image and resize it
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (640, 480))

        # create a tkinter photo image from the RGB image
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        # display the photo image in a tkinter label
        label.imgtk = imgtk
        label.config(image=imgtk)

        # check if the duration has elapsed
        if cap.get(cv2.CAP_PROP_POS_MSEC) >= duration * 1000:
            # close the tkinter window
            root.destroy()

    # call this function again after 10 milliseconds
    root.after(10, show_frame)

label1 = tk.Label(root , text="Welcome To PicTrix" ,bg="black",fg="white",font="40")
label1.pack(fill="x")

# create a tkinter label to display the video frames
label = tk.Label(root)
label.pack()

# call the function to display the video frames
show_frame()

# start the tkinter main loop
root.mainloop()

# release the video file
cap.release()

# run the neweditor.py file using subprocess
subprocess.run(['python', 'neweditor.py'])
