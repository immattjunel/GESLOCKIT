import tkinter as tk
import re
import tkinter.messagebox
from PIL import ImageTk, Image
import socket



#initialize
class Geslockit(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry()
        self.attributes('-fullscreen', True)
        self.iconbitmap('logo.ico')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, Signin, EnterPin, UI, Gesture,Manageacct,userpage,pinpage,changepin, changeemail, accounts, UIuser):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#Startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        def connected():
            REMOTE_SERVER = "www.google.com"
            try:
                host = socket.gethostbyname(REMOTE_SERVER)
                s = socket.create_connection((host, 80), 2)
                controller.show_frame(Signin)
                return True
            except:
                tkinter.messagebox.showinfo("Connection", "Internet Connection Needed")


        tk.Frame.__init__(self, parent)
        path = 'title.png'
        img = Image.open(path)
        img==img.resize((850, 200), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img)
        label1 = tk.Button(self,text="wew", command=connected, image=self.photoImg)
        label1.pack(fill="both", expand="yes")
        if connected==0:
            app.messagebox("info","No Internet Connection")

class Signin(tk.Frame):

    def __init__(self, parent, controller):
        def validateemail():
            content = email2.get()

            if re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", content):
                    controller.show_frame(EnterPin)
            else:
                tkinter.messagebox.showinfo("Invalid Syntax","Invalid Email format")

        tk.Frame.__init__(self, parent)
        self.configure(background='#eff0f1')
        path = 'bg2.png'
        img = Image.open(path)
        self.photoImg = ImageTk.PhotoImage(img)
        label2 = tk.Label(self, image=self.photoImg)
        label2.pack(fill='both', expand='yes')

        # geslockitlabel
        path1 = 'geslockit.png'
        img1 = Image.open(path1)
        img1=img1.resize((850, 200), Image.ANTIALIAS)
        self.pi = ImageTk.PhotoImage(img1)
        label1 = tk.Label(self, image=self.pi, font=("Slant", 110), bg='#eff0f1', fg='#e67e22')
        label1.place(relx=.001,rely=.001,anchor='nw')

        email1 = tk.Label(self, text='E-mail:', font=("slant", 40), bg="#eff0f1", fg="#404040")
        email1.place(relx=0.26, rely=0.4, anchor='center')

        email2 = tk.Entry(self, font=("Segou UI", 38))
        email2.focus()
        email2.place(relx=0.38, rely=0.5, anchor='center')

        button = tk.Button(self, text="Proceed", fg="white", bg="#2D2D2D", font=("slant", 40), relief='flat', cursor="heart", width=10,command=validateemail)
        button.place(relx=0.52, rely=0.8, anchor='center')


