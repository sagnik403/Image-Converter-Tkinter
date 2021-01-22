from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from PIL import Image

# =================================================================================

def convertion():
    u_path = str(t1.get())
    d_path = str(t2.get())
    name = str(t3.get())
    p_type = str(types.get())

    im = Image.open(rf"{t1.get()}")
    im.save(rf"{t2.get()}\{t3.get()}{types.get()}")

def clear():
    t1.delete(0,'end')
    t2.delete(0,'end')
    t3.delete(0,'end')
    types.delete(0,'end')

def brsfnc():
    location = askdirectory()
    if t2.get() != "":
        t2.delete(0,'end')
        t2.insert(0,location)
    else:
        t2.insert(0,location)

def brspic():
    f_loc = askopenfilename()
    if t1.get() !="":
        t1.delete(0,'end')
        t1.insert(0,f_loc)
    else:
        t1.insert(0,f_loc)



# =================================================================================


win = Tk()
win.title("Image Converter")
win.iconbitmap(r"C:\Users\Public\Pictures\Sample Pictures\Treetog-Junior-Monitor-desktop.ico")
win.geometry("900x500")
win.maxsize(900,500)
win.minsize(900,500)
win['bg']="#83a2f2"

heading = Label(win,text="Image Converter",font=("verdana",35,"bold"),bg="#83a2f2",fg="gold")
heading.place(x=150,y=10)

l1 = Label(win,text="Enter The Image Path",font=("verdana",15,"bold")).grid(row=0,column=0,padx=20,pady=120)
t1 = Entry(win,width=25,borderwidth=5,font=(("verdana",15,"bold")))
t1.grid(row=0,column=1,pady=120)

brs = Button(win,text="Browse File",font=("verdan",8,"bold"),borderwidth=5,width=10,command=brspic)
brs.place(x=660,y=120)


l2 = Label(win,text="Enter Saving Path",font=("verdana",15,"bold")).place(x=20,y=200)
t2 = Entry(win,width=25,borderwidth=5,font=(("verdana",15,"bold")))
t2.place(x=293,y=200)

brsbtn = Button(win,text="Browse Folder",font=("verdan",8,"bold"),borderwidth=5,width=14,command=brsfnc)
brsbtn.place(x=660,y=200)

l3 = Label(win,text="Enter Saving Name",font=("verdana",15,"bold")).place(x=20,y=280)
t3 = Entry(win,width=20,borderwidth=5,font=(("verdana",10,"bold")))
t3.place(x=293,y=280)

combo = ttk.Label(win, text="Enter image type",font=("verdana",14,"bold"))
combo.place(x=20,y=360)

types = ttk.Combobox(win,width = 27,font=("verdana",12,"bold"))
types['values']=('.jgp','.png','.ico','.jpeg','.gif')
types.place(x=293,y=360)
types.current()


b1 = Button(win,text="Convert",font=("verdan",12,"bold"),borderwidth=5,width=12,command=convertion)
b1.place(x=730,y=370)

b1 = Button(win,text="Clear",font=("verdan",12,"bold"),borderwidth=5,width=12,command=clear)
b1.place(x=730,y=440)


win.mainloop()