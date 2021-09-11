from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #variables################3

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        #1st
        img2=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img2=img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=0,width=800,height=200)



#2nd 
        img=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #bg img
        img3=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=2000,height=800)

        #left label frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=2,y=10,width=700,height=800)


        img_left=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=700,height=300)

        #labels and entry
        #attendance id
        attendance_label=Label(left_inside_frame,text="ATTENDENCE ID",font=("times new roman",13,"bold"))
        attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendance_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        
        #roll
        studentname_label=Label(left_inside_frame,text="ROLL",font=("times new roman",13,"bold"))
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #student name
        studentname_label=Label(left_inside_frame,text="NAME",font=("times new roman",13,"bold"))
        studentname_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #student dep
        studentname_label=Label(left_inside_frame,text="DEP",font=("times new roman",13,"bold"))
        studentname_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #student time
        studentname_label=Label(left_inside_frame,text="TIME",font=("times new roman",13,"bold"))
        studentname_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #student DATE
        studentname_label=Label(left_inside_frame,text="DATE",font=("times new roman",13,"bold"))
        studentname_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendeance
        class_div_label=Label(left_inside_frame,text="ATTENDANCE STATUS",font=("times new roman",13,"bold"))
        class_div_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",13),state="readonly",width=18)
        div_combo["values"]=("STATUS","PRESENT","ABSENT")
        div_combo.current(0)
        div_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)



        #btnframe
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=70)

        save_btn=Button(btn_frame,text="import csv",command=self.importCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="export csv",command=self.exportCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

       # reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
     #   reset_btn.grid(row=0,column=3)













        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="ATTENDANCE DETAILS",font=("times new roman",13,"bold"))
        right_frame.place(x=700,y=10,width=730,height=800)
        

         #img
        img_right=Image.open("C:/Users/Naveen Thomas/Desktop/face_recognition system/img/elegant-white-background-with-shiny-lines_1017-17580.jpg")
        img_right=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=500,height=130)


         #btnframe
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=3,y=130,width=645,height=300)


        ########3scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    

    #########fetch data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import ccsv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No DATA","No Data Found",parent=self.root)
                return FALSE
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("DATA EXPORT","Your data exported to "+os.path.basename(fln)+" successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])   
        self.var_atten_roll.set(rows[1]) 
        self.var_atten_name.set(rows[2]) 
        self.var_atten_dep.set(rows[3]) 
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5]) 
        self.var_atten_attendance.set(rows[6])          

    def reset_data(self):
        self.var_atten_id.set("") 
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()