class EnterPin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#eff0f1')
        def enter():
                    controller.show_frame(UI)
                    text1.delete(0, 'end')
                  
        label1 = tk.Label(self, text="Enter PIN", font=("Slant", 90), bg='#eff0f1', fg='#e67e22')
        label1.pack()
        frame4 = tk.Frame(self)
        frame4.pack(side='bottom')
        # bclear
        path10 = r'clear.png'
        img10 = Image.open(path10)
        img10 = img10.resize((550, 150), Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        button10 = tk.Button(frame4, image=self.photoImg10, relief='flat', command=lambda: text1.delete(0, 'end'))
        button10.pack(side='left')
        # b0
        path11 = r'0.png'
        img11 = Image.open(path11)
        img11 = img11.resize((550, 150), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        button11 = tk.Button(frame4, image=self.photoImg11, relief='flat', command=lambda: text1.insert('end', '0') if len(text1.get())!= 4 else Exception)
        button11.pack(side='left')
        # benter
        path12 = r'enter.png'
        img12 = Image.open(path12)
        img12 = img12.resize((550, 150), Image.ANTIALIAS)
        self.photoImg12 = ImageTk.PhotoImage(img12)
        button12 = tk.Button(frame4, image=self.photoImg12, relief='flat', command=enter)
        button12.pack(side='left')

        frame3 = tk.Frame(self)
        frame3.pack(side='bottom')
        # b7
        path7 = r'7.png'
        img7 = Image.open(path7)
        img7 = img7.resize((550, 150), Image.ANTIALIAS)
        self.photoImg7 = ImageTk.PhotoImage(img7)
        button7 = tk.Button(frame3, image=self.photoImg7, relief='flat', command=lambda: text1.insert('end', '7') if len(text1.get())!= 4 else Exception)
        button7.pack(side='left')
        # b8
        path8 = r'8.png'
        img8 = Image.open(path8)
        img8 = img8.resize((550, 150), Image.ANTIALIAS)
        self.photoImg8 = ImageTk.PhotoImage(img8)
        button8 = tk.Button(frame3, image=self.photoImg8, relief='flat', command=lambda: text1.insert('end', '8') if len(text1.get())!= 4 else Exception)
        button8.pack(side='left')
        # b9
        path9 = r'9.png'
        img9 = Image.open(path9)
        img9 = img9.resize((550, 150), Image.ANTIALIAS)
        self.photoImg9 = ImageTk.PhotoImage(img9)
        button9 = tk.Button(frame3, image=self.photoImg9, relief='flat', command=lambda: text1.insert('end', '9') if len(text1.get())!= 4 else Exception)
        button9.pack(side='left')

        frame2 = tk.Frame(self)
        frame2.pack(side='bottom')
        # b4
        path4 = r'4.png'
        img4 = Image.open(path4)
        img4 = img4.resize((550, 150), Image.ANTIALIAS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        button4 = tk.Button(frame2, image=self.photoImg4, relief='flat', command=lambda: text1.insert('end', '4') if len(text1.get())!= 4 else Exception)
        button4.pack(side='left')
        # b5
        path5 = r'5.png'
        img5 = Image.open(path5)
        img5 = img5.resize((550, 150), Image.ANTIALIAS)
        self.photoImg5 = ImageTk.PhotoImage(img5)
        button5 = tk.Button(frame2, image=self.photoImg5, relief='flat', command=lambda: text1.insert('end', '5') if len(text1.get())!= 4 else Exception)
        button5.pack(side='left')
        # b6
        path6 = r'6.png'
        img6 = Image.open(path6)
        img6 = img6.resize((550, 150), Image.ANTIALIAS)
        self.photoImg6 = ImageTk.PhotoImage(img6)
        button6 = tk.Button(frame2, image=self.photoImg6, relief='flat', command=lambda: text1.insert('end', '6') if len(text1.get())!= 4 else Exception)
        button6.pack(side='left')

        frame1 = tk.Frame(self)
        frame1.pack(side='bottom')
        # b1
        path1 = r'1.png'
        img1 = Image.open(path1)
        img1 = img1.resize((550, 150), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        button1 = tk.Button(frame1, image=self.photoImg1, relief='flat', command=lambda: text1.insert('end', '1') if len(text1.get())!= 4 else Exception)
        button1.pack(side='left')
        # b2
        path2 = r'2.png'
        img2 = Image.open(path2)
        img2 = img2.resize((550, 150), Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        button2 = tk.Button(frame1, image=self.photoImg2, relief='flat', command=lambda: text1.insert('end', '2') if len(text1.get())!= 4 else Exception)
        button2.pack(side='left')
        # b3
        path3 = r'3.png'
        img3 = Image.open(path3)
        img3 = img3.resize((550, 150), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        button3 = tk.Button(frame1, image=self.photoImg3, relief='flat', command=lambda: text1.insert('end', '3') if len(text1.get())!= 4 else Exception)
        button3.pack(side='left')

        frame5 = tk.Frame(self)
        frame5.place(relx=0.5, rely=0.2, anchor='center')
        text1 = tk.Entry(frame5, relief='flat', font=("Segoe UI", 60), justify='center')
        text1.pack(side='left')
        patharrow = r'arrow.png'
        arrow = Image.open(patharrow)
        self.photoImgarrow = ImageTk.PhotoImage(arrow)
        backspace = tk.Button(frame5, command=lambda:text1.delete(len(text1.get()) - 1), image=self.photoImgarrow, height=110, width=110, bg='#333333',borderwidth=5)
        backspace.pack()


class Gesture(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Button(self,text="NEXT", command=lambda: controller.show_frame(UI))
        label1.pack(fill="both", expand="yes")

class accounts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        framelogo = tk.Frame(self)
        framelogo.pack(side='top')
        pathpic = r'geslockitlogo2.png'
        img = Image.open(pathpic)
        self.photoImg = ImageTk.PhotoImage(img)
        picture = tk.Label(framelogo, image=self.photoImg, background='#eff0f1')
        picture.pack()

        frameuser = tk.Frame(self)
        frameuser.place(relx=0.5, rely=0.6, anchor='center')
        user1 = tk.Button(frameuser, text='Matt', height=3, width=10, font=('Slant', 40), bg='#4c4b4b', fg='white', relief='flat', command=lambda: controller.show_frame(EnterPin))
        user1.pack(side='left')
        user2 = tk.Button(frameuser, text='Admin', height=3, width=10, font=('Slant', 40), bg='#4c4b4b', fg='white', relief='flat', command=lambda: controller.show_frame(EnterPin))
        user2.pack(side='left')
        user3 = tk.Button(frameuser, text='Yvette', height=3, width=10, font=('Slant', 40), bg='#4c4b4b', fg='white', relief='flat', command=lambda: controller.show_frame(EnterPin))
        user3.pack(side='left')
        user4 = tk.Button(frameuser, text='Jasmin', height=3, width=10, font=('Slant', 40), bg='#4c4b4b', fg='white', relief='flat', command=lambda: controller.show_frame(EnterPin))
        user4.pack(side='left')
        user5 = tk.Button(frameuser, text='Angela', height=3, width=10, font=('Slant', 40), bg='#4c4b4b', fg='white', relief='flat', command=lambda: controller.show_frame(EnterPin))
        user5.pack(side='left')


class UIuser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background
        path = 'bg2.png'
        img = Image.open(path)
        self.photoImg = ImageTk.PhotoImage(img)
        label2 = tk.Label(self, image=self.photoImg)
        label2.pack(fill='both', expand='yes')

        # geslockitlabel
        label1 = tk.Label(self, text="Geslock It", font=("Slant", 110), bg='#eff0f1', fg='#e67e22')
        label1.place(relx=0.01, rely=0.01, anchor='nw')

        # CHANGEGESTURE
        path3 = 'cg.png'
        img3 = Image.open(path3)
        img3 = img3.resize((300, 300), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        button3 = tk.Button(self, relief='flat', image=self.photoImg3)
        button3.place(relx=0.16, rely=0.55, anchor='center')

        # LOCKIT
        path5 = 'li.png'
        img5 = Image.open(path5)
        img5 = img5.resize((300, 300), Image.ANTIALIAS)
        self.photoImg5 = ImageTk.PhotoImage(img5)
        button5 = tk.Button(self, relief='flat', image=self.photoImg5, command=lambda: controller.show_frame(accounts))
        button5.place(relx=0.345, rely=0.55, anchor='center')


class UI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        path = 'bg2.png'
        img = Image.open(path)
        self.photoImg = ImageTk.PhotoImage(img)
        label2 = tk.Label(self, image=self.photoImg)
        label2.pack(fill='both', expand='yes')
        # geslockitlabel
        label1 = tk.Label(self, text="Geslock It", font=("Slant", 110), width=10, bg='#eff0f1', fg='#e67e22')
        label1.place(relx=0.01, rely=0.01, anchor='nw')
        # MANAGEACCOUNTBUTTON
        path1 = 'qwe.png'
        img1 = Image.open(path1)
        img1 = img1.resize((250, 250), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        button1 = tk.Button(self, relief='flat', image=self.photoImg1,command=lambda: controller.show_frame(Manageacct))
        button1.place(relx=0.1, rely=0.35, anchor='center')
        # CHANGEPIN
        path2 = 'cp.png'
        img2 = Image.open(path2)
        img2 = img2.resize((250, 250), Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        button2 = tk.Button(self, relief='flat', image=self.photoImg2, command=lambda: controller.show_frame(changepin))
        button2.place(relx=0.1, rely=0.7, anchor='center')
        # CHANGEGESTURE
        path3 = 'cg.png'
        img3 = Image.open(path3)
        img3 = img3.resize((250, 250), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        button3 = tk.Button(self, relief='flat', image=self.photoImg3)
        button3.place(relx=0.3, rely=0.7, anchor='center')
        # EMAIL
        path4 = 'e.png'
        img4 = Image.open(path4)
        img4 = img4.resize((250, 250), Image.ANTIALIAS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        button4 = tk.Button(self, relief='flat', image=self.photoImg4, command=lambda: controller.show_frame(changeemail))
        button4.place(relx=0.3, rely=0.35, anchor='center')
        # LOCKIT
        path5 = 'li.png'
        img5 = Image.open(path5)
        img5 = img5.resize((250, 250), Image.ANTIALIAS)
        self.photoImg5 = ImageTk.PhotoImage(img5)
        button5 = tk.Button(self, relief='flat', image=self.photoImg5, command=lambda: controller.show_frame(accounts))
        button5.place(relx=0.50, rely=0.55, anchor='center')

class Manageacct(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#eff0f1')

        left = tk.Label(self, text="Manage Users", font=("Slant", 70), bg='#eff0f1', fg='#e67e22')
        left.place(relx=0.24, rely=0.01)

        # panel manage acct

        m1 = tk.PanedWindow(self, orient='vertical', borderwidth=0, relief='flat', bg='#434343')
        m1.place(relx=0.0001, rely=0.0001)

        pin = tk.Button(m1, text="Pin", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20), command=lambda: controller.show_frame(pinpage))
        m1.add(pin)

        u1 = tk.Button(m1, text="User 1", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20),command=lambda: controller.show_frame(userpage))
        u1.place()
        m1.add(u1)

        u2 = tk.Button(m1, text="User 2", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20),command=lambda: controller.show_frame(userpage))
        u2.place()
        m1.add(u2)

        u3 = tk.Button(m1, text="User 3", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20), command=lambda: controller.show_frame(userpage))
        u3.place()
        m1.add(u3)

        add1 = tk.Button(m1, text="Add", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20), command=lambda: controller.show_frame(userpage))
        add1.pack(side='bottom')
        m1.add(add1)

        l4 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=7, font=("slant", 20))
        l4.place()
        m1.add(l4)

        l3 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=1, font=("slant", 20))
        l3.place()
        m1.add(l3)

        l1 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=6, font=("slant", 20))
        l1.place()
        m1.add(l1)

        l2 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=5, font=("slant", 20))
        l2.place()
        m1.add(l2)

        back = tk.Button(m1, text="Back", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20), command=lambda: controller.show_frame(UI))
        back.place()
        m1.add(back)

        l22 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=1, font=("slant", 20))
        l22.place()
        m1.add(l22)

class userpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#eff0f1')
        left = tk.Label(self, text="Manage User", font=("Slant", 70), bg='#eff0f1', fg='#e67e22')
        left.place(relx=0.24, rely=0.01)

        # panel manage acct

        m1 = tk.PanedWindow(self, orient='vertical', borderwidth=0, relief='flat', bg='#434343')
        m1.place(relx=0.0001, rely=0.0001)

        pin = tk.Button(m1, text="Pin", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20), command=lambda: controller.show_frame(pinpage))
        m1.add(pin)

        u1 = tk.Button(m1, text="User 1", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20))
        u1.place()
        m1.add(u1)

        u2 = tk.Button(m1, text="User 2", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20))
        u2.place()
        m1.add(u2)

        u3 = tk.Button(m1, text="User 3", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20))
        u3.place()
        m1.add(u3)

        add1 = tk.Button(m1, text="Add", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20))
        add1.pack(side='bottom')
        m1.add(add1)

        l4 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=7, font=("slant", 20))
        l4.place()
        m1.add(l4)

        l3 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=1, font=("slant", 20))
        l3.place()
        m1.add(l3)

        l1 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=6, font=("slant", 20))
        l1.place()
        m1.add(l1)

        l2 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=5, font=("slant", 20))
        l2.place()
        m1.add(l2)

        back = tk.Button(m1, text="Back", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20),command=lambda: controller.show_frame(UI))
        back.place()
        m1.add(back)

        l22 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=1, font=("slant", 20))
        l22.place()
        m1.add(l22)

        # PANEL 2 CONTENT

        m2 = tk.PanedWindow(self, orient='vertical', borderwidth=0, relief='flat', bg='#eff0f1', width=400, height=600)
        m2.place(relx=0.3, rely=0.2)

        acctName = tk.Label(m2, text="Account Name: ", fg="black", bg='#eff0f1', width=7, height=2, font=("slant", 25))
        acctName.place()
        m2.add(acctName)

        gesture = tk.Label(m2, text="         Gesture: ", fg="black", bg='#eff0f1', width=7, height=2, font=("slant", 25))
        gesture.place()
        m2.add(gesture)

        l22 = tk.Label(m2, text="", fg="white", bg="#eff0f1", width=25, height=1, font=("slant", 20))
        l22.place()
        m2.add(l22)


        # ENTRY PANEL RIGHT SIDE

        m4 = tk.PanedWindow(self, orient='vertical', borderwidth=0, bg="#404040", width=400, height=50)
        m4.place(relx=0.5, rely=0.2)

        acctE = tk.Entry(m4, font=("slant", 38))
        acctE.focus()
        acctE.place()
        m4.add(acctE)

        m6 = tk.PanedWindow(self, orient='vertical', borderwidth=0, bg="#404040", width=400, height=200)
        m6.place(relx=0.5, rely=0.3)

        gesture = tk.Entry(m6, font=("slant", 38))
        gesture.place()
        m6.add(gesture)


        # panel 8 BOTTOM

        m8 = tk.PanedWindow(self, orient='vertical', borderwidth=0, relief='flat', bg="#404040")
        m8.place(relx=0.40, rely=0.9)

        u5 = tk.Button(m8, text="Delete", fg="white", bg="#2D2D2D", relief='flat', width=25, height=2, font=("slant", 20))
        u5.place(relx=0.40, rely=0.9)
        m8.add(u5)

        # panel 9 BOTTOM

        m9 = tk.PanedWindow(self, orient='vertical', borderwidth=0, relief='flat', bg="#404040")
        m9.place(relx=0.65, rely=0.9)

        u5 = tk.Button(m9, text="Save", fg="white", bg="#2D2D2D", relief='flat', width=25, height=2, font=("slant", 20))
        u5.place(relx=0.40, rely=0.9)
        m9.add(u5)

class pinpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#eff0f1')
        left = tk.Label(self, text="Change Pin", font=("Slant", 70), bg='#eff0f1', fg='#e67e22')
        left.place(relx=0.24, rely=0.01)

        # panel manage acct

        m1 = tk.PanedWindow(self, orient='vertical', borderwidth=0, relief='flat', bg='#434343')
        m1.place(relx=0.0001, rely=0.0001,anchor='nw')

        pin = tk.Button(m1, text="Pin", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20))
        m1.add(pin)

        u1 = tk.Button(m1, text="User 1", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20), command=lambda: controller.show_frame(userpage))
        u1.place()
        m1.add(u1)

        u2 = tk.Button(m1, text="User 2", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20), command=lambda: controller.show_frame(userpage))
        u2.place()
        m1.add(u2)

        u3 = tk.Button(m1, text="User 3", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20), command=lambda: controller.show_frame(userpage))
        u3.place()
        m1.add(u3)

        add1 = tk.Button(m1, text="Add", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20))
        add1.pack(side='bottom')
        m1.add(add1)

        l4 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=7, font=("slant", 20))
        l4.place()
        m1.add(l4)

        l3 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=1, font=("slant", 20))
        l3.place()
        m1.add(l3)

        l1 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=6, font=("slant", 20))
        l1.place()
        m1.add(l1)

        l2 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=5, font=("slant", 20))
        l2.place()
        m1.add(l2)

        back = tk.Button(m1, text="Back", fg="white", bg="#2D2D2D", width=25, height=2, relief='flat', font=("slant", 20), command=lambda: controller.show_frame(UI))
        back.place()
        m1.add(back)

        l22 = tk.Label(m1, text="", fg="white", bg="#434343", width=25, height=1, font=("slant", 20))
        l22.place()
        m1.add(l22)

        # PANEL 2 CONTENT

        m2 = tk.PanedWindow(self, orient='vertical', borderwidth=0, relief='flat', bg='#eff0f1', width=400, height=600)
        m2.place(relx=0.3, rely=0.2)

        oldp = tk.Label(m2, text="   Old Pin: ", fg="black", bg='#eff0f1', width=7, height=2, font=("slant", 25))
        oldp.place()
        m2.add(oldp)

        newp = tk.Label(m2, text="  New Pin: ", fg="black", bg='#eff0f1', width=7, height=2, font=("slant", 25))
        newp.place()
        m2.add(newp)

        con = tk.Label(m2, text="Confirm Pin: ", fg="black", bg='#eff0f1', width=7, height=2, font=("slant", 25))
        con.place()
        m2.add(con)

        # ENTRY PANEL RIGHT SIDE

        m4 = tk.PanedWindow(self, orient='vertical', borderwidth=0, bg="#404040", width=400, height=50)
        m4.place(relx=0.5, rely=0.2)

        oldp = tk.Entry(m4, font=("slant", 20))
        oldp.focus()
        oldp.place()
        m4.add(oldp)

        m6 = tk.PanedWindow(self, orient='vertical', borderwidth=0, bg="#404040", width=400, height=50)
        m6.place(relx=0.5, rely=0.3)

        newpE = tk.Entry(m6, font=("slant", 20))
        newpE.place()
        m6.add(newpE)

        m7 = tk.PanedWindow(self, orient='vertical', borderwidth=0, bg="#404040", width=400, height=50)
        m7.place(relx=0.5, rely=0.52)

        conpE = tk.Entry(m7, font=("slant", 20))
        conpE.place()
        m7.add(conpE)

        # panel 8 BOTTOM

        m8 = tk.PanedWindow(self, orient='vertical', borderwidth=0, relief='flat', bg="#404040")
        m8.place(relx=0.40, rely=0.9)

        u5 = tk.Button(m8, text="Delete", fg="white", bg="#2D2D2D", relief='flat', width=25, height=2, font=("slant", 20))
        u5.place(relx=0.40, rely=0.9)
        m8.add(u5)

        # panel 9 BOTTOM

        m9 = tk.PanedWindow(self, orient='vertical', borderwidth=0, relief='flat', bg="#404040")
        m9.place(relx=0.65, rely=0.9)

        u5 = tk.Button(m9, text="Save", fg="white", bg="#2D2D2D", relief='flat', width=25, height=2, font=("slant", 20))
        u5.place(relx=0.40, rely=0.9)
        m9.add(u5)


