import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import socket

LARGE_FONT = ("Verdana", 12)


class Geslockit(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        path = 'gestlockittitle.png'
        img = Image.open(path)
        self.photoImg = ImageTk.PhotoImage(img)
        label1 = tk.Button(self,text="wew", command=self.next,image=self.photoImg)
        label1.pack(fill="both", expand="yes")

    def next(self):
        REMOTE_SERVER = "www.facebook.com"
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            x = messagebox.showinfo("info", "Internet Connection")
        except:
            pass
            x = messagebox.showinfo("info", "no Internet Connection")


app = Geslockit()
app.attributes('-fullscreen', True)
app.geometry("1366x768")
app.configure(background='#404040')
app.title("Geslock It")
app.mainloop()
