

from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time
# import re




class HealthAppointmentSystem():
    def __init__(self):
        self.user_window()
        self.patient_name_var=tk.StringVar()
        self.patient_address_var=tk.StringVar()
        self.patient_app_date_var=tk.StringVar()
        self.patient_app_time_var=tk.StringVar()
        self.patient_app_purpose=tk.StringVar()
        self.Patient_doctor_var=tk.StringVar()
        self.name=tk.StringVar()
        self.Patientnamereview=[]
        self.PatientName = []
        self.Patientaddress=[]
        self.PatientDateOfAppointment=[]
        self.PatientTimeOfAppointment=[]
        self.PatientPurpose=[]
        self.Patientdoctor=[]
        self.Patient_Status=[]
        self.check_If_ApplicationSubmittedSuccessfully=False
        self.check_if_Table_Has_Data=False
        self.Patient_Appointment_Status=""
        self.getUsernameFromSignup="[];[n]"
        self.getPasswordFromSignup="][=--009]"

    def user_window(self):
        self.user_window=tk.Tk()
        width=427
        height=250
        scr_width=self.user_window.winfo_screenwidth()
        scr_height=self.user_window.winfo_screenheight()
        x=(scr_width/2)-(width/2)
        y=(scr_height/2)-(height/2)
        self.user_window.geometry("%dx%d+%d+%d"%(width,height,x,y))
        self.user_window.overrideredirect(1)
        self.user_window.configure(width=427,height=250,bg='#272727')
        label1=Label(self.user_window,text="Getting Started",fg='white',bg='#272727')
        label1.configure(font=("Comic Sans MS",30))
        label1.place(x=80,y=60)
        label2=Label(self.user_window,text="Health is Wealth",fg='#F8EB25',bg='#272727')
        label2.configure(font=("Georgia",20))
        label2.place(x=125,y=110)

        self.label3=Label(self.user_window,text="loading....",fg='white',bg='#272727')
        self.label3.configure(font=("Calibri",14))
        self.label3.place(x=10,y=215)
        self.animate_loading_dots()
    def animate_loading_dots(self,counter=0):
        dots = '.' * (counter % 3 + 1)
        self.label3.config(text="Loading" + dots)
        if counter>=2:
            self.user_window.withdraw()
            self.log_in()
        else:
            self.user_window.after(500, self.animate_loading_dots, counter + 1)
    def log_in(self):
       
        global login
        login=tk.Toplevel()
        login.title("LOG IN WINDOw")
        login.geometry("950x550")
        login.config(bg='#F2F3F4')
        custom=tkFont.Font(family="Arial",size=10,weight='bold')
        doctor_bg_image=tk.Frame(login)
        doctor_bg_image.pack()
        Doctor_Group = tk.PhotoImage(file=r"Doctor_Group_Picture.png")
        resized_photo_bg = Doctor_Group.subsample(1,1)
        myLabel_bg = tk.Label(doctor_bg_image, image=resized_photo_bg)
        myLabel_bg.image = resized_photo_bg
        myLabel_bg.grid(row=0, column=0, padx=10, pady=10, sticky="n")  
        login_frame=tk.Frame(login,bg="lightblue",bd=1,relief=tk.SOLID)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
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
        login_button=Button(login_frame,text="LOG IN",bg="blue",font=custom,fg="black",command=self.validate_pass)
        login_button.grid(row=12,column=1,padx=(0, 100), pady=(15, 0))
        sign_button=Button(login_frame,text="SIGN UP",bg="#0295A9",font=custom,fg="black",command=self.Signup)
        sign_button.grid(row=12,column=1,padx=(100, 0), pady=(15, 0))
        c=Checkbutton(login_frame,text="Show Password",command=self.password_visibility,bg="lightblue",font=custom)
        c.grid(row=24, column=1, padx=(0, 0), pady=(15, 0),)
        
    def password_visibility(self):
        if passwordentry.cget("show") == "":
            passwordentry.config(show="*")
        else:
            passwordentry.config(show="")
    def Signup(self):
         login.withdraw()
         global Sign_up
         usernameentry.delete(0,'end')
         passwordentry.delete(0,'end')
         Sign_up=tk.Toplevel() 
         Sign_up.title("SIGN UP REGISTRATION")
         Sign_up.geometry("950x550")
         Sign_up.config(bg='#B2D6ED')
         Signup_frame=tk.Frame(Sign_up,bg="#46A094",bd=1,relief=tk.SOLID)
         Signup_frame.pack(expand=True,padx=50,pady=50)
         custom=tkFont.Font(family="Arial",size=12,weight='bold')
         entry_font=("Helvatica",12)
         Label(Signup_frame,text="Sign up",height=1,width=10,bg='#46A094',font=custom,fg="black").grid(row=0,column=1,padx=(0, 60), pady=(15, 0))
         Label(Signup_frame,text="Name ",height=1,width=10,bg='silver',font=custom,fg="black").grid(row=4,column=0,padx=(0, 0), pady=(15, 0))
         Label(Signup_frame,text="Adress ",height=1,width=10,bg='silver',font=custom,fg="black").grid(row=8,column=0,padx=(0, 0), pady=(15, 0))
         Label(Signup_frame,text="Gender ",height=1,width=10,bg='silver',font=custom,fg="black").grid(row=12,column=0,padx=(0, 0), pady=(15, 0))
         Label(Signup_frame,text="Username  ",height=1,width=10,bg='silver',font=custom,fg="black").grid(row=16,column=0,padx=(0, 0), pady=(15, 0))
         Label(Signup_frame,text="Password ",height=1,width=10,bg='silver',font=custom,fg="black").grid(row=20,column=0,padx=(0, 0), pady=(15, 0))
         global signUp_username
         global signUp_password
         global name
         global address
         global birth_year
         name=Entry(Signup_frame,width=30,bg='white',font=entry_font)
         address=Entry(Signup_frame,width=30,bg='white',font=entry_font)
         birth_year=Entry(Signup_frame,width=30,bg='white',font=entry_font)
         signUp_username=Entry(Signup_frame,width=30,bg='white',font=entry_font)
         signUp_password=Entry(Signup_frame,width=30,bg='white',font=entry_font,show="*")
         name.grid(row=4,column=1,padx=(0, 90), pady=(15, 0))
         address.grid(row=8,column=1,padx=(0, 90), pady=(15, 0))
         birth_year.grid(row=12,column=1,padx=(0, 90), pady=(10, 0))
         signUp_username.grid(row=16,column=1,padx=(0, 90), pady=(15, 0))
         signUp_password.grid(row=20,column=1,padx=(0, 90), pady=(15, 0))
         Sign_up_button=tk.Button(Signup_frame,text="SIGN UP",bg="#82A762",font=custom,fg="black",command=self.SignUpValidate)
         Sign_up_button.grid(row=24,column=1,padx=(0,50), pady=(15, 0))
         c=tk.Checkbutton(Signup_frame,text="Show Password",command=self.toggle_password_visibility,bg="#46A094",font=custom)
         c.grid(row=24, column=0, padx=(50, 0), pady=(15,0))
         Label(Signup_frame,text="Already have account?",bg='#46A094',font=entry_font).grid(row=28,column=0,padx=(0, 0), pady=(15, 0))
         tk.Button(Signup_frame,text="LOG IN",bg="red",command=self.showLogin,font=custom).grid(row=28,column=0,padx=(230, 0), pady=(15, 0))   
    def toggle_password_visibility(self):
        if signUp_password.cget("show") == "":
            signUp_password.config(show="*")
        else:
            signUp_password.config(show="")
    def showLogin(self):
        Sign_up.withdraw()
        login.deiconify()
    def SignUpValidate(self):
         username2=signUp_username.get()
         password2=signUp_password.get()
         name2=name.get()
         address2=address.get()
         birth_year2=birth_year.get()
         if username2=="" or password2=="" or name2=="" or address2=="" or birth_year2=="":
            messagebox.showerror("Alert","Please input all fields")
         else:
          digit=["1","2","3","4","5","6","7","8","9","0"]
          uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
          spec_char=["!","@","#","$","%","^","&","*","(",")","_","+","{","}",":","|","<",">","?"]
          checkdig=False
          checkup=False
          check_spec=False
          for i in password2:
            if i in digit:
                checkdig=True
            if i in uppercase:
                checkup=True
            if i in spec_char:
                check_spec=True
          if checkdig==True and checkup==True and check_spec==True and len(password2)>=8:
            Sign_up.withdraw()
            self.homepage()
            self.getUsernameFromSignup=username2
            self.getPasswordFromSignup=password2

          if checkdig!=True:
            messagebox.showerror("Alert","Password must have a digit!")
          if checkup!=True:
            messagebox.showerror("Alert","Password must have uppercase!")
          if check_spec!=True:
            messagebox.showerror("Alert","Password must have a special character")
          if len(password2)<8:
            messagebox.showerror("Alert","Password minimum of  8 characters")    
    def checkUserPage(self):
            welcomePage.pack()
    def homepage(self):
        global apply_name
        global apply_address
        global apply_birthdate
        global apply_contact_number
        global apply_dateOfAppointment
        global apply_timeOfAppointment
        global Homepage
        Homepage=tk.Toplevel()
        Homepage.title("HOMEPAGE")
        Homepage.geometry("1150x700")
        Homepage.config(bg='#bdcec6')
        custom=tkFont.Font(family="Arial",size=15,weight='bold')
        homepage_frame=tk.Frame(Homepage,bg="#001F38",width=20,height=100)
        homepage_frame.pack(side="left",fill="y")
        self.userpage()
        home_button=tk.Button(homepage_frame,text="Home",bg="#006281",fg="white",font=custom,command=self.checkUserPage)
        home_button.grid(row=5,column=0,padx=(0, 0), pady=(50, 0))
        home_button.config(width=12)
        Apply_button=tk.Button(homepage_frame,text="Book now",bg="#006281",fg="white",font=custom,command=self.Apply)
        Apply_button.grid(row=10,column=0,padx=(0, 0), pady=(50, 0))
        Apply_button.config(width=12)
        Status_button=tk.Button(homepage_frame,text="Status",bg="#006281",fg="white",font=custom,command= self.seeStatus)
        Status_button.grid(row=15,column=0,padx=(0, 0), pady=(50, 0))
        Status_button.config(width=12)
        review_button=tk.Button(homepage_frame,text="Write Reviews",bg="#006281",fg="white",font=custom,command=self.writeReviews)
        review_button.grid(row=20,column=0,padx=(0, 0), pady=(50, 0))
        review_button.config(width=12)
        doctorList=tk.Button(homepage_frame,text="Doctors List",bg="#006281",fg="white",font=custom,command=self.seeDoctorList)
        doctorList.grid(row=25,column=0,padx=(0, 0), pady=(50, 0))
        doctorList.config(width=12)
        logOut_button=tk.Button(homepage_frame,text="Log Out",bg="#006281",fg="white",font=custom,command=self.LogOut)
        logOut_button.grid(row=30,column=0,padx=(0, 0), pady=(50, 0))
        logOut_button.config(width=12)
    def writeReviews(self):
    	Homepage.withdraw()
    	global reviewsPage
    	reviewsPage=tk.Toplevel()
    	reviewsPage.title("Write Reviews")
    	reviewsPage.geometry("900x610")
    	reviewsPage.config(bg='#F2F3F4')
    	entry_font=('Helvatica',12)
    	global name
    	global create_review
    	doctor_bg_image=tk.Frame(reviewsPage)
    	doctor_bg_image.pack()
    	Doctor_Group=tk.PhotoImage(file=r"sample.png")
    	resized_photo_bg=Doctor_Group.subsample(1,1)
    	myLabel_bg=tk.Label(doctor_bg_image,image=resized_photo_bg)
    	myLabel_bg.image=resized_photo_bg
    	myLabel_bg.grid(row=0, column=0, padx=10, pady=10, sticky="n")  
    	custom=tkFont.Font(family="Arial",size=10,weight="bold")
    	reviewsFrame=tk.Frame(reviewsPage,bg="#E0BBE4")
    	reviewsFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    	Label(reviewsFrame,text="Patient name",height=1,width=10,font=custom,bg="#E0BBE4",fg="black").grid(row=0,column=1,padx=(0,235), pady=(5, 15))
    	Label(reviewsFrame,text="Rate our Services ",height=1,width=18,font=custom,bg="#E0BBE4",fg="black").grid(row=0,column=1,padx=(0,200), pady=(110,0))
    	Label(reviewsFrame,text="Write your reviews",height=1,width=20,font=custom,bg="#E0BBE4",fg="black").grid(row=1,column=1,padx=(0,180),pady=(30,0))
    	self.Patientnamereview=Entry(reviewsFrame,width=20,bg='white',textvariable=self.name,font=entry_font)
    	self.Patientnamereview.grid(row=0,column=1,padx=(50, 0), pady=(5, 15))
    	rate=['1-Poor','2-Unsatisfactory','3-Satisfactory','4-Very Satisfactory','5-Outstanding']
    	choose_rate=ttk.Combobox(reviewsFrame,values=rate,width=20,font=entry_font)
    	choose_rate.set(rate[0])
    	choose_rate.grid(row=0,column=1,padx=(180,0), pady=(100,0))
    	self.patient_create_review=Text(reviewsFrame,width=35,bg='white',font=entry_font,height=7)
    	self.patient_create_review.grid(row=2,column=1,padx=(20, 0), pady=(10, 2))
    	submit_review=tk.Button(reviewsFrame,text="submit",bg="lightblue",font=custom,command=self.validate_review_submit)
    	submit_review.grid(row=4,column=1,padx=(0,100),pady=(20,10))
    	back_to_homepage=tk.Button(reviewsFrame,text='back',bg="lightblue",font=custom,command=self.from_write_review_to_homepage)
    	back_to_homepage.grid(row=4,column=1,padx=(150,0),pady=(20,10))

    def validate_review_submit(self):
    	name_of_patient_making_review=self.name.get()
    	patient_review_=self.patient_create_review.get('1.0','end').strip()
    	if name_of_patient_making_review=="" or patient_review_=="":
    		messagebox.showerror("Alert","You need to fill out all the fields")
    	else:
    		messagebox.showinfo("Alert","Thank you for making reviews it will serve as our guide to improve our services")
    		self.name.set("")
    		self.patient_create_review.delete('1.0','end')
    	
    def from_write_review_to_homepage(self):
    	reviewsPage.withdraw()
    	Homepage.deiconify()
    def seeDoctorList(self):
        Homepage.withdraw()
        global DoctorList
        DoctorList=tk.Toplevel()
        DoctorList.title("Qualified Doctors")
        DoctorList.geometry("1150x700")
        DoctorList.config(bg='#F2F3F4')
        custom=tkFont.Font(family="Arial",size=10,weight='bold')
        doctor_list_left=tk.Frame(DoctorList)
        doctor_list_left.pack(side="left")

        #photo 1
        # Photo 1
        Doctor1 = tk.PhotoImage(file="doctor1.png")
        resized_photo1 = Doctor1.subsample(2)
        myLabel1 = tk.Label(doctor_list_left, image=resized_photo1)
        myLabel1.image = resized_photo1
        myLabel1.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Use grid to place the image label
        Label_for_photo1 = tk.Label(doctor_list_left, text="Dr. John Dale \n\nSpecialty:Cardiologist \nTel. number: 098-234-90\nWorking Days:Everyday\nWorking hours:10:00 a.m -5:00 p.m", font=custom,bg="#90CF8E")
        Label_for_photo1.grid(row=0, column=1, padx=(0, 150))

        Doctor4=tk.PhotoImage(file="doctor4.png")
        resized_photo4 = Doctor4.subsample(2)
        myLabel4 = tk.Label(doctor_list_left, image=resized_photo4)
        myLabel4.image = resized_photo4
        myLabel4.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        Label_for_photo4 = tk.Label(doctor_list_left, text="Dr. Clyde Tyler \n\n Specialty:Plastic Surgery\nTel. number: 493-237-904\nWorking Days:M-W-F\nWorking hours:10:00 a.m -12:00 p.m", font=custom,bg="#90CF8E")
        Label_for_photo4.grid(row=0, column=3)
 

        # Use grid to place the label
        # Photo 2
        Doctor2 = tk.PhotoImage(file="doctor2.png")
        resized_photo2 = Doctor2.subsample(2)
        myLabel2 = tk.Label(doctor_list_left, image=resized_photo2)
        myLabel2.image = resized_photo2
        myLabel2.grid(row=1, column=0, padx=10, pady=10, sticky="w") 
        Label_for_photo2 = tk.Label(doctor_list_left, text="Dr. Philip Cruz \n\nSpecialty: Neurologist\nTel. number: 101-204-9\nWorking Days:M-W\nWorking hours:10:00 a.m -5:00 p.m", font=custom,bg="#90CF8E")
        Label_for_photo2.grid(row=1, column=1, padx=(0, 10), sticky="w")
        #photo 5 
        Doctor5=tk.PhotoImage(file="doctor5.png")
        resized_photo5 = Doctor5.subsample(2)
        myLabel5 = tk.Label(doctor_list_left, image=resized_photo5)
        myLabel5.image = resized_photo5
        myLabel5.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        Label_for_photo5 = tk.Label(doctor_list_left, text="Dr. Jhon Ponce\n\n Specialty:Gynecolist\nTel. number: 875-294-940\nWorking Days:T-Th\nWorking hours:10:00 a.m -2:00 p.m", font=custom,bg="#90CF8E")
        Label_for_photo5.grid(row=1, column=3)
 
        #photo 3
        Doctor3 = tk.PhotoImage(file="doctor3.png")
        resized_photo3 = Doctor3.subsample(2)
        myLabel3 = tk.Label(doctor_list_left, image=resized_photo3)
        myLabel3.image = resized_photo3
        myLabel3.grid(row=2, column=0, padx=10, pady=10, sticky="w")  # Use grid to place the image label
        Label_for_photo3 = tk.Label(doctor_list_left, text="Dr. Juan Ponce \n\nSpecialty: Ophthalmology\nTel. number: 997-004-90\nWorking Days:M-W-F\nWorking hours:12:00 p.m -5:00 p.m", font=custom,bg="#90CF8E")
        Label_for_photo3.grid(row=2, column=1, padx=(0, 10), sticky="w")  # Use grid to place the label
        Doctor6=tk.PhotoImage(file="doctor6.png")
        resized_photo6 = Doctor6.subsample(2)
        myLabel6 = tk.Label(doctor_list_left, image=resized_photo6)
        myLabel6.image = resized_photo6
        myLabel6.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        Label_for_photo6 = tk.Label(doctor_list_left, text="Dr. Jerry Cabal \n\n Specialty:Dermatologist\nTel. number: 009-184-10\nWorking Days:M-W-F\nWorking hours:10:00 a.m -2:00 p.m", font=custom,bg="#90CF8E")
        Label_for_photo6.grid(row=2, column=3,pady=(0,30))
        #for Button
        back_to_homepage=tk.Button(doctor_list_left,text="Back",bg="lightblue",font=custom,command=self.from_doctor_window_back_to_homepage)       
        back_to_homepage.grid(row=3,column=3,padx=(40,0))
    def from_doctor_window_back_to_homepage(self):
        DoctorList.withdraw() 
        Homepage.deiconify()
      
    def updateStatusTable(self, new_name, new_address,new_date,new_time,new_doctor,new_patient_status):
        for i in range (len(new_name)):
           table.insert(parent='', index='end', values=(new_name[i], new_address[i],new_date[i],new_time[i],new_doctor[i],new_patient_status[i]))
    
    def seeStatus(self):
        if self.check_If_ApplicationSubmittedSuccessfully==True or self.check_if_Table_Has_Data == True:
        	global table
	        Homepage.withdraw()
	        new_Patientname=self.patient_name_var.get()
	        new_Patientaddress=self.patient_address_var.get()
	        new_Patient_DateOfAppointment=self.patient_app_date_var.get()
	        new_Patient_timeOfAppointment=self.patient_app_time_var.get()
	        new_Patient_Doctor=self.Patient_doctor_var.get()
	        print("Doctor: ",new_Patient_Doctor)
	        global userStatus
	        global table
	        userStatus=tk.Toplevel()
	        userStatus.geometry('2000x2000')
	        userStatus.config(bg="#EED9C4")
	        entry_font=("Helvatica",12)
	        column_widths = ( 10, 10, 10, 10, 10,10)
	        custom_style = ttk.Style()
	        custom_style.configure("Treeview", background='#9BBB59', foreground="black",font=entry_font)
	        table=ttk.Treeview(userStatus,columns=('Name','Address','Apppointment_Date','Apppointment_Time','Doctor','Status'),show='headings')
	         
	        table.heading('Name',text='Patient name',anchor=CENTER)
	        table.heading('Address',text='Patient address',anchor=CENTER)
	        table.heading('Apppointment_Date',text='Date',anchor=CENTER)
	        table.heading('Apppointment_Time',text='Time',anchor=CENTER)
	        table.heading('Doctor',text='Doctor',anchor=CENTER)
	        table.heading('Status',text='Status',anchor=CENTER) 
	        
	        for i, width in enumerate(column_widths):
	            table.column(table["columns"][i], width=width)
	        table.place(relx=0.5,anchor="n",width=1200,height=240)
	        # if self.check_If_ApplicationSubmittedSuccessfully==True:
	        self.PatientName.append(new_Patientname)
	        self.Patientaddress.append(new_Patientaddress)
	        self.PatientDateOfAppointment.append(new_Patient_DateOfAppointment)
	        self.PatientTimeOfAppointment.append(new_Patient_timeOfAppointment)
	        self.Patientdoctor.append(new_Patient_Doctor)
	        self.Patient_Status.append(self.Patient_Appointment_Status)
	        self.updateStatusTable(self.PatientName,self.Patientaddress,self.PatientDateOfAppointment,self.PatientTimeOfAppointment,self.Patientdoctor,self.Patient_Status)
	        self.patient_name_var.set('')
	        self.patient_address_var.set('')
	        self.patient_app_date_var.set('')
	        self.patient_app_time_var.set('')
	        self.Patient_doctor_var.set('')
	        self.Patient_Appointment_Status=""
	        self.check_if_Table_Has_Data=True
	        back_to_homepage=tk.Button(userStatus,text="Back",bg="lightblue",font=entry_font,command=self.status_to_homepage)
	        back_to_homepage.place(relx=0.9,rely=0.9,anchor="se")
	        global name_patient_entry
	        global address_patient_entry
	        global doctor_patient_entry
	        global date_patient_entry
	        global time_patient_entry
	        applycancelAppointment=tk.Frame(userStatus,width=10,height=100,bg="#d3a297")
	        applycancelAppointment.place(relx=0.1,rely=0.9,anchor="sw")
	        custom=tkFont.Font(family="Arial",size=14,weight='bold')
	        textfont=tkFont.Font(family="Arial",size=20,weight='bold')
	        textlabel=tk.Label(applycancelAppointment,text="Cancellation Form",font=custom,fg="black",bg="#d3a297")
	        textlabel.pack(pady=5)
	        #name
	        name_of_patient_cancel=tk.Label(applycancelAppointment,text="Patient Name",font=entry_font,fg="black",bg="#d3a297")
	        name_of_patient_cancel.pack(pady=(5,0),padx=(20,20))
	        name_patient_entry=tk.Entry(applycancelAppointment,bg='white',font=entry_font,width=20)
	        name_patient_entry.pack(pady=(5,0),padx=(20,20),ipady=5,ipadx=10)
	        #doctor
	        address_of_patient_cancel=tk.Label(applycancelAppointment,text="Patient Address",font=entry_font,fg="black",bg="#d3a297")
	        address_of_patient_cancel.pack(pady=(5,0),padx=(20,20))
	        address_patient_entry=tk.Entry(applycancelAppointment,bg='white',font=entry_font)
	        address_patient_entry.pack(pady=(5,0),padx=(20,20),ipady=5,ipadx=10)
	        #doctor
	        doctor_of_patient_cancel=tk.Label(applycancelAppointment,text="Patient Doctor",font=entry_font,fg="black",bg="#d3a297")
	        doctor_of_patient_cancel.pack(pady=(5,0),padx=(20,20))
	        doctor_patient_entry=tk.Entry(applycancelAppointment,bg='white',font=entry_font)
	        doctor_patient_entry.pack(pady=(5,0),padx=(20,20),ipady=5,ipadx=10)
	        #date
	        date_of_patient_cancel=tk.Label(applycancelAppointment,text="Date",font=entry_font,fg="black",bg="#d3a297")
	        date_of_patient_cancel.pack(pady=(5,0),padx=(20,20))
	        date_patient_entry=tk.Entry(applycancelAppointment,bg='white',font=entry_font)
	        date_patient_entry.pack(pady=(5,0),padx=(20,20),ipady=5,ipadx=10)
	        #time
	        time_of_patient_cancel=tk.Label(applycancelAppointment,text="Time",font=entry_font,fg="black",bg="#d3a297")
	        time_of_patient_cancel.pack(pady=(5,0),padx=(20,20))
	        time_patient_entry=tk.Entry(applycancelAppointment,bg='white',font=entry_font)
	        time_patient_entry.pack(pady=(5,0),padx=(20,20),ipady=5,ipadx=10)
	        
	        cancelAppointmentButton=tk.Button(applycancelAppointment,text="cancel",bg="lightblue",font=entry_font,command=self.cancel_validation_form)
	        cancelAppointmentButton.pack(pady=(15,10),padx=(0,0))

        else:
        	messagebox.showerror("Alert","You haven't made any appointments yet")
        
    def cancel_validation_form(self):
    	check_data_is_present_in_table=False
    	validate_patient_name= name_patient_entry.get()
    	validate_patient_address=address_patient_entry.get()
    	validate_patient_doctor=doctor_patient_entry.get()
    	validate_patient_date=date_patient_entry.get()
    	validate_patient_time=time_patient_entry.get()
    	new_status="cancel"
    	if validate_patient_name=="" or validate_patient_address=="" or validate_patient_doctor=="" or validate_patient_date=="" or validate_patient_time=="":
    		messagebox.showerror("Error","Please Input all fields in cancellation form")
    	else:
            messagebox.showinfo("Alert","Successfully cancel an appointment  ")
            for i in range (len(self.PatientName)):
                if validate_patient_name==self.PatientName[i] and validate_patient_address==self.Patientaddress[i] and validate_patient_doctor==self.Patientdoctor[i] and validate_patient_date== self.PatientDateOfAppointment[i] and validate_patient_time== self.PatientTimeOfAppointment[i]:
                    self.Patient_Status[i]="cancel"
                    item_id = None
                    for child in table.get_children():
                        values = table.item(child, 'values')
                        if values[0] == validate_patient_name and values[1] == validate_patient_address:
                            item_id = child
                            break
                    if item_id:
                        table.item(item_id, values=(validate_patient_name, validate_patient_address, validate_patient_date, validate_patient_time, validate_patient_doctor, new_status))
                    check_data_is_present_in_table=True
                    break
            if check_data_is_present_in_table==False:
                messagebox.showerror("Alert","oops! you entered a wrong information in Appointment cancellation form")
    		
    			
    				
    def status_to_homepage(self):
        self.check_If_ApplicationSubmittedSuccessfully=False
        userStatus.withdraw()
        Homepage.deiconify()
    def Apply(self):
        Homepage.withdraw()
        global ApplyWindow
        global ApplyPage
        ApplyWindow=tk.Toplevel()
        ApplyWindow.title("APPOINTMENT REQUEST FORM")
        ApplyWindow.geometry("1150x950")
        ApplyWindow.config(bg="lightblue")
        ApplyPage=tk.Frame(ApplyWindow,bg="#5689C0")
        ApplyPage.pack(pady=150,padx=0)
        custom=tkFont.Font(family="Arial",size=12,weight='bold')
        entry_font=("Helvatica",12)
        Label(ApplyPage,text="APPOINTMENT FORM",font=custom,bg="#5689C0",fg="black").grid(row=0,column=0,padx=(50, 0), pady=(15, 0))
        Label(ApplyPage,text="Name ",font=custom,width=15,bg="#5689C0").grid(row=3,column=0,padx=(0, 0), pady=(15, 0))
        Label(ApplyPage,text="Address ",font=custom,width=15,bg="#5689C0").grid(row=6,column=0,padx=(0, 0), pady=(15, 0))
        Label(ApplyPage,text="Birth Date (MM/DD/YYYY): ",font=custom,bg="#5689C0").grid(row=9,column=0,padx=(0, 0), pady=(15, 0))
        Label(ApplyPage,text="Contact Number ",font=custom,bg="#5689C0").grid(row=12,column=0,padx=(0, 0), pady=(15, 0))
        Label(ApplyPage,text="Date of appointment (MM/DD/YYYY)",font=custom,bg="#5689C0").grid(row=15,column=0,padx=(0, 0), pady=(15, 0))
        Label(ApplyPage,text="Time of appointment (hh:mm AM/PM)",font=custom,bg="#5689C0").grid(row=17,column=0,padx=(0, 0), pady=(15, 0))  
        Label(ApplyPage,text="Purpose ",font=custom,bg="#5689C0").grid(row=20,column=0,padx=(0, 0), pady=(15, 0))
        Label(ApplyPage,text="Doctor ",font=custom,bg="#5689C0").grid(row=22,column=0,padx=(0, 0), pady=(15, 0))
        contact_number_entryValue=tk.StringVar()
        contact_number_entryValue.set("+639")
        self.patient_name=Entry(ApplyPage,width=30,bg='white',font=entry_font,textvariable=self.patient_name_var,bd=1,relief=tk.SOLID)
        self.patient_name.grid(row=3,column=1,padx=(0, 90), pady=(15, 0))
        self.apply_address=Entry(ApplyPage,width=30,bg='white',font=entry_font,textvariable=self.patient_address_var,bd=1,relief=tk.SOLID)
        self.apply_address.grid(row=6,column=1,padx=(0, 90), pady=(15, 0))
        self.apply_birthdate=Entry(ApplyPage,width=30,bg='white',font=entry_font,bd=1,relief=tk.SOLID)
        self.apply_birthdate.grid(row=9,column=1,padx=(0, 90), pady=(15, 0))
        self.apply_contact_number=Entry(ApplyPage,textvariable=contact_number_entryValue,width=30,bg='white',font=entry_font,bd=1,relief=tk.SOLID)
        self.apply_contact_number.grid(row=12,column=1,padx=(0, 90), pady=(15, 0))
        self.apply_dateOfAppointment=Entry(ApplyPage,width=30,bg='white',font=entry_font,textvariable=self.patient_app_date_var,bd=1,relief=tk.SOLID)
        self.apply_dateOfAppointment.grid(row=15,column=1,padx=(0, 90), pady=(15, 0))
        self.apply_timeOfAppointment=Entry(ApplyPage,width=30,bg='white',font=entry_font,textvariable=self.patient_app_time_var,bd=1,relief=tk.SOLID)
        self.apply_timeOfAppointment.grid(row=17,column=1,padx=(0, 90), pady=(15, 0))
        self.purpose=Entry(ApplyPage,width=30,bg='white',font=entry_font,textvariable=self.patient_app_purpose,bd=1,relief=tk.SOLID)
        self.purpose.grid(row=20,column=1,padx=(0, 90), pady=(15, 0))
        values=['Jhon Dale','Philip Cruz','Juan Ponce','Clyde Tyler','Jhon Bryan','Jerry Cabal']
        self.chooseDoctor=ttk.Combobox(ApplyPage,values=values,width=20,textvariable=self.Patient_doctor_var,font=entry_font)
        self.chooseDoctor.set(values[0])   
        self.chooseDoctor.grid(row=22,column=1,padx=(0, 90), pady=(15, 0))
        Submit=tk.Button(ApplyPage,text="Submit",bg="#FF6187",font=entry_font,command=self.submitApplication).grid(row=25,column=1,padx=(0, 300), pady=(20, 20))
        back_to_homepage=tk.Button(ApplyPage,text="Back",bg="lightblue",font=entry_font,command=self.homepageBack).grid(row=25,column=1,padx=(0, 0), pady=(20, 20))
        
    def homepageBack(self):
        if self.check_If_ApplicationSubmittedSuccessfully==False:
            self.patient_name_var.set('')
            self.patient_address_var.set('')
            self.patient_app_date_var.set('')
            self.patient_app_time_var.set('')
            self.patient_app_purpose.set('')
            self.Patient_doctor_var.set('')
        ApplyWindow.withdraw()
        Homepage.deiconify()

    def submitApplication(self):
        global check_message_box
        global check_birthdate
        check_message_box=False
        check_name=self.patient_name.get()
        check_address=self.apply_address.get()
        check_birthdate=self.apply_birthdate.get()
        check_contact_number=self.apply_contact_number.get()
        check_date=self.apply_dateOfAppointment.get()
        check_time=self.apply_timeOfAppointment.get()
        custom=tkFont.Font(family="Arial",size=12,weight='bold')
        digit=["1","2","3","4","5","6","7","8","9","0","+"]
        check_digit=False
        if check_name=="" or check_address=="" or check_birthdate=="" or check_contact_number=="" or check_date=="" or check_time=="":
            messagebox.showerror("Alert","Please input all fields")
            self.check_If_ApplicationSubmittedSuccessfully=False
            check_message_box=True
        elif len(check_contact_number)!=12:
            messagebox.showerror("Alert"," Invalid Phone number it must be 11 digit")
            self.check_If_ApplicationSubmittedSuccessfully=False
            check_message_box=True
        for i in check_contact_number:
            if i in digit:
                check_digit=True
            else:
                check_digit=False
                break
        if check_digit==False:
            messagebox.showerror("Alert","Contact number must be a digit")
            self.check_If_ApplicationSubmittedSuccessfully=False
            check_message_box=True
        if check_message_box==False:
         if check_birthdate:
          try:
            check_birthdate=datetime.strptime(check_birthdate,"%m/%d/%Y")
            today=datetime.today()
            if check_birthdate<=today:
                age=today.year-check_birthdate.year-((today.month,today.day)<(check_birthdate.month,check_birthdate.day))
            else:
                self.check_If_ApplicationSubmittedSuccessfully=False
                messagebox.showerror("Error","Birthdate cannot be in the future")
                check_message_box=True
          except:
            self.check_If_ApplicationSubmittedSuccessfully=False
            messagebox.showerror("Alert","Incorrect Format of Birthdate")
            check_message_box=True
        if check_message_box==False:
         if check_date:
            try:
                check_date=datetime.strptime(check_date,"%m/%d/%Y")
                today=datetime.today()
                if check_date<today:
                    self.check_If_ApplicationSubmittedSuccessfully=False
                    messagebox.showerror("Error ","Appointment date cannot be in the past")
                    check_message_box=True
            except:
                self.check_If_ApplicationSubmittedSuccessfully=False
                messagebox.showerror("Error ","Incorrect format of Appointment date")
                check_message_box=True
        if check_message_box==False:
            try:
                start_time = datetime.strptime("10:00 AM", "%I:%M %p")
                end_time = datetime.strptime("5:00 PM", "%I:%M %p")
                appointment_time = datetime.strptime(check_time, "%I:%M %p")
                if appointment_time < start_time or appointment_time > end_time:
                    messagebox.showerror("Alert","Time must be between 10:00 AM and 5:00 PM")
                    check_message_box=True
            except:
                messagebox.showerror("Alert","Invalid Format of Time")
                check_message_box=True

        self.approvalMessage()
        
    def approvalMessage(self):
        checkApplication=True
        if check_message_box==False:
            messagebox.showinfo("Alert","Your Application has been Submitted")
            self.Patient_Appointment_Status="Pending"
            self.check_If_ApplicationSubmittedSuccessfully=True

            

    def LogOut(self):
        Homepage.withdraw()
        usernameentry.delete(0,'end')
        passwordentry.delete(0,'end')
        login.deiconify()
    def userpage(self):
        global welcomePage
        welcomePage=tk.Frame(Homepage,bg="#bdcec6")
        welcomePage.pack()
        custom=tkFont.Font(family="Arial",size=14,weight='bold')
        textfont=tkFont.Font(family="Arial",size=10,weight='bold')
        hipage=tk.Label(welcomePage,text="Good day! How are you feeling today!",font=custom,fg="black").grid(row=3,column=2,padx=(0,90), pady=(100, 0))
        aboutUsTitle=tk.Label(welcomePage,text="About us",font=custom,bg="white",fg="#132743").grid(row=13,column=2,padx=(0,400), pady=(100,10))
        aboutUs=tk.Label(welcomePage,text="Welcome to HealthEase, where managing \nyour healthcare appointments has  been easier.\n At HealthEase, we're dedicated to revolutionizing\n the way patients connect with healthcare providers, \noffering a seamless  and user-friendly platform \nthat simplifies the appointment scheduling process \nfor everyone involved.",font=textfont,bg="#26282A",fg='white').grid(row=15,column=2,padx=(0,450), pady=(0,200))
        openingHoursTitle=tk.Label(welcomePage,text="Opening Hours",font=custom,bg="white",fg="#132743").grid(row=13,column=2,padx=(400,0), pady=(100,10))
        openingHours=tk.Label(welcomePage,text="Mon\t\t\t\t 10:00 A.M - 5:00 P.M \nTue\t\t\t\t 10:00 A.M - 5:00 P.M \nWed\t\t\t\t 10:00 A.M - 5:00 P.M \nThu\t\t\t\t 10:00 A.M - 5:00 P.M \nFri\t\t\t\t 10:00 A.M - 5:00 P.M \nSat\t\t\t\t 10:00 A.M - 5:00 P.M \nSun\t\t\t\t\t  Day Off",font=textfont,bg="#26282A",fg='white').grid(row=15,column=2,padx=(500,0), pady=(0, 200))
        contactInfoTitle=tk.Label(welcomePage,text="Contact Info",font=custom,bg="white",fg="#132743").grid(row=15,column=2,padx=(0,400), pady=(50,0))
        contactInfo=tk.Label(welcomePage,text="Email address: HealthEase@gmail.com \nTel. number: 0910-289-486 \nAdress: Santa Cruz st. Cebu City",font=textfont,bg="#26282A",fg='white').grid(row=15,column=2,padx=(0,450), pady=(200,0))
        welcomePage.lift()
        
    def LogOutHomepage(self):
        docPage.withdraw()
        usernameentry.delete(0,'end')
        passwordentry.delete(0,'end')
        login.deiconify()
    def Back_to_doctors_homepage(self):
        Approved_Request.withdraw()
        docPage.deiconify()




    def validate_pass(self):
        password=passwordentry.get()
        username=usernameentry.get()
        if password=="user" and username=="user":
            login.withdraw()
            self.homepage()
        elif username=="doctor" and username=="doctor":
            login.withdraw()
            self.DoctorsPage()
        elif username=="" and password=="":
            messagebox.showerror("Alert","Input password and username")
        elif username== self.getUsernameFromSignup and password== self.getPasswordFromSignup:
            login.withdraw()
            self.homepage()
        elif username=="user" and password!="user":
            messagebox.showerror("Alert","Incorrect Password")
        elif username!="user" and password=="user":
            messagebox.showerror("Alert","Incorrect Username")
        elif username!="user" and password =="":
            messagebox.showerror("Alert","Incorrect username and please input password")
        elif username=="" and password !="user":
            messagebox.showerror("Alert","Incorrect Password and please input username")
        elif username!="user" and password!="user":
            messagebox.showerror("Alert","Incorrect Password and  username")
        
         
    def run(self):
        self.user_window.mainloop()


app = HealthAppointmentSystem()
app.run()

 

    

   