class changepin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#eff0f1')

        def but1():
            if len(text1.get()) != 4:
                text1.insert('end', '1')

        def but2():
            if len(text1.get()) != 4:
                text1.insert('end', '2')

        def but3():
            if len(text1.get()) != 4:
                text1.insert('end', '3')

        def but4():
            if len(text1.get()) != 4:
                text1.insert('end', '4')

        def but5():
            if len(text1.get()) != 4:
                text1.insert('end', '5')

        def but6():
            if len(text1.get()) != 4:
                text1.insert('end', '6')

        def but7():
            if len(text1.get()) != 4:
                text1.insert('end', '7')

        def but8():
            if len(text1.get()) != 4:
                text1.insert('end', '8')

        def but9():
            if len(text1.get()) != 4:
                text1.insert('end', '9')

        def but0():
            if len(text1.get()) != 4:
                text1.insert('end', '0')

        def clear():
            text1.delete(0, 'end')

        def enter():
            if text1.get() == '1234':
                text1.delete(0, 'end')
                text1.insert(0, 'NICE')
                controller.show_frame(UI)

        def backspace():
            text1.delete(len(text1.get()) - 1)

        label1 = tk.Label(self, text="Enter Old PIN", font=("Slant", 90), bg='#eff0f1', fg='#e67e22')
        label1.pack()
        frame4 = tk.Frame(self)
        frame4.pack(side='bottom')
        # bclear
        path10 = r'clear.png'
        img10 = Image.open(path10)
        img10 = img10.resize((550, 150), Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        button10 = tk.Button(frame4, image=self.photoImg10, relief='flat', command=clear)
        button10.pack(side='left')
        # b0
        path11 = r'0.png'
        img11 = Image.open(path11)
        img11 = img11.resize((550, 150), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        button11 = tk.Button(frame4, image=self.photoImg11, relief='flat', command=but0)
        button11.pack(side='left')
        # benter
        path12 = r'enter.png'
        img12 = Image.open(path12)
        img12 = img12.resize((550, 150), Image.ANTIALIAS)
        self.photoImg12 = ImageTk.PhotoImage(img12)

        button12 = tk.Button(frame4, image=self.photoImg12, relief='flat', command=enter)
        button12.pack(side='left')

        frame3 = tk.Frame(self)
        frame3.pack(side='bottom')
        # b7
        path7 = r'7.png'
        img7 = Image.open(path7)
        img7 = img7.resize((550, 150), Image.ANTIALIAS)
        self.photoImg7 = ImageTk.PhotoImage(img7)
        button7 = tk.Button(frame3, image=self.photoImg7, relief='flat', command=but7)
        button7.pack(side='left')
        # b8
        path8 = r'8.png'
        img8 = Image.open(path8)
        img8 = img8.resize((550, 150), Image.ANTIALIAS)
        self.photoImg8 = ImageTk.PhotoImage(img8)
        button8 = tk.Button(frame3, image=self.photoImg8, relief='flat', command=but8)
        button8.pack(side='left')
        # b9
        path9 = r'9.png'
        img9 = Image.open(path9)
        img9 = img9.resize((550, 150), Image.ANTIALIAS)
        self.photoImg9 = ImageTk.PhotoImage(img9)
        button9 = tk.Button(frame3, image=self.photoImg9, relief='flat', command=but9)
        button9.pack(side='left')

        frame2 = tk.Frame(self)
        frame2.pack(side='bottom')
        # b4
        path4 = r'4.png'
        img4 = Image.open(path4)
        img4 = img4.resize((550, 150), Image.ANTIALIAS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        button4 = tk.Button(frame2, image=self.photoImg4, relief='flat', command=but4)
        button4.pack(side='left')
        # b5
        path5 = r'5.png'
        img5 = Image.open(path5)
        img5 = img5.resize((550, 150), Image.ANTIALIAS)
        self.photoImg5 = ImageTk.PhotoImage(img5)
        button5 = tk.Button(frame2, image=self.photoImg5, relief='flat', command=but5)
        button5.pack(side='left')
        # b6
        path6 = r'6.png'
        img6 = Image.open(path6)
        img6 = img6.resize((550, 150), Image.ANTIALIAS)
        self.photoImg6 = ImageTk.PhotoImage(img6)
        button6 = tk.Button(frame2, image=self.photoImg6, relief='flat', command=but6)
        button6.pack(side='left')

        frame1 = tk.Frame(self)
        frame1.pack(side='bottom')
        # b1
        path1 = r'1.png'
        img1 = Image.open(path1)
        img1 = img1.resize((550, 150), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        button1 = tk.Button(frame1, image=self.photoImg1, relief='flat', command=but1)
        button1.pack(side='left')
        # b2
        path2 = r'2.png'
        img2 = Image.open(path2)
        img2 = img2.resize((550, 150), Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        button2 = tk.Button(frame1, image=self.photoImg2, relief='flat', command=but2)
        button2.pack(side='left')
        # b3
        path3 = r'3.png'
        img3 = Image.open(path3)
        img3 = img3.resize((550, 150), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        button3 = tk.Button(frame1, image=self.photoImg3, relief='flat', command=but3)
        button3.pack(side='left')

        frame5 = tk.Frame(self)
        frame5.place(relx=0.5, rely=0.2, anchor='center')
        text1 = tk.Entry(frame5, relief='flat', font=("Segoe UI", 60), justify='center')
        text1.pack(side='left')
        patharrow = r'arrow.png'
        arrow = Image.open(patharrow)
        self.photoImgarrow = ImageTk.PhotoImage(arrow)
        backspace = tk.Button(frame5, command=backspace, image=self.photoImgarrow, height=110, width=110, bg='#333333',
                              borderwidth=5)
        backspace.pack()\

class changeemail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#eff0f1')

        #background
        path = 'bg2.png'
        img = Image.open(path)
        self.photoImg = ImageTk.PhotoImage(img)
        label2 = tk.Label(self, image=self.photoImg)
        label2.pack(fill='both', expand='yes')

        label1 = tk.Label(self, text="Change E-mail", font=("Slant", 70), bg='#eff0f1', fg='#e67e22')
        label1.place(relx=0.001, rely=0.01, anchor='nw')

        email = tk.Label(self, text='       New E-mail:', font=("slant", 35), bg="#eff0f1", fg='#434343', relief='flat')
        email.place(relx=0.1, rely=0.4)

        emailE = tk.Entry(self, font=("slant", 30), width=15)
        emailE.focus()
        emailE.place(relx=0.3, rely=0.4)

        conemail = tk.Label(self, text='Confirm E-mail:', font=("slant", 35), bg="#eff0f1", fg='#434343', relief='flat')
        conemail.place(relx=0.1, rely=0.5)

        conemailE = tk.Entry(self, font=("slant", 30), width=15)
        conemailE.place(relx=0.3, rely=0.5)

        change = tk.Button(self, text='Change', font=("slant", 40), fg="white", bg="#2D2D2D", relief='flat', width = 15)
        change.place(relx=0.20, rely=0.8, anchor='center')

        backbtn = tk.Button(self, text='Back', font=("slant", 40), fg="white", bg="#2D2D2D", relief='flat',  width = 15, command=lambda: controller.show_frame(UI))
        backbtn.place(relx=0.42, rely=0.8, anchor='center')

app = Geslockit()

app.mainloop()
