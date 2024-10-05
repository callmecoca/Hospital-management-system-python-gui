# from tkinter import *
# from tkinter import messagebox
# import tkinter.font as tkFont

# def animate_loading_dots(counter=0):
#     dots = '.' * (counter % 3 + 1)
#     label3.config(text="Loading" + dots)
#     if counter >= 2:
#         window.withdraw()
#         log_in()
#     else:
#         window.after(500, animate_loading_dots, counter + 1)

# def log_in():
#     login = Toplevel()
#     login.title("LOG IN WINDOW")
#     login.geometry("1000x1000")
#     login.config(bg='#5B8291')
#     login_frame = Frame(login, bg="lightblue", bd=1, relief=SOLID)
#     login_frame.pack(expand=True, padx=50, pady=50)
#     custom = tkFont.Font(family="Arial", size=12, weight='bold')
#     entry_font = ("Helvatica", 14)
#     Label(login_frame, text="USER LOG IN", height=1, width=10, bg='lightblue', font=custom, fg="#41436A").grid(row=0, column=1)
#     Label(login_frame, text="Username ", height=1, width=10, bg='lightblue', font=custom, fg="black").grid(row=5, column=1)
#     Label(login_frame, text="Password ", height=1, width=10, bg='lightblue', font=custom, fg="black").grid(row=8, column=1)
#     global usernameentry
#     global passwordentry
#     usernameentry = Entry(login_frame, width=30, bg='white', font=entry_font)
#     passwordentry = Entry(login_frame, width=30, bg='white', font=entry_font, show="*")
#     usernameentry.grid(row=7, column=1)
#     passwordentry.grid(row=11, column=1, pady=5)
#     login_button = Button(login_frame, text="LOG IN", bg="blue", font=custom, fg="black")
#     login_button.grid(row=12, column=1, padx=(0, 100), pady=(15, 0))
#     sign_button = Button(login_frame, text="SIGN UP", bg="#0295A9", font=custom, fg="black")
#     sign_button.grid(row=12, column=1, padx=(100, 0), pady=(15, 0))
#     c = Checkbutton(login_frame, text="Show Password", command=password_visibility, bg="silver")
#     c.grid(row=24, column=1, padx=(0, 0), pady=(15, 0))

# def password_visibility():
#     if passwordentry.cget("show") == "":
#         passwordentry.config(show="*")
#     else:
#         passwordentry.config(show="")

# window = Tk()
# width = 427
# height = 250
# scr_width = window.winfo_screenwidth()
# scr_height = window.winfo_screenheight()
# x = (scr_width/2) - (width/2)
# y = (scr_height/2) - (height/2)
# window.geometry("%dx%d+%d+%d" % (width, height, x, y))
# window.overrideredirect(1)
# window.configure(width=427, height=250, bg='#272727')
# label1 = Label(window, text="Getting Started", fg='white', bg='#272727')
# label1.configure(font=("Comic Sans MS", 30))
# label1.place(x=80, y=60)
# label2 = Label(window, text="Health is Wealth", fg='#F8EB25', bg='#272727')
# label2.configure(font=("Georgia", 20))
# label2.place(x=125, y=110)
# label3 = Label(window, text="loading....", fg='white', bg='#272727')
# label3.configure(font=("Calibri", 14))
# label3.place(x=10, y=215)

# animate_loading_dots()

# window.mainloop()



import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
def animate_loading_dots(counter=0):
    dots = '.' * (counter % 3 + 1)
    label3.config(text="Loading" + dots)
    if counter>=2:
        window.withdraw()
        log_in()
    else:
        window.after(500, animate_loading_dots, counter + 1)



def log_in():
    login=tk.Toplevel()
    login.title("LOG IN WINDOW")
    login.geometry("1000x1000")
    login.config(bg='#5B8291')
    login_frame=tk.Frame(login,bg="lightblue",bd=1,relief=tk.SOLID)
    login_frame.pack(expand=True,padx=50,pady=50)
    custom=tkFont.Font(family="Arial",size=12,weight='bold')
    entry_font=("Helvatica",14)
    Label(login_frame, text="USER LOG IN",height=1,width=10,bg='lightblue',font=custom,fg="#41436A").grid(row=0,column=1)
    Label(login_frame, text="Username ",height=1,width=10,bg='lightblue',font=custom,fg="black").grid(row=5,column=1)
    Label(login_frame, text="Password ",height=1,width=10,bg='lightblue',font=custom,fg="black").grid(row=8,column=1)
    global usernameentry
    global passwordentry
    usernameentry=Entry(login_frame,width=30,bg='white',font=entry_font)
    passwordentry=Entry(login_frame,width=30,bg='white',font=entry_font,show="*")
    usernameentry.grid(row=7,column=1)
    passwordentry.grid(row=11,column=1,pady=5)
    login_button=Button(login_frame,text="LOG IN",bg="blue",font=custom,fg="black")
    login_button.grid(row=12,column=1,padx=(0, 100), pady=(15, 0))
    sign_button=Button(login_frame,text="SIGN UP",bg="#0295A9",font=custom,fg="black")
    sign_button.grid(row=12,column=1,padx=(100, 0), pady=(15, 0))
    c=Checkbutton(login_frame,text="Show Password",command=password_visibility,bg="silver")
    c.grid(row=24, column=1, padx=(0, 0), pady=(15, 0),)
def password_visibility():
    if passwordentry.cget("show") == "":
        passwordentry.config(show="*")
    else:
        passwordentry.config(show="")

window=tk.Tk()
width=427
height=250
scr_width=window.winfo_screenwidth()
scr_height=window.winfo_screenheight()
x=(scr_width/2)-(width/2)
y=(scr_height/2)-(height/2)
window.geometry("%dx%d+%d+%d"%(width,height,x,y))
window.overrideredirect(1)
window.configure(width=427,height=250,bg='#272727')
label1=Label(window,text="Getting Started",fg='white',bg='#272727')
label1.configure(font=("Comic Sans MS",30))
label1.place(x=80,y=60)
label2=Label(window,text="Health is Wealth",fg='#F8EB25',bg='#272727')
label2.configure(font=("Georgia",20))
label2.place(x=125,y=110)

label3=Label(window,text="loading....",fg='white',bg='#272727')
label3.configure(font=("Calibri",14))
label3.place(x=10,y=215)


animate_loading_dots()

window.mainloop()