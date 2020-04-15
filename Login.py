from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import dbconnector


# ==================================================================================================================#
# =============================================== Login module ====================================================#
# ==================================================================================================================#
class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Classification and Traffic Violation Detection System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='powder blue')

        # ============================================= Variables =============================
        self.uname = StringVar()
        self.passd = StringVar()

        # =============================================== All Images ===========================#
        self.bg_icon = ImageTk.PhotoImage(file="images\icon.jpg")
        self.logo_icon = ImageTk.PhotoImage(file="images\icon_user.png")
        # self.pass_icon=ImageTk.PhotoImage(file="")

        # bg_lbl=Label(self.root,image=self.bg_icon).pack()
        title = Label(self.root, text="Vehicle Classification and Traffic Violation Detection System",
                      font=("time new roman", 20, "bold"), bg="RoyalBlue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)

        login_frame = Frame(self.root, bg="white", bd=4)
        login_frame.place(x=450, y=150)

        # =============================================== Labels and Text Fields =========================#
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

        user = self.uname.get()
        pswd = self.passd.get()
        # msg = messagebox.showinfo("login fail", "Please Enter User Name and password")
        if self.uname.get() == "" or self.passd.get() == "":
            msg = messagebox.showerror("Error", "All The Fields are required")
        elif dbconnector.login_check(user, pswd) == 1:
            # self.uname.get() == "Tariq" and self.passd.get() == "12345":
            # messagebox.showinfo("login","You are Wellcome Sir")
            self.NewWindow = Toplevel(self.root)
            self.app = main_window(self.NewWindow)

        else:
            messagebox.showerror("Error", "Invalid User Name or Password")
            self.uname.set("")
            self.passd.set("")
            # self.uname.focus("")

    def reset_login(self):
        self.uname.set("")
        self.passd.set("")


# ==================================================================================================================#
# =============================================== Main Window Design ==============================================#
# ==================================================================================================================#

class main_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Classification and Traffic Violation Detection System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Vehicle Classification and Traffic Violation Detection System",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)

        # ==================================================================================================================#
        # =============================================== Main Menu Frame ====================================================#
        # ==================================================================================================================#
        mBar = Frame(root, relief=RAISED, bd="4")
        mBar.pack()
        mBar.place(x=300, y=75)
        CmdBtn = self.makeCameraMenu(mBar)
        CasBtn = self.makeTrafficRulesMenu(mBar)
        ChkBtn = self.makeVehiclesMenu(mBar)
        RadBtn = self.makeTicketsMenu(mBar)
        NoMenu = self.makeChangePasswordMenu(mBar)

        # ==================================================================================================================#
        # ================================================ Main Window Frame ===========================================#
        # ==================================================================================================================#

        loadingFrame = Frame(root, relief=RAISED, bd="4")
        loadingFrame.pack()
        loadingFrame.place(x=300, y=120)
        loading = Label(loadingFrame, text="Loading Image Here For Processing ...", font=("time new roman", 15, "bold"),
                        bg="white", relief=GROOVE, bd=3, padx=187, pady=200).pack(expand=1, padx=0, pady=0)
        upload = Button(loadingFrame, width=15, text="upload image", font=("time new roman", 14, "bold"),
                        bg="blue").pack(expand=1, side=LEFT, pady=10, padx=20)
        uploadvideo = Button(loadingFrame, width=15, text="upload video", font=("time new roman", 14, "bold"),
                             bg="blue").pack(expand=1, side=RIGHT, pady=10, padx=20)

    # ==================================================================================================================#
    # =================================================== Function submenu Tasks ========================================#
    # ==================================================================================================================#

    def add_camera(self):
        self.NewWindow = Toplevel(self.root)
        self.app = AddCameraWindow(self.NewWindow)

    def edit_camera(self):
        self.NewWindow = Toplevel(self.root)
        self.app = EditCameraWindow(self.NewWindow)

    def search_camera(self):
        self.NewWindow = Toplevel(self.root)
        self.app = SearchCameraWindow(self.NewWindow)

    def delete_camera(self):
        self.NewWindow = Toplevel(self.root)
        self.app = DeleteCameraWindow(self.NewWindow)

    def add_rules(self):
        self.NewWindow = Toplevel(self.root)
        self.app = AddRulesWindow(self.NewWindow)

    def edit_rules(self):
        self.NewWindow = Toplevel(self.root)
        self.app = EditRulesWindow(self.NewWindow)

    def delete_rule(self):
        self.NewWindow = Toplevel(self.root)
        self.app = DeleteRuleWindow(self.NewWindow)

    def add_vehicle(self):
        self.NewWindow = Toplevel(self.root)
        self.app = AddVehicleWindow(self.NewWindow)

    def edit_vehicle(self):
        self.NewWindow = Toplevel(self.root)
        self.app = EditVehicleWindow(self.NewWindow)

    def delete_vehicle(self):
        self.NewWindow = Toplevel(self.root)
        self.app = DeleteVehicleWindow(self.NewWindow)

    def show_ticket(self):
        self.NewWindow = Toplevel(self.root)
        self.app = ShowTicketWindow(self.NewWindow)

    def search_ticket(self):
        self.NewWindow = Toplevel(self.root)
        self.app = SearchTicketWindow(self.NewWindow)

    def change_password(self):
        self.NewWindow = Toplevel(self.root)
        self.app = ChangePasswordWindow(self.NewWindow)

    # ==================================================================================================================#
    # =============================================== Main Menu Function ==============================================#
    # ==================================================================================================================#

    def makeCameraMenu(self, mBar):
        CmdBtn = Menubutton(mBar, text='Camera Detail', width=20, underline=0, activebackground="blue")
        CmdBtn.pack(side=LEFT, padx="2m")
        CmdBtn.menu = Menu(CmdBtn)
        CmdBtn.menu.add_command(label="Add Camera", command=self.add_camera)
        CmdBtn.menu.entryconfig(0, state=DISABLED)
        CmdBtn.menu.add_command(label='Search Camera', underline=0, command=self.search_camera)
        CmdBtn.menu.add_command(label='Delete Camera', underline=0, command=self.delete_camera)
        CmdBtn.menu.add('separator')
        CmdBtn.menu.add_command(label='Quit', underline=0,
                                background='white', activebackground='green')
        CmdBtn['menu'] = CmdBtn.menu
        return CmdBtn

    def makeTrafficRulesMenu(self, mBar):
        CmdBtn = Menubutton(mBar, text='Traffic Rules', width=20, underline=0, activebackground="blue")
        CmdBtn.pack(side=LEFT, padx="2m")
        CmdBtn.menu = Menu(CmdBtn)
        CmdBtn.menu.add_command(label="Add Rule", command=self.add_rules)
        CmdBtn.menu.entryconfig(0, state=DISABLED)
        CmdBtn.menu.add_command(label='Edit Rule', underline=0, command=self.edit_rules)
        CmdBtn.menu.add_command(label='Delete Rule', underline=0, command=self.delete_rule)
        CmdBtn.menu.add('separator')
        CmdBtn.menu.add_command(label='Quit', underline=0,
                                background='white', activebackground='green')
        CmdBtn['menu'] = CmdBtn.menu
        return CmdBtn

    def makeVehiclesMenu(self, mBar):
        CmdBtn = Menubutton(mBar, text='Vehicles Record', width=20, underline=0, activebackground="blue")
        CmdBtn.pack(side=LEFT, padx="2m")
        CmdBtn.menu = Menu(CmdBtn)
        CmdBtn.menu.add_command(label="Add Vehicle Record", command=self.add_vehicle)
        CmdBtn.menu.entryconfig(0, state=DISABLED)
        CmdBtn.menu.add_command(label='Edit Vehicle Record', underline=0, command=self.edit_vehicle)
        CmdBtn.menu.add_command(label='Delete Vehicle Record', underline=0, command=self.delete_vehicle)
        CmdBtn.menu.add('separator')
        CmdBtn.menu.add_command(label='Quit', underline=0,
                                background='white', activebackground='green')
        CmdBtn['menu'] = CmdBtn.menu
        return CmdBtn

    def makeTicketsMenu(self, mBar):
        CmdBtn = Menubutton(mBar, text='Fine Ticket', width=20, underline=0, activebackground="blue")
        CmdBtn.pack(side=LEFT, padx="2m")
        CmdBtn.menu = Menu(CmdBtn)
        CmdBtn.menu.add_command(label="Show Fine Tickets", command=self.show_ticket)
        CmdBtn.menu.entryconfig(0, state=DISABLED)
        CmdBtn.menu.add_command(label='Search Ticket', underline=0, command=self.search_ticket)
        CmdBtn.menu.add('separator')
        CmdBtn.menu.add_command(label='Quit', underline=0,
                                background='white', activebackground='green')
        CmdBtn['menu'] = CmdBtn.menu
        return CmdBtn

    def makeChangePasswordMenu(self, mBar):
        CmdBtn = Menubutton(mBar, text='Change Password', width=20, underline=0, activebackground="blue")
        CmdBtn.pack(side=LEFT, padx="2m")
        CmdBtn.menu = Menu(CmdBtn)
        CmdBtn.menu.add_command(label="Change Password", command=self.change_password)
        CmdBtn.menu.add('separator')
        CmdBtn.menu.add_command(label='Quit', underline=0,
                                background='white', activebackground='green')
        CmdBtn['menu'] = CmdBtn.menu
        return CmdBtn


# ==================================================================================================================#
# =============================================== Submenu Tasks Window Design ====================================================#
# ==================================================================================================================#
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

        self.c_id = StringVar()
        self.c_name = StringVar()
        self.c_loc = StringVar()
        self.x_cord = StringVar()
        self.y_cord = StringVar()

        # ==================================== Labels and Buttons =====================#

        Label(AddCamera_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Camera ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraid_entry = Entry(AddCamera_screen, textvariable=self.c_id, font=("time new roman", 12), relief=GROOVE,
                               bd=5)
        cameraid_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Camera Name*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraname_entry = Entry(AddCamera_screen, textvariable=self.c_name, font=("time new roman", 12),
                                 relief=GROOVE, bd=5)
        cameraname_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Camera Location*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameralocation_entry = Entry(AddCamera_screen, textvariable=self.c_loc, font=("time new roman", 12),
                                     relief=GROOVE, bd=5)
        cameralocation_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="X Coordinate*:", bg="white", font=("time new roman", 13, "bold")).pack()
        xcoordinate_entry = Entry(AddCamera_screen, textvariable=self.x_cord, font=("time new roman", 12),
                                  relief=GROOVE, bd=5)
        xcoordinate_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Label(AddCamera_screen, text="Y Coordinate*:", bg="white", font=("time new roman", 13, "bold")).pack()
        ycoordinate_entry = Entry(AddCamera_screen, textvariable=self.y_cord, font=("time new roman", 12),
                                  relief=GROOVE, bd=5)
        ycoordinate_entry.pack()
        Label(AddCamera_screen, text="", bg="white").pack()
        Button(AddCamera_screen, text="OK", command=self.camera_insert, width=10, height=1, bg="blue").pack()

    def camera_insert(self):

        c_id = self.c_id.get()
        c_name = self.c_name.get()
        c_loc = self.c_loc.get()
        x_cord = self.x_cord.get()
        y_cord = self.y_cord.get()

        if c_id == "" or c_name == "" or c_loc == "" or x_cord == "" or y_cord == "":
            messagebox.showerror("Error", "All Fields are Required")

        elif dbconnector.add_camera(c_id, c_name, c_loc, x_cord, y_cord) == 1:
            messagebox.showinfo("Sucess", "Record Sucessfully Inserted")


        else:
            messagebox.showerror("Error", "Record Can't be Inserted! Try Again")


class EditCameraWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Camera Detail")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Add Camera Detail",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        EditCamera_screen = Frame(self.root, bg="white", bd=4)
        EditCamera_screen.place(x=550, y=150)
        # ==================================== Labels and Buttons =====================#

        Label(EditCamera_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(EditCamera_screen, text="", bg="white").pack()
        Label(EditCamera_screen, text="Camera ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraid_entry = Entry(EditCamera_screen, textvariable="Camera_id", font=("time new roman", 12), relief=GROOVE,
                               bd=5)
        cameraid_entry.pack()
        Label(EditCamera_screen, text="", bg="white").pack()
        Label(EditCamera_screen, text="Camera Name*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameraname_entry = Entry(EditCamera_screen, textvariable="camera_name", font=("time new roman", 12),
                                 relief=GROOVE, bd=5)
        cameraname_entry.pack()
        Label(EditCamera_screen, text="", bg="white").pack()
        Label(EditCamera_screen, text="Camera Location*:", bg="white", font=("time new roman", 13, "bold")).pack()
        cameralocation_entry = Entry(EditCamera_screen, textvariable="camera_location", font=("time new roman", 12),
                                     relief=GROOVE, bd=5)
        cameralocation_entry.pack()
        Label(EditCamera_screen, text="", bg="white").pack()
        Label(EditCamera_screen, text="X Coordinate*:", bg="white", font=("time new roman", 13, "bold")).pack()
        xcoordinate_entry = Entry(EditCamera_screen, textvariable="x_coordinate", font=("time new roman", 12),
                                  relief=GROOVE, bd=5)
        xcoordinate_entry.pack()
        Label(EditCamera_screen, text="", bg="white").pack()
        Label(EditCamera_screen, text="Y Coordinate*:", bg="white", font=("time new roman", 13, "bold")).pack()
        ycoordinate_entry = Entry(EditCamera_screen, textvariable="y_coordinate", font=("time new roman", 12),
                                  relief=GROOVE, bd=5)
        ycoordinate_entry.pack()
        Label(EditCamera_screen, text="", bg="white").pack()
        Button(EditCamera_screen, text="OK", width=10, height=1, bg="blue").pack()


class SearchCameraWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Search Camera Record")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Search Camera Record",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        Search_Camera_screen = Frame(self.root, bg="white", bd=4)
        Search_Camera_screen.place(x=550, y=150)

        self.c_id = StringVar()
        # ==================================== Label and Buttons ==========================================#

        Label(Search_Camera_screen, text="Please enter ID of the Camera", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(Search_Camera_screen, text="", bg="white").pack()
        Label(Search_Camera_screen, text="Enter Camera ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        Entry(Search_Camera_screen, textvariable=self.c_id,
              font=("time new roman", 12), relief=GROOVE,
              bd=5).pack()

        Label(Search_Camera_screen, text="", bg="white").pack()
        Button(Search_Camera_screen, text="Search", command=self.camera_search, width=15, height=1, bg="blue",
               font=("time new roman", 13, "bold")).pack()
        Label(Search_Camera_screen, text="", bg="white").pack()
        # self.loading = Label(Search_Camera_screen, text="Loading Camera Record Here ...",
        #                 font=("time new roman", 15, "bold"),
        #                 bg="white", relief=GROOVE, bd=3, padx=200, pady=150).pack(expand=1, padx=0, pady=0)




    def camera_search(self):
        c_id = self.c_id.get()

        rows = dbconnector.camera_search(c_id)
        #print(rows)
        scores = Tk()
        scores.title("Camera Details")
        # label = Label(scores, text="High Scores", font=("Arial", 30)).grid(row=0, columnspan=3)
        listbox = Text(scores, width=100)
        listbox.grid(row=2, column=0, columnspan=2)
        listbox.insert(END,
                            "Camera ID \t \t| Name     \t\t |Score \t\t| Location \t\t| X-Coordinate \t\t| Y-Coordinate\n")
        listbox.insert(END, "-------------------------------------------------------------------------------------------")
        listbox.insert(END, "\n")
        #self.loading['text'] = "Data"
        listbox.insert(END, rows[0][0])
        listbox.insert(END, "\t \t|")
        listbox.insert(END, rows[0][1])
        listbox.insert(END, "\t\t|")
        listbox.insert(END, rows[0][2])
        listbox.insert(END, "\t\t|")
        listbox.insert(END, rows[0][3])
        listbox.insert(END, "\t\t|")
        listbox.insert(END, rows[0][4])
        listbox.insert(END, "\t\t|")
        listbox.insert(END, rows[0][4])
        listbox.insert(END, "\n")

class DeleteCameraWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Delete Camera Record")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Delete Camera Record",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        Search_Camera_screen = Frame(self.root, bg="white", bd=4)
        Search_Camera_screen.place(x=500, y=120)

        self.c_id = StringVar()
        # ==================================== Label and Buttons ==========================================#

        Label(Search_Camera_screen, text="Please enter ID of the Camera", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(Search_Camera_screen, text="", bg="white").pack()
        Label(Search_Camera_screen, text="Enter Camera ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        Entry(Search_Camera_screen, textvariable=self.c_id,
              font=("time new roman", 12), relief=GROOVE,
              bd=5).pack()

        Label(Search_Camera_screen, text="", bg="white").pack()
        Button(Search_Camera_screen, text="Delete", command=self.remove_camera, width=15, height=1, bg="blue",
               font=("time new roman", 13, "bold")).pack()

    def remove_camera(self):

        c_id = self.c_id.get()
        if c_id == "":
            messagebox.showerror("Error", "Camera ID Field Can't Be Empty")

        elif dbconnector.delete_camera(c_id) == 1:
            messagebox.showinfo("Sucess", "Record Sucessfully Deleted")


        else:
            messagebox.showerror("Error", "Record Can't be Deleted! Try Again")


class AddRulesWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Rule Detail")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Add Rule Detail",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        AddRules_screen = Frame(self.root, bg="white", bd=4)
        AddRules_screen.place(x=550, y=150)

        self.r_id = StringVar()
        self.r_name = StringVar()
        self.fine = StringVar()
        # ==================================== Labels and Buttons =====================#

        Label(AddRules_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(AddRules_screen, text="", bg="white").pack()
        Label(AddRules_screen, text="Rule ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        rule_id_entry = Entry(AddRules_screen, textvariable=self.r_id, font=("time new roman", 12), relief=GROOVE,
                              bd=5)
        rule_id_entry.pack()
        Label(AddRules_screen, text="", bg="white").pack()
        Label(AddRules_screen, text="Rule Name*:", bg="white", font=("time new roman", 13, "bold")).pack()
        rule_name_entry = Entry(AddRules_screen, textvariable=self.r_name, font=("time new roman", 12), relief=GROOVE,
                                bd=5)
        rule_name_entry.pack()
        Label(AddRules_screen, text="", bg="white").pack()
        Label(AddRules_screen, text="Violation Fine*:", bg="white", font=("time new roman", 13, "bold")).pack()
        violation_fine_entry = Entry(AddRules_screen, textvariable=self.fine, font=("time new roman", 12),
                                     relief=GROOVE, bd=5)
        violation_fine_entry.pack()
        Label(AddRules_screen, text="", bg="white").pack()
        Button(AddRules_screen, text="OK", command=self.rule_insert, width=10, height=1, bg="blue").pack()

    def rule_insert(self):
        r_id = self.r_id.get()
        r_name = self.r_name.get()
        fine = self.fine.get()

        if r_id == "" or r_name == "" or fine == "":
            messagebox.showerror("Error", "All Fields are Required")

        elif dbconnector.add_rule(r_id, r_name, fine) == 1:
            messagebox.showinfo("Sucess", "Record Sucessfully Inserted")

        else:
            messagebox.showerror("Error", "Record Can't be Inserted! Try Again")


class EditRulesWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Edit Traffic Rules")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Edit Traffic Rules",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        EditRules_screen = Frame(self.root, bg="white", bd=4)
        EditRules_screen.place(x=550, y=150)

        self.r_id = StringVar()
        self.r_name = StringVar()
        self.fine = StringVar()

        # ==================================== Labels and Buttons =====================#

        Label(EditRules_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(EditRules_screen, text="", bg="white").pack()
        Label(EditRules_screen, text="Rule ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        self.rule_id_entry = Entry(EditRules_screen, textvariable=self.r_id, font=("time new roman", 12), relief=GROOVE,
                                   bd=5)
        self.rule_id_entry.pack()

        Button(EditRules_screen, text="Search", command=self.fetch_data_rule, width=10, height=1, bg="blue").pack()

        Label(EditRules_screen, text="", bg="white").pack()
        Label(EditRules_screen, text="Rule Name*:", bg="white", font=("time new roman", 13, "bold")).pack()
        rule_name_entry = Entry(EditRules_screen, textvariable=self.r_name, font=("time new roman", 12), relief=GROOVE,
                                bd=5)
        rule_name_entry.pack()
        Label(EditRules_screen, text="", bg="white").pack()
        Label(EditRules_screen, text="Violation Fine*:", bg="white", font=("time new roman", 13, "bold")).pack()
        violation_fine_entry = Entry(EditRules_screen, textvariable=self.fine, font=("time new roman", 12),
                                     relief=GROOVE, bd=5)
        violation_fine_entry.pack()
        Label(EditRules_screen, text="", bg="white").pack()
        Button(EditRules_screen, text="Update", command=self.edit_rule, width=10, height=1, bg="blue").pack()

    def fetch_data_rule(self):
        r_id = self.r_id.get()
        if r_id == "":
            messagebox.showerror("Error", "Rule ID can't be Empty")
        else:
            rows = dbconnector.fetch_rule_edit(r_id)
            self.r_name.set(rows[0][1])
            self.fine.set(rows[0][2])
            self.rule_id_entry.configure(state="disable")

    def edit_rule(self):
        r_id = self.r_id.get()
        r_name = self.r_name.get()
        fine = self.fine.get()

        if r_name == "" or fine == "":
            messagebox.showerror("Error", "All fields are required!")

        elif dbconnector.edit_rule(r_id, r_name, fine) == 1:
            messagebox.showinfo("Sucess", "Record Sucessfully Updated")


        else:
            messagebox.showerror("Error", "Record Can't be Updated! Try Again")


class DeleteRuleWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Delete Rule Record")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Delete Rule Record",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        Delete_Rule_screen = Frame(self.root, bg="white", bd=4)
        Delete_Rule_screen.place(x=500, y=120)

        self.r_id = StringVar()
        # ==================================== Label and Buttons ==========================================#

        Label(Delete_Rule_screen, text="Please enter ID of the Rule", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(Delete_Rule_screen, text="", bg="white").pack()
        Label(Delete_Rule_screen, text="Enter Rule ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        Entry(Delete_Rule_screen, textvariable=self.r_id,
              font=("time new roman", 12), relief=GROOVE,
              bd=5).pack()

        Label(Delete_Rule_screen, text="", bg="white").pack()
        Button(Delete_Rule_screen, text="Delete", command=self.remove_rule, width=15, height=1, bg="blue",
               font=("time new roman", 13, "bold")).pack()

    def remove_rule(self):
        r_id = self.r_id.get()

        if r_id == "":
            messagebox.showerror("Error", "Rule ID Field Can't Be Empty")

        elif dbconnector.delete_rule(r_id) == 1:
            messagebox.showinfo("Sucess", "Record Sucessfully Deleted")


        else:
            messagebox.showerror("Error", "Record Can't be Deleted! Try Again")


class AddVehicleWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Vehicle Detail")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Add Vehicle Detail",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        AddVehicle_screen = Frame(self.root, bg="white", bd=4)
        AddVehicle_screen.place(x=550, y=150)

        self.v_id = StringVar()
        self.v_name = StringVar()
        self.v_color = StringVar()
        self.l_number = StringVar()
        self.owner = StringVar()
        # ==================================== Labels and Buttons =====================#

        Label(AddVehicle_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(AddVehicle_screen, text="", bg="white").pack()
        Label(AddVehicle_screen, text="Vehicle ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        vehicle_id_entry = Entry(AddVehicle_screen, textvariable=self.v_id, font=("time new roman", 12), relief=GROOVE,
                                 bd=5)
        vehicle_id_entry.pack()
        Label(AddVehicle_screen, text="", bg="white").pack()
        Label(AddVehicle_screen, text="Vehicle Name*:", bg="white", font=("time new roman", 13, "bold")).pack()
        vehicle_name_entry = Entry(AddVehicle_screen, textvariable=self.v_name, font=("time new roman", 12),
                                   relief=GROOVE, bd=5)
        vehicle_name_entry.pack()
        Label(AddVehicle_screen, text="", bg="white").pack()
        Label(AddVehicle_screen, text="Vehicle Color*:", bg="white", font=("time new roman", 13, "bold")).pack()
        vehicle_color_entry = Entry(AddVehicle_screen, textvariable=self.v_color, font=("time new roman", 12),
                                    relief=GROOVE, bd=5)
        vehicle_color_entry.pack()
        Label(AddVehicle_screen, text="", bg="white").pack()
        Label(AddVehicle_screen, text="Licence Number*:", bg="white", font=("time new roman", 13, "bold")).pack()
        licence_number_entry = Entry(AddVehicle_screen, textvariable=self.l_number, font=("time new roman", 12),
                                     relief=GROOVE, bd=5)
        licence_number_entry.pack()
        Label(AddVehicle_screen, text="", bg="white").pack()
        Label(AddVehicle_screen, text="Vehicle Owner*:", bg="white", font=("time new roman", 13, "bold")).pack()
        vehicle_owner_entry = Entry(AddVehicle_screen, textvariable=self.owner, font=("time new roman", 12),
                                    relief=GROOVE, bd=5)
        vehicle_owner_entry.pack()
        Label(AddVehicle_screen, text="", bg="white").pack()
        Button(AddVehicle_screen, text="Add Vehicle", command=self.vehicle_insert, width=10, height=1, bg="blue").pack()

    def vehicle_insert(self):
        v_id = self.v_id.get()
        v_name = self.v_name.get()
        v_color = self.v_color.get()
        l_number = self.l_number.get()
        owner = self.owner.get()

        if v_id == "" or v_name == "" or v_color == "" or l_number == "" or owner == "":
            messagebox.showerror("Error", "All Fields are Required")

        elif dbconnector.add_vehicle(v_id, v_name, v_color, l_number, owner) == 1:
            messagebox.showinfo("Sucess", "Record Sucessfully Inserted")

        else:
            messagebox.showerror("Error", "Record Can't be Inserted! Try Again")


class EditVehicleWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Edit Vehicle Record")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Edit Vehicle Record",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        EditVehicle_screen = Frame(self.root, bg="white", bd=4)
        EditVehicle_screen.place(x=550, y=150)

        self.v_id = StringVar()
        self.v_name = StringVar()
        self.v_color = StringVar()
        self.l_nmbr = StringVar()
        self.owner = StringVar()
        # ==================================== Labels and Buttons ================================#

        Label(EditVehicle_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(EditVehicle_screen, text="", bg="white").pack()
        Label(EditVehicle_screen, text="Vehicle ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        self.vehicle_id_entry = Entry(EditVehicle_screen, textvariable=self.v_id, font=("time new roman", 12),
                                      relief=GROOVE,
                                      bd=5)
        self.vehicle_id_entry.pack()

        Button(EditVehicle_screen, text="Search", command=self.fetch_data_vehicle, width=10, height=1, bg="blue").pack()

        Label(EditVehicle_screen, text="", bg="white").pack()
        Label(EditVehicle_screen, text="Vehicle Name*:", bg="white", font=("time new roman", 13, "bold")).pack()
        vehicle_name_entry = Entry(EditVehicle_screen, textvariable=self.v_name, font=("time new roman", 12),
                                   relief=GROOVE, bd=5)
        vehicle_name_entry.pack()
        Label(EditVehicle_screen, text="", bg="white").pack()
        Label(EditVehicle_screen, text="Vehicle Color*:", bg="white", font=("time new roman", 13, "bold")).pack()
        vehicle_color_entry = Entry(EditVehicle_screen, textvariable=self.v_color, font=("time new roman", 12),
                                    relief=GROOVE, bd=5)
        vehicle_color_entry.pack()
        Label(EditVehicle_screen, text="", bg="white").pack()
        Label(EditVehicle_screen, text="Licence Number*:", bg="white", font=("time new roman", 13, "bold")).pack()
        licence_number_entry = Entry(EditVehicle_screen, textvariable=self.l_nmbr, font=("time new roman", 12),
                                     relief=GROOVE, bd=5)
        licence_number_entry.pack()
        Label(EditVehicle_screen, text="", bg="white").pack()
        Label(EditVehicle_screen, text="Vehicle Owner*:", bg="white", font=("time new roman", 13, "bold")).pack()
        vehicle_owner_entry = Entry(EditVehicle_screen, textvariable=self.owner, font=("time new roman", 12),
                                    relief=GROOVE, bd=5)
        vehicle_owner_entry.pack()
        Label(EditVehicle_screen, text="", bg="white").pack()
        Button(EditVehicle_screen, text="Update", command=self.edit_vehicle, width=10, height=1, bg="blue").pack()

    def fetch_data_vehicle(self):
        v_id = self.v_id.get()
        if v_id == "":
            messagebox.showerror("Error", "Vehcile ID can't be empty")
        else:
            rows = dbconnector.fetch_vehicles_edit(v_id)
            self.v_name.set(rows[0][1])
            self.v_color.set(rows[0][2])
            self.l_nmbr.set(rows[0][3])
            self.owner.set(rows[0][4])
            self.vehicle_id_entry.configure(state="disable")

    def edit_vehicle(self):
        v_id = self.v_id.get()
        v_name = self.v_name.get()
        v_color = self.v_color.get()
        l_nmbr = self.l_nmbr.get()
        owner = self.owner.get()

        if v_id == "":
            messagebox.showerror("Error", "All fields are required!")

        elif dbconnector.edit_vehicle(v_id, v_name, v_color, l_nmbr, owner) == 1:
            messagebox.showinfo("Sucess", "Record Sucessfully Updated")


        else:
            messagebox.showerror("Error", "Record Can't be Updated! Try Again")


class DeleteVehicleWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Delete Vehicle Record")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Delete Vehicle Record",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        Delete_Vehicle_screen = Frame(self.root, bg="white", bd=4)
        Delete_Vehicle_screen.place(x=500, y=120)

        self.v_id = StringVar()
        # ==================================== Label and Buttons ==========================================#

        Label(Delete_Vehicle_screen, text="Please enter ID of the Vehicles", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(Delete_Vehicle_screen, text="", bg="white").pack()
        Label(Delete_Vehicle_screen, text="Enter Vehicle ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        Entry(Delete_Vehicle_screen, textvariable=self.v_id,
              font=("time new roman", 12), relief=GROOVE,
              bd=5).pack()

        Label(Delete_Vehicle_screen, text="", bg="white").pack()
        Button(Delete_Vehicle_screen, text="Delete", command=self.remove_vehicle, width=15, height=1, bg="blue",
               font=("time new roman", 13, "bold")).pack()

    def remove_vehicle(self):
        v_id = self.v_id.get()

        if v_id == "":
            messagebox.showerror("Error", "Vehicle ID Field Can't Be Empty")

        elif dbconnector.delete_vehicld(v_id) == 1:
            messagebox.showinfo("Sucess", "Record Sucessfully Deleted")


        else:
            messagebox.showerror("Error", "Record Can't be Deleted! Try Again")


class ShowTicketWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Tickets Record")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Tickets Record",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)

        mBar = Frame(root, relief=RAISED, bd="4")
        mBar.pack()
        mBar.place(x=300, y=75)
        loading = Label(self.root, text="Loading Ticket Record Here ...", font=("time new roman", 15, "bold"),
                        bg="white", relief=GROOVE, bd=3, padx=400, pady=350).pack(expand=1, padx=350, pady=150)


class SearchTicketWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Search Ticket Record")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Search Ticket Record",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        Search_Ticket_screen = Frame(self.root, bg="white", bd=4)
        Search_Ticket_screen.place(x=350, y=85)
        # ==================================== Label and Buttons ==========================================#

        Label(Search_Ticket_screen, text="Please enter ID of the Ticket", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(Search_Ticket_screen, text="", bg="white").pack()
        Label(Search_Ticket_screen, text="Enter Ticket ID*:", bg="white", font=("time new roman", 13, "bold")).pack()
        Entry(Search_Ticket_screen, textvariable="current_password",
              font=("time new roman", 12), relief=GROOVE,
              bd=5).pack()

        Label(Search_Ticket_screen, text="", bg="white").pack()
        Button(Search_Ticket_screen, text="Search", width=15, height=1, bg="blue").pack()
        Label(Search_Ticket_screen, text="", bg="white").pack()
        loading = Label(Search_Ticket_screen, text="Loading Ticket Record Here ...",
                        font=("time new roman", 15, "bold"),
                        bg="white", relief=GROOVE, bd=3, padx=200, pady=150).pack(expand=1, padx=0, pady=0)


class ChangePasswordWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Change Password")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg='powder blue')
        title = Label(self.root, text="Change Password",
                      font=("time new roman", 20, "bold"), bg="blue", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, relheight=0.1)
        change_password_screen = Frame(self.root, bg="white", bd=4)
        change_password_screen.place(x=550, y=150)
        self.c_pass = StringVar()
        self.n_pass = StringVar()
        self.c_n_pass = StringVar()

        # ==================================== Label and Buttons=====================#

        Label(change_password_screen, text="Please enter required details", bg="white",
              font=("time new roman", 18, "bold")).pack()
        Label(change_password_screen, text="", bg="white").pack()
        Label(change_password_screen, text="Current Password*:", bg="white", font=("time new roman", 13, "bold")).pack()
        Current_Password_entry = Entry(change_password_screen, textvariable=self.c_pass,
                                       font=("time new roman", 12), relief=GROOVE,
                                       bd=5)
        Current_Password_entry.pack()
        Label(change_password_screen, text="", bg="white").pack()
        Label(change_password_screen, text="New Password*:", bg="white", font=("time new roman", 13, "bold")).pack()
        New_Password_entry = Entry(change_password_screen, textvariable=self.n_pass, font=("time new roman", 12),
                                   relief=GROOVE,
                                   bd=5)
        New_Password_entry.pack()
        Label(change_password_screen, text="", bg="white").pack()
        Label(change_password_screen, text="Confirm New Password*:", bg="white",
              font=("time new roman", 13, "bold")).pack()
        Conform_Password_entry = Entry(change_password_screen, textvariable=self.c_n_pass,
                                       font=("time new roman", 12),
                                       relief=GROOVE, bd=5)
        Conform_Password_entry.pack()
        Label(change_password_screen, text="", bg="white").pack()
        Button(change_password_screen, text="Change Password", command=self.change_pass, width=15, height=1, bg="blue").pack()

    def change_pass(self):
        c_pass = self.c_pass.get()
        n_pass = self.n_pass.get()
        con_pass = self.c_n_pass.get()

        if n_pass == con_pass:
            if c_pass == "" or n_pass == "" or con_pass == "":
                messagebox.showerror("Error", "All fields are Required!")

            elif dbconnector.change_pass(c_pass, n_pass) == 1:
                messagebox.showinfo("Sucess", "Password Changed")

            else:
                messagebox.showerror("Error", "Password Can't be Changed! Try Again")

        else:
            messagebox.showerror("Error", "New Password and Confirm Password Don't Match!")


root = Tk()
obj = login_system(root)
#SSobj = main_window(root)
root.mainloop()
