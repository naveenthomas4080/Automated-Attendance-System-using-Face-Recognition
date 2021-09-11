from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance



def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #self.bg=ImageTk.PhotoImage(file="C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=2,relheight=2)

         #bg img
        img3=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        
        #title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)  

        frame=Frame(self.root,bg="gray")
        frame.place(x=550,y=200,width=340,height=450)

         #1st
        img2=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/PicsArt_06-23-02.07.57.png")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=670,y=205,width=100,height=100)

        get_str=Label(frame,text="LOG IN",font=("times new roman",20,"bold"),fg="black",bg="grey")
        get_str.place(x=125,y=100)


        #label
        username=lbl=Label(frame,text="USERNAME",font=("times new roman",15,"bold"),fg="black",bg="grey")
        username.place(x=45,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=45,y=180)

        #label2
        password=lbl=Label(frame,text="PASSWORD",font=("times new roman",15,"bold"),fg="black",bg="grey")
        password.place(x=45,y=240)

        self.txtpass=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtpass.place(x=45,y=270)

        #Button
        loginbtn=Button(frame,text="LOGIN",command=self.login,font=("times new roman",10,"bold"),bd=1,relief=RIDGE,fg="black",bg="blue")
        loginbtn.place(x=110,y=325,width=120,height=35)

        #Button2
        registerinbtn=Button(frame,text="SIGN UP",command=self.register_window,font=("times new roman",10,"bold"),relief=RIDGE,fg="black",bg="blue")
        registerinbtn.place(x=110,y=362,width=120,height=35)

        #Button3
        forgotbtn=Button(frame,text="FORGOT PASSWORD",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="gray")
        forgotbtn.place(x=110,y=400,width=130,height=35)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get=="":
            messagebox.showerror("Error","Enter All Fields")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","welcome to automated attendance system")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                self.txtuser.get(),
                                                                                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error","Invalid user name and password")
            else:
                open_main=messagebox.askyesno("Select yes or no","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    
    def reset(self):
        if self.combo_security_q.get()=="select":
            messagebox.showerror("Error","Select sequrity question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","please enter password",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityq=%s and securitya=%s")
            value=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Succuss","Your password has successful reset",parent=self.root2)
                self.root2.destroy()




        

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),borderwidth=0,fg="blue",bg="white")
                l.place(x=0,y=10,relwidth=1)
                security_q=Label(self.root2,text="SECURITY QUESTION",font=("times new roman",15,"bold"),fg="blue",bg="white")
                security_q.place(x=50,y=80)

        

                self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",15),state="readonly",width=18)
                self.combo_security_q["values"]=("Select","Name of your pet","Name of your best friend","favourite hobby","favourate place")
                self.combo_security_q.place(x=50,y=110)
                self.combo_security_q.current(0)




                security_a=Label(self.root2,text="SECURITY ANSWER",font=("times new roman",15,"bold"),fg="blue",bg="white")
                security_a.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180)

                new_password=Label(self.root2,text="NEW PASSWORD",font=("times new roman",15,"bold"),fg="blue",bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250)

                btnn=Button(self.root2,text="RESET",command=self.reset,font=("times new roman",15,"bold"),fg="black",bg="blue")
                btnn.place(x=100,y=290)

            




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


         #bg img
        img3=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

         #title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)  

        #frame
        frame=Frame(self.root,bg="gray")
        frame.place(x=300,y=200,width=800,height=500)

        #labels
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="blue",bg="grey")
        register_lbl.place(x=20,y=20)

        fname=Label(frame,text="FIRST NAME",font=("times new roman",15,"bold"),fg="blue",bg="grey")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130)

        l_name=Label(frame,text="LAST NAME",font=("times new roman",15,"bold"),fg="blue",bg="grey")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130)


        contact=Label(frame,text="CONTACT",font=("times new roman",15,"bold"),fg="blue",bg="grey")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200)


        email=Label(frame,text="EMAIL",font=("times new roman",15,"bold"),fg="blue",bg="grey")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200)


        security_q=Label(frame,text="SECURITY QUESTION",font=("times new roman",15,"bold"),fg="blue",bg="grey")
        security_q.place(x=50,y=240)

        

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityq,font=("times new roman",15),state="readonly",width=18)
        self.combo_security_q["values"]=("Select","Name of your pet","Name of your best friend","favourite hobby","favourate place")
        self.combo_security_q.place(x=50,y=270)
        self.combo_security_q.current(0)

        


        security_a=Label(frame,text="SECURITY ANSWER",font=("times new roman",15,"bold"),fg="blue",bg="grey")
        security_a.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securitya,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270)

        pswd=Label(frame,text="PASSWORD",font=("times new roman",15,"bold"),fg="blue",bg="grey")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340)


        confirm_pswd=Label(frame,text="CONFIRM PASSWORD",font=("times new roman",15,"bold"),fg="blue",bg="grey")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340)

        #check b0x
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The terms and condition",font=("times new roman",12,"bold"),bg="grey",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)


        #buttons
        b1=Button(frame,text="REGISTER",command=self.register_data,font=("times new roman",10,"bold"),bd=1,relief=RIDGE,fg="black",bg="blue")
        b1.place(x=50,y=420,width=120,height=35)


        #b2=Button(frame,text="LOGIN",font=("times new roman",10,"bold"),bd=1,relief=RIDGE,fg="black",bg="blue")
        #b2.place(x=370,y=420,width=120,height=35)




        #function
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:
             messagebox.showerror("Error","Please agree terms and condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("error","user already excist,use different email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityq.get(),
                    self.var_securitya.get(),
                    self.var_pass.get()))
                    
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successful",parent=self.root)
        
        



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

       
       
        #1st
        img2=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=0,width=500,height=130)



