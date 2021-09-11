from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #########varriable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        





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
        title_lbl=Label(bg_img,text="STUDENT MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)  
        
        
       
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=2000,height=800)


        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=2,y=10,width=700,height=800)


        img_left=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        #current course frame
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",12,"bold"))
        current_course_frame.place(x=2,y=130,width=720,height=200)

        #department label
        dep_label=Label(current_course_frame,text="DEPARTMENT",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CSA","Science","Arts")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="COURSE",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13),state="readonly",width=20)
        course_combo["values"]=("Select Course","BCA","MCA","BS","MS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #YEAR
        year_label=Label(current_course_frame,text="YEAR",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13),state="readonly",width=20)
        year_combo["values"]=("Select year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="SEMESTER",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13),state="readonly",width=20)
        semester_combo["values"]=("Select semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Student information
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"))
        class_student_frame.place(x=2,y=250,width=720,height=300)
        
        #studentid
        studentid_label=Label(class_student_frame,text="STUDENT ID",font=("times new roman",13,"bold"))
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentname_label=Label(class_student_frame,text="NAME",font=("times new roman",13,"bold"))
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="DIVISION",font=("times new roman",13,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13),state="readonly",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_no_label=Label(class_student_frame,text="ROLL NO",font=("times new roman",13,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #gender
        gender_label=Label(class_student_frame,text="GENDER",font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

         #dob
        dob_label=Label(class_student_frame,text="DOB",font=("times new roman",13,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         #email
        email_label=Label(class_student_frame,text="EMAIL",font=("times new roman",13,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         #phone no
        phone_label=Label(class_student_frame,text="PHONE NO",font=("times new roman",13,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         #address
        address_label=Label(class_student_frame,text="ADDRESS",font=("times new roman",13,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name
        teacher_label=Label(class_student_frame,text="TEACHER'S Name",font=("times new roman",13,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radiobutton
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="no")
        radiobtn2.grid(row=6,column=1)
       
        #btnframe
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=70)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="update",command=self.update_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        take_photo_btn=Button(btn_frame,command=self.genarate_dataset,text="take photo",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4)

        update_photo_btn=Button(btn_frame,text="update photo",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=5)



         #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",13,"bold"))
        right_frame.place(x=700,y=10,width=730,height=800)

        #img
        img_right=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img_right=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=500,height=130)

        ######searching system#####
        #Student information
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=700,height=130)

        search_label=Label(search_frame,text="SEARCH BY",font=("times new roman",13,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(search_frame,font=("times new roman",13),state="readonly",width=10)
        search_combo["values"]=("Select","Roll No","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=10,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        search_btn=Button(search_frame,text="SEARCH",width=8,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        showall_btn=Button(search_frame,text="SHOW ALL",width=8,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)


#=============table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=200,width=650,height=311)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        ##############fuction declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_dep.get(),
                                                                                self.var_course.get(),
                                                                                self.var_year.get(),
                                                                                self.var_semester.get(),
                                                                                self.var_std_id.get(),
                                                                                self.var_std_name.get(),
                                                                                self.var_div.get(),
                                                                                self.var_roll.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_email.get(),
                                                                                self.var_phone.get(),
                                                                                self.var_address.get(),
                                                                                self.var_teacher.get(),
                                                                                self.var_radio1.get()                                                          
                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","student details has been added successfuly",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        
        ######fetch data
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()

            if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                            self.student_table.insert("",END,values=i)
                    conn.commit()
            conn.close()

    ################get cursor
    def get_cursor(self,event=""):
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            data=content["values"]

            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_std_id.set(data[4]),
            self.var_std_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14]),
   
    ###########Update function
    def update_data(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("ERROR","All fields are required",parent=self.root)
            else:
                    try:
                            Upadate=messagebox.askyesno("Upadte","Do you want to update this students's details",parent=self.root)
                            if Upadate >0:
                                    conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
                                    my_cursor=conn.cursor()
                                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                self.var_dep.get(),
                                                                                self.var_course.get(),
                                                                                self.var_year.get(),
                                                                                self.var_semester.get(), 
                                                                                self.var_div.get(),
                                                                                self.var_roll.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_email.get(),
                                                                                self.var_phone.get(),
                                                                                self.var_address.get(),
                                                                                self.var_teacher.get(),
                                                                                self.var_radio1.get(),
                                                                                self.var_std_id.get()
                                                                                ))  
                            else:
                                    if not Upadate:
                                            return    
                            messagebox.showinfo("Success","Student details Succussfully Updated",parent=self.root)   
                            conn.commit()
                            self.fetch_data()
                            conn.close()

                    except Exception as es:
                            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)       

    ##########delete fuction
    def delete_data(self):
            if self.var_std_id.get()=="":
                    messagebox.showerror("Error","Student id is required",self.root)
            else:
                    try:
                            delete=messagebox.askyesno("Student Details","Do you want to delete this student",parent=self.root)
                            if delete>0:
                                    conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
                                    my_cursor=conn.cursor()
                                    sql="delete from student where Student_id=%s"
                                    val=(self.var_std_id.get(),)
                                    my_cursor.execute(sql,val)
                            else:
                                    if not delete:
                                            return

                               
                            conn.commit()
                            self.fetch_data()
                            conn.close()  
                            messagebox.showinfo("Success","Student details Succussfully Deleted",parent=self.root)  
                    except Exception as es:
                            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


#######reset function
    def reset_data(self):
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_year.set("Select year")
            self.var_semester.set("Select semester")
            self.var_std_id.set("")
            self.var_std_name.set("")
            self.var_div.set("A")
            self.var_roll.set("")
            self.var_gender.set("Male")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_teacher.set("")
            self.var_radio1.set("")

#########take photo sample
    def genarate_dataset(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("ERROR","All fields are required",parent=self.root)
            else:
                    try:
                            Upadate=messagebox.askyesno("Upadte","Do you want to add photo of this student",parent=self.root)
                            if Upadate >0:
                                    conn=mysql.connector.connect(host="localhost",username="root",password="jarvisonline",database="face_recognizer")
                                    my_cursor=conn.cursor()
                                    my_cursor.execute("select * from student")
                                    myresult=my_cursor.fetchall()
                                    id=0
                                    for x in myresult:
                                            id+=1
                                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                self.var_dep.get(),
                                                                                self.var_course.get(),
                                                                                self.var_year.get(),
                                                                                self.var_semester.get(), 
                                                                                self.var_div.get(),
                                                                                self.var_roll.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_email.get(),
                                                                                self.var_phone.get(),
                                                                                self.var_address.get(),
                                                                                self.var_teacher.get(),
                                                                                self.var_radio1.get(),
                                                                                self.var_std_id.get()==id+1
                                                                                ))  
                                    conn.commit()
                                    self.fetch_data()
                                    self.reset_data()
                                    conn.close()

                                    ########3load predefined data on face frontal from opencv
                                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                                    def face_cropped(img):
                                            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                            faces=face_classifier.detectMultiScale(gray,1.3,5)
                                            #scaling factor=1.3
                                            #minimum neighbor=5

                                            for (x,y,w,h) in faces:
                                                    face_cropped=img[y:y+h,x:x+w]
                                                    return face_cropped
                                    cap=cv2.VideoCapture(0)
                                    img_id=0
                                    while True:
                                            ret,my_frame=cap.read()
                                            if face_cropped(my_frame) is not None:
                                                    img_id+=1
                                                    face=cv2.resize(face_cropped(my_frame),(450,450))  
                                                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)  
                                                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                                    cv2.imwrite(file_name_path,face)
                                                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                                    cv2.imshow("Cropped Face",face)

                                            
                                            if cv2.waitKey(1)==13 or int(img_id)==100:
                                                    break
                                    cap.release()
                                    cv2.destroyAllWindows()
                                    messagebox.showinfo("Result","Generating data set completed",parent=self.root)
                       
                    except Exception as es:
                            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)                    






        
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()