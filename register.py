from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector





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
        b2=Button(frame,text="REGISTER",command=self.register_data,font=("times new roman",10,"bold"),bd=1,relief=RIDGE,fg="black",bg="blue")
        b2.place(x=50,y=420,width=120,height=35)


        b2=Button(frame,text="LOGIN",font=("times new roman",10,"bold"),bd=1,relief=RIDGE,fg="black",bg="blue")
        b2.place(x=370,y=420,width=120,height=35)




        #function
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select":
            messagebox.showerror("Error","All Fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
             messagebox.showerror("Error","Please agree terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("error","user already excist,use different email")
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
            messagebox.showinfo("Success","Registration Successful")

    









        





if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()