#2nd 
        img=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
#3rd
        img1=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #bg img
        img3=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)  


        ##########time
        def time():
                string= strftime('%H:%M:%S %p')
                lbl.config(text=string)
                lbl.after(1000, time)
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()


        #student button
        img4=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)



        #detect face button
        img5=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/smart-attendance.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


         #attendence button
        img6=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/girl.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="ATTENDENCE",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

         #help button
       # img7=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/face_detector1.jpg")
        #img7=img7.resize((220,220),Image.ANTIALIAS)
        #self.photoimg7=ImageTk.PhotoImage(img7)
        
        #b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        #b1.place(x=1100,y=100,width=220,height=220)

        #b1_1=Button(bg_img,text="HELP",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=1100,y=300,width=220,height=40)


          #train data button
        img8=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/di.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="TRAIN",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=550,width=220,height=40)



           #photos button
        img9=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/images1.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=550,width=220,height=40)

         #exit button
        img10=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/exit.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.iexit)
        b1.place(x=800,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iexit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=550,width=220,height=40)


         #exit button
       # img11=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/face_detector1.jpg")
        #img11=img11.resize((220,220),Image.ANTIALIAS)
        #self.photoimg11=ImageTk.PhotoImage(img11)
        
        #b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        #b1.place(x=1100,y=350,width=220,height=220)

        #b1_1=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        #b1_1.place(x=1100,y=550,width=220,height=40)



    def open_img(self):
            os.startfile("data")  

    def iexit(self):
            self.iexit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit",parent=self.root)
            if self.iexit >0:
                    self.root.destroy()
            else:
                    return  


##############Function buttons
    def student_details(self):
            self.new_window=Toplevel(self.root) 
            self.app=Student(self.new_window)


    def train_data(self):
            self.new_window=Toplevel(self.root) 
            self.app=Train(self.new_window)

    def face_data(self):
            self.new_window=Toplevel(self.root) 
            self.app=Face_Recognition(self.new_window)
            

    def attendance_data(self):
            self.new_window=Toplevel(self.root) 
            self.app=Attendance(self.new_window)








if __name__=="__main__":
    main()