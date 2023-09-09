
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk
from PIL import Image, ImageOps, ImageTk, ImageFilter
from PIL import Image
from PIL import ImageGrab

root = Tk()
root.geometry("1200x650")
root.title("Photo Editor")
root.config(bg="black")

pen_color = "black"
pen_size = 5
file_path = ""


def add_image():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="E:\wallpaper")
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor='nw')


def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline="")


def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select pen color")[1]


def change_size(size):
    global pen_size
    pen_size = size


def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")


def apply_filter(filter):
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)

    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)

    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)

    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor='nw')
    return image


def save_image():
    # get the filename to save the image as
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        # grab the image from the canvas
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        img = ImageGrab.grab((x, y, x1, y1))
        # save the image
        img.save(file_path, "PNG")


left_frame = Frame(root, width=200, height=600, bg="black")
left_frame.pack(side="left", fill="y")

# canvas to do editing
canvas = Canvas(root, width=750, height=600, bg="black")
canvas.pack(pady=80)

label1 = Label(root, text="Welcome To PicTrix", bg="black", fg="white", font="40")
label1.place(x=650, y=20)

upload_image = Image.open("upload.png")
upload_photo = ImageTk.PhotoImage(upload_image)
button = Button(left_frame, image=upload_photo, command=add_image, bd=0, highlightthickness=0, width=160, height=100,
                bg="black")
button.pack(pady=10)

pen_size_frame = Frame(left_frame, bg="white", width=90)
pen_size_frame.pack(pady=20, padx=20)

# pen size input button
pen_size_1 = Radiobutton(pen_size_frame, text="Small", value=3, bg="black", fg="white", command=lambda: change_size(3))
pen_size_1.pack(side="left")

pen_size_2 = Radiobutton(pen_size_frame, text="Medium", value=5, bg="black", fg="white", command=lambda: change_size(5))
pen_size_2.pack(side="left")
pen_size_2.select()

pen_size_3 = Radiobutton(pen_size_frame, text="Large", value=8, bg="black", fg="white", command=lambda: change_size(8))
pen_size_3.pack(side="left")

# color_button = Button(left_frame, text="Change pen color", command=change_color  ,bg="white" ,fg="black", relief=SUNKEN,borderwidth=3)
# color_button.pack()
color_image = Image.open("color.jpg")
color_image = ImageTk.PhotoImage(color_image)
color_button = Button(left_frame, image=color_image, command=change_color, bd=0, highlightthickness=0, width=160,
                      height=100, bg="black")
color_button.pack(pady=10)

filterFrame = Frame(left_frame, bg="white", width=90)
filterFrame.pack(pady=60)

filter_label = Label(filterFrame, text="select filter", bg="red")
filter_label.pack(fill="x")

filter_combobox = ttk.Combobox(filterFrame, values=["Black and White", "Blur", "Emboss", "Sharpen", "Smooth"])
filter_combobox.pack()
filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))

canvas.bind("<B1-Motion>", draw)

# save button to save the image

save_image2 = Image.open("save.png")
save_image2 = ImageTk.PhotoImage(save_image2)
save_button = Button(left_frame, image=save_image2, command=save_image, bd=0, highlightthickness=0, width=160,
                     height=100, bg="black")
save_button.pack(pady=7)

clear_button = Button(left_frame, text="Clear", command=clear_canvas, width=7, height=2, bg="red")
clear_button.pack(pady=10)

root.mainloop()