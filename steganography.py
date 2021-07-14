from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import math

image_display_size = 300, 300


def on_click():
    global path_image
    path_image = filedialog.askopenfilename()
    load_image = Image.open(path_image)
    load_image.thumbnail(image_display_size, Image.ANTIALIAS)
    np_load_image = np.asarray(load_image)
    np_load_image = Image.fromarray(np.uint8(np_load_image))
    render = ImageTk.PhotoImage(np_load_image)
    img = Label(app, image=render)
    img.image = render
    img.place(x=20, y=50)


def encrypt_data_into_image():
    data = txt.get(1.0, "end-1c")
    img = cv2.imread(path_image)
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = img.shape
    PixReq = len(data) * 3
    RowReq = PixReq/width
    RowReq = math.ceil(RowReq)
    count = 0
    charCount = 0
    for i in range(RowReq + 1):
        while count < width and charCount < len(data):
            char = data[charCount]
            charCount += 1
            for index_k, k in enumerate(char):
                if (k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1):
                    img[i][count][index_k % 3] -= 1
                if index_k % 3 == 2:
                    count += 1
                if index_k == 7:
                    if (charCount*3 < PixReq and img[i][count][2] % 2 == 1) or (charCount*3 >= PixReq and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0
    cv2.imwrite("image.png", img)
    success_label = Label(app, text="Encryption Successful!", bg='#eb5e49', font=("Times New Roman", 20))
    success_label.place(x=160, y=300)

app = Tk()
app.configure(background='#98ff96')
app.title("Encrypt")
app.geometry('600x600')
on_click_button = Button(app, text="Choose Image", bg='white', fg='black', command=on_click)
on_click_button.place(x=250, y=10)
txt = Text(app, wrap=WORD, width=30)
txt.place(x=340, y=55, height=165)
encrypt_button = Button(app, text="Encode", bg='white', fg='black', command=encrypt_data_into_image)
encrypt_button.place(x=435, y=230)
app.mainloop()


def decrypt():
    load = Image.open("./image.png")
    load.thumbnail(image_display_size, Image.ANTIALIAS)
    load = np.asarray(load)
    load = Image.fromarray(np.uint8(load))
    render = ImageTk.PhotoImage(load)
    img = Label(app, image=render)
    img.image = render
    img.place(x=100, y=50)

    img = cv2.imread("image.png")
    data = []
    stop = False
    for index_i, i in enumerate(img):
        i.tolist()
        for index_j, j in enumerate(i):
            if index_j % 3 == 2:
                data.append(bin(j[0])[-1])
                data.append(bin(j[1])[-1])
                if bin(j[2])[-1] == '1':
                    stop = True
                    break
            else:
                data.append(bin(j[0])[-1])
                data.append(bin(j[1])[-1])
                data.append(bin(j[2])[-1])
        if stop:
            break

    message = []
    for i in range(int((len(data)+1)/8)):
        message.append(data[i*8:(i*8+8)])
    message = [chr(int(''.join(i), 2)) for i in message]
    message = ''.join(message)
    message_label = Label(app, text=message, bg='white', font=("Times New Roman", 15))
    message_label.place(x=30, y=400)


app = Tk()
app.configure(background='#fa7878')
app.title("Decrypt")
app.geometry('600x600')
main_button = Button(app, text="Start Program", bg='white', fg='black', command=decrypt)
main_button.place(x=250, y=10)
app.mainloop()