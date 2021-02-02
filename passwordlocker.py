import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox as msg
from locker import lock

class passwordlocker():
    def __init__(self):
        self.start = tk.Tk()
        #self.start.wm_overrideredirect(True)
        self.start.title("Password Locker")
        self.start.geometry("700x400+200+200")
        self.start.resizable(0,0)
        self.start.iconbitmap("C:/Users/franklinobasy/Downloads/GUI/photoicons/lock_icon.ico")
        #self.start.attributes("-alpha", 0.5)

        #displays
        self.set_start_display()
        #imported class
        self.lock = lock()
        
    def set_start_display(self):

        #eVENTS
        def enter(event):
            self.proceed.configure(bg = "Green")
        
        def leave(event):
            self.proceed.config(bg = "Light Green")

        #Images
        img = Image.open("C:/Users/franklinobasy/Downloads/GUI/photoicons/lock.png")
        img = img.resize((200,200))
        lock = ImageTk.PhotoImage(img)
        lock_label = tk.Label(self.start, image = lock)
        lock_label.image = lock

        #Text display
        banner = tk.Label(self.start, text = "Password Locker", font = ("monospace",30, "bold") )
        motto =  tk.Label(self.start, text = "...providing maximum security.", font = ("forte",10, "normal") )
        mini = tk.Label(self.start, text = "powered by Franobs", font = ("magneto",10, "bold"))

        #button
        self.proceed = tk.Button(self.start, text = "PROCEED", bd = 0, font = ("Georgia",10, "bold"), bg = "Light Green", fg = "White" )
        self.proceed.config(command = self.next_UI)

        #widget layout
        #------------------------------------------------------------------
        self.proceed.bind("<Enter>", enter) #binding
        self.proceed.bind("<Leave>", leave) #binding
        #------------------------------------------------------------------
        banner.pack(side = tk.TOP, pady = 10)
        lock_label.pack(side = tk.TOP, pady = 10)
        motto.pack(side = tk.TOP, pady = 4)
        mini.pack(side = tk.LEFT)
        self.proceed.pack(side= tk.RIGHT, padx = 5)
    
    def next_UI(self):
        def enter(event):
            self.menu_section.config(width = 120)
            self.a_button.config(text = "Account")
            self.b_button.config(text = "Add New")
            self.c_button.config(text = "View")
            self.d_button.config(text = "View All")
            self.e_button.config(text = "Delete")
            #self.main_section.config(width = 580)
        
        def leave(event):
            self.menu_section.config(width = 70, relief = tk.FLAT)
            self.a_button.config(text = "")
            self.b_button.config(text = "")
            self.c_button.config(text = "")
            self.d_button.config(text = "")
            self.e_button.config(text = "")
            self.main_section.config(width = 630)

        def signin_e(event):
            sign_in.config(bg = "Light Blue", fg = "White")
        def signin_l(event):
            sign_in.config(bg = "White", fg = "Black")
        def signup_e(event):
            sign_up.config(bg = "Light Blue", fg = "White")
        def signup_l(event):
            sign_up.config(bg = "White", fg = "Black")


        self.start.state("withdrawn")
        self._UI = tk.Toplevel(self.start)
        self._UI.title("Password Locker")
        self._UI.geometry("700x400+200+200")
        self._UI.resizable(0,0)
        self._UI.iconbitmap("C:/Users/franklinobasy/Downloads/GUI/photoicons/lock_icon.ico")

        #load all frames
         # text variables
        #-username
        self.username = tk.StringVar()
        #-password
        self.password = tk.StringVar()
        self.frames()
        #Split sections
        self.menu_section = tk.Frame(self._UI, bg = "Grey", width = 70, height = 400, bd = 2)
        self.menu_section.grid_propagate(False)
        self.main_section = tk.Frame(self._UI, width = 630, height = 400)
        self.main_section.pack_propagate(False)

        #menu_frame bind
        self.menu_section.bind("<Enter>", enter)
        self.menu_section.bind("<Leave>", leave)

        #menu_section slave
        #images
        self.img_a = Image.open(r"C:/Users/franklinobasy/Downloads/GUI/photoicons/user.png")
        self.img_a = self.img_a.resize((50,50))
        self.account = ImageTk.PhotoImage(self.img_a)
        self.img_b = Image.open(r"C:/Users/franklinobasy/Downloads/GUI/photoicons/add.png")
        self.img_b = self.img_b.resize((50,50))
        self.account1 = ImageTk.PhotoImage(self.img_b)
        self.img_c = Image.open(r"C:/Users/franklinobasy/Downloads/GUI/photoicons/view.png")
        self.img_c = self.img_c.resize((50,50))
        self.account2 = ImageTk.PhotoImage(self.img_c)
        self.img_d = Image.open(r"C:/Users/franklinobasy/Downloads/GUI/photoicons/viewall.png")
        self.img_d = self.img_d.resize((46,46))
        self.account3 = ImageTk.PhotoImage(self.img_d)
        self.img_e = Image.open(r"C:/Users/franklinobasy/Downloads/GUI/photoicons/delete.png")
        self.img_e = self.img_e.resize((46,46))
        self.account4 = ImageTk.PhotoImage(self.img_e)
        

        self.a_button = tk.Button(self.menu_section,image = self.account, compound = tk.LEFT,
                              bg = "Grey", fg = "White", bd = 0, font = ("courier",9,"bold"))

        self.b_button = tk.Button(self.menu_section,image = self.account1, compound = tk.LEFT,
                              bg = "Grey",state = "disabled", fg = "White", bd = 0, font = ("courier",9,"bold"), command = self.show_addAccountFrame)
        
        self.c_button = tk.Button(self.menu_section,image = self.account2, compound = tk.LEFT,
                              bg = "Grey",state = "disabled", fg = "White", bd = 0, font = ("courier",9,"bold"))

        self.d_button = tk.Button(self.menu_section,image = self.account3, compound = tk.LEFT,
                              bg = "Grey",state = "disabled", fg = "White", bd = 0, font = ("courier",9,"bold"))

        self.e_button = tk.Button(self.menu_section,image = self.account4, compound = tk.LEFT,
                              bg = "Grey",state = "disabled", fg = "White", bd = 0, font = ("courier",9,"bold"))
        #main_section slave
        self.img_b = Image.open(r"C:/Users/franklinobasy/Downloads/GUI/photoicons/key.png")
        self.img_b = self.img_b.resize((200,200))
        self._account = ImageTk.PhotoImage(self.img_b)
        label_image = tk.Label(self.main_section, image = self._account)

        #buttons
        sign_in = tk.Button(self.main_section, command = self.Sign_In_window, text ="SIGN-IN", bd = 0, bg = "White", font = ("msoutlook", 12, "bold"))
        sign_up = tk.Button(self.main_section, command = self.Sign_Up_window, text ="SIGN-UP", bd = 0, bg = "White", font = ("msoutlook", 12, "bold"))
        #____bind buttons____
        sign_in.bind("<Enter>", signin_e)
        sign_in.bind("<Leave>", signin_l)
        sign_up.bind("<Enter>", signup_e)
        sign_up.bind("<Leave>", signup_l)


        #Widget Layout
        self.menu_section.pack(side = tk.LEFT)
        self.main_section.pack(side = tk.LEFT)
        self.a_button.grid(row = 0, column = 0, sticky = tk.W, padx = 5, pady = 7)
        self.b_button.grid(row = 1, column = 0, sticky = tk.W, padx = 5, pady = 7)
        self.c_button.grid(row = 2, column = 0, sticky = tk.W, padx = 5, pady = 7)
        self.d_button.grid(row = 3, column = 0, sticky = tk.W, padx = 5, pady = 7)
        self.e_button.grid(row = 4, column = 0, sticky = tk.W, padx = 5, pady = 7)
        


        label_image.pack(side = tk.TOP, padx = 180, pady = [2,10])
        sign_in.pack(side= tk.LEFT, padx = [210,1])
        sign_up.pack(side= tk.RIGHT, padx = [1,210])
    
    def Sign_In_window(self):
        self.InWindow = tk.Toplevel(self._UI)
        self.InWindow.grab_set()        #helps to grab all event
        self.InWindow.geometry("250x270+470+300")
        self.InWindow.wm_overrideredirect(True)
        self.InWindow.lift(self._UI)
        self.InWindow.config(bg = "Light Blue")
        val = tk.IntVar()
        val.set(0)

       

        #functions
        def enter_exit_signin(event):
            img_button.config(image = self.b_)
        def leave_exit_signin(event):
            img_button.config(image = self.a_)
        def enter_signin(event):
            signinButton.config(image = self.d_)
        def leave_signin(event):
            signinButton.config(image = self.c_)
        
        def _signSucess():
            check = self.lock.sign_in(self.username.get(),self.password.get())
            if check == True:
                msg.showinfo("Sign-In Successful", "Welcome to Password Locker")
                self.InWindow.destroy()
                self.a_button.config(state = "normal")
                self.b_button.config(state = "normal")
                self.c_button.config(state = "normal")
                self.d_button.config(state = "normal")
                self.e_button.config(state = "normal")
                self.user_text.config(text = "Welcome "+self.username.get())
                self.main_section.pack_forget()
                self.user_frame.pack()
                

            elif check == False:
                msg.showinfo("Sign-In Failed!", "Incorrect Username or password")

        def show_pw():
            #global pw, val
            #a = pw.get()
            b = val.get()
            if b == 0:
                pEntry.config(show = "*")
            elif b == 1:
                pEntry.config(show = "")

           
        #Images
        self.a = Image.open("C:/Users/franklinobasy/Downloads/GUI/photoicons/e.png")
        self.a = self.a.resize((25,25))
        self.b = Image.open("C:/Users/franklinobasy/Downloads/GUI/photoicons/ea.png")
        self.b = self.b.resize((25,25))
        self.c = Image.open("C:/Users/franklinobasy/Downloads/GUI/photoicons/go2.png")
        self.c = self.c.resize(((40,40)))
        self.d = Image.open("C:/Users/franklinobasy/Downloads/GUI/photoicons/go1.png")
        self.d = self.d.resize(((40,40)))
        self.a_ = ImageTk.PhotoImage(self.a)
        self.b_ = ImageTk.PhotoImage(self.b)
        self.c_ = ImageTk.PhotoImage(self.c)
        self.d_ = ImageTk.PhotoImage(self.d)

        #widgets
        
        layer = tk.Canvas(self.InWindow, width =240, height = 260, bg = 'Gray')
    

        img_button = tk.Button(layer, image = self.a_ , bg = "Gray", bd = 0, command = self.exit_signin)
        signinButton = tk.Button(layer, image = self.c_ , bg = "Grey", bd = 0, command = _signSucess)
        showpw = tk.Checkbutton(layer, text = "show password",bd =0, variable = val, bg = "Gray", command = show_pw, font = ("lucidasans",8,"italic") )
        showpw.deselect()

        sLabel = tk.Label(layer, text = "Sign-In", fg ="White", bg ="Gray", font =("lucidasans",12,"bold"))
        uLabel = tk.Label(layer, text = "Username : ", bg = "Grey", fg = "White", font =("lucidasans",10,"bold") )
        self.uEntry = tk.Entry(layer, bg = "Grey", fg = "White",textvariable =self.username, font = ("Consolas",9,"normal"), width =23, bd = 0, justify = tk.CENTER)
        self.uEntry.focus()
        pEntry = tk.Entry(layer, bg = "Grey", fg = "White", show = "*", textvariable = self.password, font = ("Consolas",9,"normal"), width =23, bd = 0, justify = tk.CENTER )
        pLabel = tk.Label(layer, text = "Password : ", bg = "Grey", fg = "White", font =("lucidasans",10,"bold") )
        
        #binding
        img_button.bind("<Enter>", enter_exit_signin)
        img_button.bind("<Leave>", leave_exit_signin)
        signinButton.bind("<Enter>", enter_signin)
        signinButton.bind("<Leave>", leave_signin)

        #widget layout
        layer.pack()
        layer.create_line(80,36,160,36, fill = "white")
        layer.create_line(40,125,200,125, fill = "Green")
        layer.create_line(40,183,200,183, fill = "Green")
        img_button.place(x = 210, y = 5)
        sLabel.place(x = 90, y =5)
        
        uLabel.place(x = 90, y = 80)
        self.uEntry.place(x = 40, y = 105)
        pLabel.place(x = 90, y = 138)
        pEntry.place(x = 40, y = 165)
        showpw.place(x = 40, y =184)

        signinButton.place(x = 100, y = 220)

    def Sign_Up_window(self):
        self.UpWindow = tk.Toplevel(self._UI)
        self.UpWindow.grab_set()        #helps to grab all event
        self.UpWindow.geometry("250x320+470+300")
        self.UpWindow.wm_overrideredirect(True)
        self.UpWindow.lift(self._UI)
        self.UpWindow.config(bg = "Light Blue")
        val = tk.IntVar()
        val.set(0)

        # text variables
        #-username
        self.username = tk.StringVar()
        self.username.set("")
        #-password
        self.password = tk.StringVar()
        self.password.set("")
        self.password1 = tk.StringVar()
        self.password1.set("")
        

        #functions
        def enter_exit_signin(event):
            img_button.config(image = self.b_)
        def leave_exit_signin(event):
            img_button.config(image = self.a_)
        def enter_signin(event):
            signupButton.config(image = self.d_)
        def leave_signin(event):
            signupButton.config(image = self.c_)

        def _signUpSucess():
            a = self.username.get()
            b = self.password.get()
            c = self.password1.get()

            if a == "" or b == "" or c == "":
                msg.showinfo("Empty Field", "Some or all of the field are empty")
            else:
                check = self.lock.sign_up(a, b, c)
                if check == True:
                    msg.showinfo("Sign-Up Successful", "Welcome to Password Locker\nClick Sign-in Button to login")
                    self.UpWindow.destroy()
                    #self.UpWindow.config(state = "normal")
                elif check == False:
                    msg.showinfo("Sign-Up Failed!", "Incorrect Username or password\nOr\nPassword mis-match")



        def show_pw():
            #global pw, val
            #a = pw.get()
            b = val.get()
            if b == 0:
                pEntry1.config(show = "*")
                pEntry2.config(show = "*")
            elif b == 1:
                pEntry1.config(show = "")
                pEntry2.config(show = "")
            

        
        #Images
        self.a = Image.open("C:/Users/franklinobasy/Downloads/GUI/photoicons/e.png")
        self.a = self.a.resize((25,25))
        self.b = Image.open("C:/Users/franklinobasy/Downloads/GUI/photoicons/ea.png")
        self.b = self.b.resize((25,25))
        self.c = Image.open("C:/Users/franklinobasy/Downloads/GUI/photoicons/go2.png")
        self.c = self.c.resize(((40,40)))
        self.d = Image.open("C:/Users/franklinobasy/Downloads/GUI/photoicons/go1.png")
        self.d = self.d.resize(((40,40)))
        self.a_ = ImageTk.PhotoImage(self.a)
        self.b_ = ImageTk.PhotoImage(self.b)
        self.c_ = ImageTk.PhotoImage(self.c)
        self.d_ = ImageTk.PhotoImage(self.d)

        #widgets
        
        layer = tk.Canvas(self.UpWindow, width =240, height = 310, bg = 'Gray')
    

        img_button = tk.Button(layer, image = self.a_ , bg = "Gray", bd = 0, command = self.exit_signup)
        signupButton = tk.Button(layer, image = self.c_ , bg = "Grey", bd = 0, command = _signUpSucess)
        showpw = tk.Checkbutton(layer, text = "show password",bd =0, variable = val, bg = "Gray", command = show_pw, font = ("lucidasans",8,"italic") )
        showpw.deselect()
        


        sLabel = tk.Label(layer, text = "Create New Account", fg ="White", bg ="Gray", font =("lucidasans",10,"bold"))
        uLabel = tk.Label(layer, text = "Username : ", bg = "Grey", fg = "White", font =("lucidasans",10,"bold") )
        uEntry = tk.Entry(layer, bg = "Grey", fg = "White",textvariable =self.username, font = ("Consolas",9,"normal"), width =23, bd = 0, justify = tk.CENTER)
        uEntry.focus()
        pEntry1 = tk.Entry(layer, bg = "Grey", fg = "White", show = "*", textvariable = self.password, font = ("Consolas",9,"normal"), width =23, bd = 0, justify = tk.CENTER )
        pLabel1 = tk.Label(layer, text = "Password : ", bg = "Grey", fg = "White", font =("lucidasans",10,"bold") )
        pEntry2 = tk.Entry(layer, bg = "Grey", fg = "White", show = "*", textvariable = self.password1, font = ("Consolas",9,"normal"), width =23, bd = 0, justify = tk.CENTER )
        pLabel2 = tk.Label(layer, text = "Enter Password again : ", bg = "Grey", fg = "White", font =("lucidasans",10,"bold") )
        
        #binding
        img_button.bind("<Enter>", enter_exit_signin)
        img_button.bind("<Leave>", leave_exit_signin)
        signupButton.bind("<Enter>", enter_signin)
        signupButton.bind("<Leave>", leave_signin)

        #widget layout
        layer.pack()
        layer.create_line(30,36,195,36, fill = "white")
        layer.create_line(40,105,200,105, fill = "Yellow")
        layer.create_line(40,163,200,163, fill = "Yellow")
        layer.create_line(40,233,200,233, fill = "Yellow")
        
        img_button.place(x = 210, y = 5)
        sLabel.place(x = 43, y =9)
        
        uLabel.place(x = 90, y = 60)
        uEntry.place(x = 40, y = 85)
        pLabel1.place(x = 90, y = 118)
        pEntry1.place(x = 40, y = 145)
        pLabel2.place(x = 39, y = 185)
        pEntry2.place(x = 40, y = 213)

        showpw.place(x = 40, y =164)
        signupButton.place(x = 100, y = 270)
       
    def exit_signin(self):
        self.InWindow.destroy()
    
    def exit_signup(self):
        self.UpWindow.destroy()  

    def show_addAccountFrame(self):
            self.user_frame.pack_forget()
            self.addAccount_frame.pack() 
    
    
        
    def frames(self):
        #Userframe images
        self.uf_img1 = Image.open("photoicons/powerOn.png")
        self.uf_img1 = self.uf_img1.resize((50,50))
        self.uf_img1 = ImageTk.PhotoImage(self.uf_img1)

        self.uf_img2 = Image.open("photoicons/powerOff.png")
        self.uf_img2 = self.uf_img2.resize((50,50))
        self.uf_img2 = ImageTk.PhotoImage(self.uf_img2)
        
        self.new_account = tk.StringVar()
        self.new_username = tk.StringVar()
        self.new_password = tk.StringVar()
        #Functions
        def enter(event):
            user_frame_limg.config(image = self.uf_img2)
            log_text.config(text = "Log-Off?", fg = "Red")
        def leave(event):
            user_frame_limg.config(image = self.uf_img1)
            log_text.config(text = "Logged-In!", fg = "Blue")
        def click_userframe():
            ans = msg.askyesno("Log-off?", "Are you sure you want to log-off?")
            if ans == True:
                self.user_frame.pack_forget()
                self.username.set("")
                self.password.set("")
                self.main_section.pack()
                self.b_button.config(state = "disabled")
                self.c_button.config(state = "disabled")
                self.d_button.config(state = "disabled")
                self.e_button.config(state = "disabled")
            else:
                pass
        def leavesave(event):
            savebut.config(image = self.addimg3 )
        def entersave(event):
            savebut.config(image = self.addimg3a )

        def clickSaveButton():
            try:
                new_account = self.new_account.get()
                new_username = self.new_username.get()
                new_password = self.new_password.get()
                self.lock.addNewAccount(new_account, new_username, new_password)
                msg.showinfo("Successfull", "Account Saved!")
                self.new_account.set("")
                self.new_username.set("")
                self.new_password.set("")
            except TypeError:
                msg.showwarning("Incomplete", "Some data is missing")

        #----------------------userframe----------------------------------
        self.user_frame = tk.Frame(self._UI,width = 630, height = 400)
        self.user_frame.pack_propagate(False)

        #Userframe widgets--------------------------- 
        self.user_text = tk.Label(self.user_frame, font =("consolas",18,"bold") )
        user_frame_limg = tk.Button(self.user_frame, image = self.uf_img1, bd = 0, command = click_userframe)
        log_text = tk.Label(self.user_frame, text= "Logged-In!", font =("consolas",15,"normal"), fg = "Blue" )

        #----------------------Add New Account---------------------------
        self.addAccount_frame = tk.Frame(self._UI,width = 630, height = 400)
        self.addAccount_frame.grid_propagate(False)

        #Add Account widget
        self.addimg1 = Image.open("photoicons/addnew1.png")
        self.addimg1 = self.addimg1.resize((300,65))
        self.addimg1 =ImageTk.PhotoImage(self.addimg1)

        self.addimg2a = Image.open("photoicons/newaccount.png")
        self.addimg2a = self.addimg2a.resize((250,40))
        self.addimg2a =ImageTk.PhotoImage(self.addimg2a)

        self.addimg2b = Image.open("photoicons/newusername.png")
        self.addimg2b = self.addimg2b.resize((250,40))
        self.addimg2b =ImageTk.PhotoImage(self.addimg2b)

        self.addimg2c = Image.open("photoicons/newpassword.png")
        self.addimg2c = self.addimg2c.resize((250,40))
        self.addimg2c =ImageTk.PhotoImage(self.addimg2c)

        self.addimg3 = Image.open("photoicons/save1.png")
        self.addimg3 = self.addimg3.resize((50,25))
        self.addimg3 =ImageTk.PhotoImage(self.addimg3)

        self.addimg3a = Image.open("photoicons/save.png")
        self.addimg3a = self.addimg3a.resize((50,25))
        self.addimg3a =ImageTk.PhotoImage(self.addimg3a)

        heading = tk.Label(self.addAccount_frame, image = self.addimg1)
        adc =tk.Label(self.addAccount_frame, image = self.addimg2a)
        adc.pack_propagate(False)
        ac_us = tk.Label(self.addAccount_frame, image = self.addimg2b)
        ac_us.pack_propagate(False)
        ac_pw = tk.Label(self.addAccount_frame, image = self.addimg2c)
        ac_pw.pack_propagate(False)
        savebut = tk.Button(self.addAccount_frame, image = self.addimg3, bd = 0, command = clickSaveButton)
        savebut.bind("<Enter>", entersave)
        savebut.bind("<Leave>", leavesave)


        #within images
        adc_textbox = tk.Entry(adc, width =23, textvariable = self.new_account, bg= "White", bd =0, font = ("consolas",10, "bold"))
        adc_textbox.pack(side=tk.LEFT, pady= [8,0], padx = [11,0])
        acus_textbox = tk.Entry(ac_us, width =23, textvariable= self.new_username, bg= "White", bd =0, font = ("consolas",10, "bold"))
        acus_textbox.pack(side=tk.LEFT, pady= [8,0], padx = [11,0])
        acpw_textbox = tk.Entry(ac_pw, width =23, textvariable= self.new_password, bg= "White", bd =0, font = ("consolas",10, "bold"))
        acpw_textbox.pack(side=tk.LEFT, pady= [8,0], padx = [11,0])
        


        #binding
        user_frame_limg.bind("<Enter>",enter)
        user_frame_limg.bind("<Leave>",leave)
        #---------------------------------------------------------------------
         

        #widget packing
        self.user_text.pack()
        user_frame_limg.pack(padx =10, pady =70)
        log_text.pack(padx = 10, pady = 70)

        heading.grid(row =0, column= 0, columnspan =3, padx =[150,0], pady = 35)
        adc.grid(row =1, column= 0, columnspan =3, padx =[150,0])
        ac_us.grid(row =2, column= 0, columnspan =3, padx =[150,0], pady = [15,0])
        ac_pw.grid(row =3, column= 0, columnspan =3, padx =[150,0], pady = [15,0])
        savebut.grid(row =4, column= 3)
        
#start app
if __name__ == "__main__":
    app = passwordlocker()
    app.start.mainloop()