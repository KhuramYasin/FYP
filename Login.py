from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Classification and Traffic Violation Detection System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='powder blue')

        # =============================================veriables=============================
        self.uname = StringVar()
        self.passd = StringVar()

        # ===============================================All Images===========================#
        self.bg_icon = ImageTk.PhotoImage(file="images\icon.jpg")
        self.logo_icon = ImageTk.PhotoImage(file="images\icon_user.png")
        # self.pass_icon=ImageTk.PhotoImage(file="")

        # bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title = Label(self.root, text="Vehicle Classification and Traffic Violation Detection System",
                      font=("time new roman", 20, "bold"), bg="RoyalBlue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)

        login_frame = Frame(self.root, bg="white", bd=4)
        login_frame.place(x=450, y=150)

        # ===============================================Lables and Text Fields==================#
        logolbl = Label(login_frame, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)
        lbluser = Label(login_frame, text="User Name:", bg="white", font=("time new roman", 18, "bold")).grid(row=1,
                                                                                                              column=0,
                                                                                                              padx=20,
                                                                                                              pady=10)
        txtuser = Entry(login_frame, bd=5, relief=GROOVE, textvariable=self.uname, font=("", 15)).grid(row=1, column=1,
                                                                                                       padx=20)
        lblpass = Label(login_frame, text="Password :", bg="white", font=("time new roman", 18, "bold")).grid(row=2,
                                                                                                              column=0,
                                                                                                              padx=20,
                                                                                                              pady=10)
        txtpass = Entry(login_frame, bd=5, relief=GROOVE, show='*', textvariable=self.passd, font=("", 15)).grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=20)
        # ===============================================Buttons==================================#
        btn_login = Button(login_frame, text="Reset", width=15, command=self.reset_login,
                           font=("time new roman", 14, "bold"), bg="RoyalBlue").grid(row=3, column=0, padx=10, pady=10)
        btn_reset = Button(login_frame, text="login", width=15, font=("time new roman", 14, "bold"),
                           command=self.login_verify, bg="RoyalBlue").grid(
            row=3, column=1, padx=10, pady=10)

    def login_verify(self):

        # msg = messagebox.showinfo("login fail", "Please Enter User Name and password")
        if self.uname.get() == "" or self.passd.get() == "":
            msg = messagebox.showerror("Error", "All The Fields are required")
        elif self.uname.get() == "Tariq" and self.passd.get() == "12345":
            # messagebox.showinfo("login","You are Wellcome Sir")
            self.NewWindow = Toplevel(self.root)
            self.app = main_window(self.NewWindow)

        else:
            messagebox.showerror("Error", "Invalid User Name or Password")
            self.uname.set("")
            self.passd.set("")
            self.uname.focus()

    def reset_login(self):
        self.uname.set("")
        self.passd.set("")


class AddCameraWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Camera Detail")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Add Camera Detail",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        AddCamera_screen = Frame(self.root, bg="white", bd=4)
        AddCamera_screen.place(x=550, y=150)
        # ====================================Add Camera Labeles and Buttons=====================#

        Label(AddCamera_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Camera ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraid_entry = Entry(AddCamera_screen, textvariable="id", font=("time new roman", 12), relief=GROOVE, bd=5)
        cameraid_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Camera Name*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraname_entry = Entry(AddCamera_screen, textvariable="cameraname", font=("time new roman", 12),
                                 relief=GROOVE, bd=5)
        cameraname_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Camera Location*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameralocation_entry = Entry(AddCamera_screen, textvariable="cameralocation", font=("time new roman", 12),
                                     relief=GROOVE, bd=5)
        cameralocation_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="X Coordinate*:", bg="white", font=("time new roman", 13, "bold")).pack()
        xcoordinate_entry = Entry(AddCamera_screen, textvariable="xcoordinate", font=("time new roman", 12),
                                  relief=GROOVE, bd=5)
        xcoordinate_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Y Coordinate*:", bg="white", font=("time new roman", 13, "bold")).pack()
        ycoordinate_entry = Entry(AddCamera_screen, textvariable="ycoordinate", font=("time new roman", 12),
                                  relief=GROOVE, bd=5)
        ycoordinate_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Button(AddCamera_screen, text="OK", width=10, height=1, bg="blue").pack()


class AddRulesWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Rule Detail")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Add Rule Detail",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        AddCamera_screen = Frame(self.root, bg="white", bd=4)
        AddCamera_screen.place(x=550, y=150)
        # ==================================== Labeles and Buttons=====================#

        Label(AddCamera_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Rule ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraid_entry = Entry(AddCamera_screen, textvariable="rule_id", font=("time new roman", 12), relief=GROOVE,
                               bd=5)
        cameraid_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Rule Name*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraname_entry = Entry(AddCamera_screen, textvariable="rule_name", font=("time new roman", 12), relief=GROOVE,
                                 bd=5)
        cameraname_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Violation Fine*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameralocation_entry = Entry(AddCamera_screen, textvariable="violation_fine", font=("time new roman", 12),
                                     relief=GROOVE, bd=5)
        cameralocation_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Button(AddCamera_screen, text="OK", width=10, height=1, bg="blue").pack()


class AddVehicleWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Vehicle Detail")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Add Vehicle Detail",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        AddCamera_screen = Frame(self.root, bg="white", bd=4)
        AddCamera_screen.place(x=550, y=150)
        # ====================================Add Vehicle Labeles and Buttons=====================#

        Label(AddCamera_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Vehicle ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraid_entry = Entry(AddCamera_screen, textvariable="vehicle_id", font=("time new roman", 12), relief=GROOVE,
                               bd=5)
        cameraid_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Vehicle Name*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraname_entry = Entry(AddCamera_screen, textvariable="vehicle_name", font=("time new roman", 12),
                                 relief=GROOVE, bd=5)
        cameraname_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Vehicle Color*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameralocation_entry = Entry(AddCamera_screen, textvariable="vehicle_color", font=("time new roman", 12),
                                     relief=GROOVE, bd=5)
        cameralocation_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Licence Number*:", bg="white", font=("time new roman", 13, "bold")).pack()
        xcoordinate_entry = Entry(AddCamera_screen, textvariable="licence_number", font=("time new roman", 12),
                                  relief=GROOVE, bd=5)
        xcoordinate_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Vehicle Owner*:", bg="white", font=("time new roman", 13, "bold")).pack()
        ycoordinate_entry = Entry(AddCamera_screen, textvariable="vehicle_owner", font=("time new roman", 12),
                                  relief=GROOVE, bd=5)
        ycoordinate_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Button(AddCamera_screen, text="OK", width=10, height=1, bg="blue").pack()


class main_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Classification and Traffic Violation Detection System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Vehicle Classification and Traffic Violation Detection System",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)

        # ================================main_window Frame================================
        # mainwindow_frame=Frame(self.root,bg="white")
        # mainwindow_frame.place(x=0.5,y=75)
        # logolbl=Label(mainwindow_frame,image=self.logo_icon).grid(row=0,column=0,pady=20)
        # btn_login=Button(mainwindow_frame,text="Login",width=15,font=("time new roman",14,"bold"),bg="blue").grid(row=2, column=1, pady=10)
        # mBar= Frame(root,relief=RAISED,bd="2")
        # mBar.pack(Fill=X)
        mBar = Frame(root, relief=RAISED, bd="4")
        mBar.pack()
        mBar.place(x=300, y=75)
        CmdBtn = self.makeCameraMenu(mBar)
        CasBtn = self.makeTrafficRulesMenu(mBar)
        ChkBtn = self.makeVehiclesMenu(mBar)
        RadBtn = self.makeTicketsMenu(mBar)
        NoMenu = self.makeChangePasswordMenu(mBar)
        loading=Label(self.root, text="Loading Here ...", font=("time new roman", 20, "bold"), bg="white", relief=GROOVE,bd=3,padx=400, pady=350).pack(expand=1, padx=350, pady=150)
        #upload=Button(self.root,width=15, text="upload image",font=("time new roman",14,"bold"),bg="blue").pack(expand=1,side=BOTTOM,pady=600,padx=1000)

        # mBar.tk_menuBar(CmdBtn, CasBtn, ChkBtn, RadBtn, NoMenu)

    def makeCameraMenu(self, mBar):
        CmdBtn = Menubutton(mBar, text='Camera Detail',width=20, underline=0, activebackground="blue" )
        CmdBtn.pack(side=LEFT, padx="2m")
        CmdBtn.menu = Menu(CmdBtn)
        CmdBtn.menu.add_command(label="Add Camera", command=self.add_camer)
        CmdBtn.menu.entryconfig(0, state=DISABLED)
        CmdBtn.menu.add_command(label='Search Camera', underline=0)
        CmdBtn.menu.add_command(label='Delete Camera', underline=0)
        CmdBtn.menu.add('separator')
        CmdBtn.menu.add_command(label='Quit', underline=0,
                                background='white', activebackground='green')
        CmdBtn['menu'] = CmdBtn.menu
        return CmdBtn

    def add_camer(self):
        self.NewWindow = Toplevel(self.root)
        self.app = AddCameraWindow(self.NewWindow)

    def add_rules(self):
        self.NewWindow = Toplevel(self.root)
        self.app = AddRulesWindow(self.NewWindow)

    def add_vehicle(self):
        self.NewWindow = Toplevel(self.root)
        self.app = AddVehicleWindow(self.NewWindow)

    def makeTrafficRulesMenu(self, mBar):
        CmdBtn = Menubutton(mBar, text='Traffic Rules',width=20, underline=0, activebackground="blue")
        CmdBtn.pack(side=LEFT, padx="2m")
        CmdBtn.menu = Menu(CmdBtn)
        CmdBtn.menu.add_command(label="Add Rule", command=self.add_rules)
        CmdBtn.menu.entryconfig(0, state=DISABLED)
        CmdBtn.menu.add_command(label='Edit Rule', underline=0)
        CmdBtn.menu.add_command(label='Delete Rule', underline=0)
        CmdBtn.menu.add('separator')
        CmdBtn.menu.add_command(label='Quit', underline=0,
                                background='white', activebackground='green')
        CmdBtn['menu'] = CmdBtn.menu
        return CmdBtn

    def makeVehiclesMenu(self, mBar):
        CmdBtn = Menubutton(mBar, text='Vehicles Record',width=20, underline=0, activebackground="blue")
        CmdBtn.pack(side=LEFT, padx="2m")
        CmdBtn.menu = Menu(CmdBtn)
        CmdBtn.menu.add_command(label="Add Vehicle Record", command=self.add_vehicle)
        CmdBtn.menu.entryconfig(0, state=DISABLED)
        CmdBtn.menu.add_command(label='Edit Vehicle Record', underline=0)
        CmdBtn.menu.add_command(label='Delete Vehicle Record', underline=0)
        CmdBtn.menu.add('separator')
        CmdBtn.menu.add_command(label='Quit', underline=0,
                                background='white', activebackground='green')
        CmdBtn['menu'] = CmdBtn.menu
        return CmdBtn

    def makeTicketsMenu(self, mBar):
        CmdBtn = Button(mBar, text='Fine Tickets',bd=0, underline=0,width=20, command=self.add_camer, activebackground="blue")
        CmdBtn.pack(side=LEFT, padx="2m")

        # CmdBtn['menu'] = CmdBtn.menu
        # return CmdBtn

    def makeChangePasswordMenu(self, mBar):
        Dummy_button = Menubutton(mBar, text='Change Password',width=20, underline=0, activebackground="blue")
        Dummy_button.pack(side=LEFT, padx='2m')
        # Dummy_button["state"] = DISABLED
        return Dummy_button






root = Tk()
#obj=login_system(root)
obj = main_window(root)
root.mainloop()
