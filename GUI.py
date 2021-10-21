from tkinter import *
from tkinter import filedialog
from tensorflow.keras.models import load_model
from PIL import ImageTk,Image
import numpy as np
import tkinter.font as tkFont


load=Image
root=Tk()
model=load_model('CIFAR-10-MODEL.h5')
def fileDialog():
    filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select A File", filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    global load
    load = Image.open(filename)

    load2=load.resize((300,300))
    render = ImageTk.PhotoImage(load2)
    img = Label(root, image=render)
    img.image = render
    img.place(relx=0.5,
                       rely=0.5,
                       anchor='center')
    # img.place(x=0, y=0)
def predc():
    load10=load.resize((32,32))
    load10=np.array(load10)
    load10=load10.reshape((1,32,32,3))
    pre = model.predict(load10)
    results = {
        0: 'aeroplane',
        1: 'automobile',
        2: 'bird',
        3: 'cat',
        4: 'deer',
        5: 'dog',
        6: 'frog',
        7: 'horse',
        8: 'ship',
        9: 'truck'
    }
    result = np.where(pre[0] == max(pre[0]))  # returns the index of the result / prediction
    x = int(result[0])
    global w
    w.config(text=str(results[x]))

root.title("Python Tkinter Dialog Widget")
root.minsize(640, 400)

Button1 = Button(root,text="upload image", command=fileDialog)
Button1.place(relx=0.20,rely=0.93)

Button2 = Button(root,text="predict result", command=predc)
Button2.place(relx=0.70,rely=0.93)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
w = Label(root, text="result",font=fontStyle)
w.place(relx=0.50,rely=0.90, anchor='n')


root.mainloop()

