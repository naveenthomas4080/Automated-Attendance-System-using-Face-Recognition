from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


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
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
