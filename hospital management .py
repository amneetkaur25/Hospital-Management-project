
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import random
from tkcalendar import DateEntry
import mysql.connector as sqlcon

conn = sqlcon.connect(user="root", host="localhost", password="")
cur = conn.cursor()
if (conn):
    print("Connection successfull")
else:
    print("connection unsuccessfull")

try:
    cur.execute("create database Hospital;")
except:
    pass
cur.execute("use Hospital;")

try:
    cur.execute("create table Register(id_no varchar(20) primary key,name varchar(20),age varchar(5),gender varchar(5),ph_no varchar(20),bg varchar(10));")
except:
    pass

try:
    cur.execute("create table appointment_details(id_no varchar(20),doctor varchar(40),date varchar(20),time varchar(20),appoint_no varchar(20));")
except:
    pass
try:
    cur.execute(
        "create table slots(name varchar(20), time_10am int, time_12pm int, time_3pm int , time_5pm int);")
    
except :
    pass


class hospital:
    # HOMEPAGE
    def homepage(self):
        # HEADING
        self.root = Tk()
        self.root.title("Hospital Management")
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.geometry(f"{self.w}x{self.h}")
        self.root.configure(bg="pink")

        self.img = Image.open(r'./hosp2.jpg')
        self.resize_img=self.img.resize((1280,720))
        self.img = ImageTk.PhotoImage(self.resize_img)
        self.l = Label(self.root, image=self.img)
        self.l.place(relx=0.0, rely=0.0)
        def exit():
            self.root.destroy()
        # LABELS

        self.l = Label(self.root, text="Indian Hospital", font=(
            "Times New Roman", 30, "italic"), bg="pink", fg="purple")
        self.l.place(relx=0.4, rely=0.01)

        self.b1 = Button(self.root, text="Registration", font=(
            "Times New Roman", 24),bg="light blue", command=register)
        self.b1.place(relx=0.2, rely=0.6)

        self.b2 = Button(self.root, text="List of doctors",
                         font=("Times New Roman", 24),bg="light blue", command=lst_doc)
        self.b2.place(relx=0.4, rely=0.6)

        self.b3 = Button(self.root, text="Services Available",
                         font=("Times New Roman", 24),bg="light blue", command=services)
        self.b3.place(relx=0.6, rely=0.6)

        self.b3 = Button(self.root, text="Appointment", font=(
            "Times New Roman", 24),bg="light blue", command=appoint)
        self.b3.place(relx=0.2, rely=0.8)

        self.b4 = Button(self.root, text="Modify Existing data",
                         font=("Times New Roman", 24), bg="light blue",command=mod)
        self.b4.place(relx=0.4, rely=0.8)

        self.b5 = Button(self.root, text="Exit", font=(
            "Times New Roman", 24), bg="light blue",command=exit)
        self.b5.place(relx=0.7, rely=0.8)

        self.root.mainloop()

    # REGISTRATION PAGE

    def registeration(self):
        self.root1 = Tk()
        self.root1.title("Registeration Page")
        self.w1 = self.root1.winfo_screenwidth()
        self.h1 = self.root1.winfo_screenheight()
        self.root1.geometry(f"{self.w1}x{self.h1}")
        self.root1.configure(bg="sky blue")

        def bk():
            obj.root1.destroy()
            obj.homepage()

        # labels
        self.l = Label(self.root1, text="Register Yourself", font=(
            "Times New Roman", 30, "italic"), bg="sky blue", fg="dark blue")
        self.l.place(relx=0.38, rely=0.01)

        self.l1 = Label(self.root1, text="Id No:", font=(
            "Times New Roman", 20), bg="sky blue")
        self.l1.place(relx=0.3, rely=0.3)

        self.l2 = Label(self.root1, text="Name:", font=(
            "Times New Roman", 20), bg="sky blue")
        self.l2.place(relx=0.3, rely=0.38)

        self.l3 = Label(self.root1, text="Age:", font=(
            "Times New Roman", 20), bg="sky blue")
        self.l3.place(relx=0.3, rely=0.46)

        self.l4 = Label(self.root1, text="Gender:", font=(
            "Times New Roman", 20), bg="sky blue")
        self.l4.place(relx=0.3, rely=0.54)

        self.l5 = Label(self.root1, text="Phone No:", font=(
            "Times New Roman", 20), bg="sky blue")
        self.l5.place(relx=0.3, rely=0.62)

        self.l6 = Label(self.root1, text="Blood Group:",
                        font=("Times New Roman", 20), bg="sky blue")
        self.l6.place(relx=0.3, rely=0.7)

        # ENTRY FIELDS

        self.e1 = Entry(self.root1, font=("Times New Roman", 18))
        self.e1.place(relx=0.45, rely=0.3)

        self.e2 = Entry(self.root1, font=("Times New Roman", 18))
        self.e2.place(relx=0.45, rely=0.38)

        self.e3 = Entry(self.root1, font=("Times New Roman", 18))
        self.e3.place(relx=0.45, rely=0.46)

        self.val = IntVar()

        self.male = Radiobutton(self.root1, text="Male", variable=self.val, value=0, font=("Times New Roman", 18))
        self.male.place(relx=0.45, rely=0.54)

        self.female = Radiobutton(
            self.root1, text="Female", variable=self.val, value=1, font=("Times New Roman", 18),width=7)
        self.female.place(relx=0.54, rely=0.54)

        self.e5 = Entry(self.root1, font=("Times New Roman", 18))
        self.e5.place(relx=0.45, rely=0.62)

        self.v = StringVar()
        self.v.set("choose blood group")
        lst = ["A+", "A-", "B+", "B-", "O+", "O-", "AB"]
        self.e6 = ttk.Combobox(self.root1, textvariable=self.v, values=lst,
                               font=("Times New Roman", 18),width=19)
        self.e6.place(relx=0.45, rely=0.7)

        # button
        self.bt = Button(self.root1, text="Submit", font=(
            "Times New Roman", 24), command=entry)
        self.bt.place(relx=0.4, rely=0.8)

        self.bt = Button(self.root1, text="Back To Homepage",
                         font=("Times New Roman", 18), command=bk)
        self.bt.place(relx=0.8, rely=0.9)

        self.root1.mainloop()

    # LIST OF DOCTORS PAGE

    def list_of_doctors(self):
        self.root2 = Tk()
        self.root2.title("List of doctors")
        self.w = self.root2.winfo_screenwidth()
        self.h = self.root2.winfo_screenheight()
        self.root2.geometry(f"{self.w}x{self.h}")
        self.root2.configure(bg="light green")
        self.img = Image.open(r'./doc.jpg')
        self.resize_img=self.img.resize((1280,720))
        self.img = ImageTk.PhotoImage(self.resize_img)
        self.l = Label(self.root2, image=self.img)
        self.l.place(relx=0.0, rely=0.0)

        # labels
        names = ["Dr. sharma ", "Dr. Verma ", "Dr. Kumar", "Dr. Khan", "Dr. Kohli", "Dr. singh", "Dr. Sidharth", "Dr. tendulkar", "Dr. Virat", "Dr. Leo", 'Dr. Irfan', 'Dr. John',
                 'Dr. Sanjay', 'Dr. Shahid']
        depart = ["Orthopaedic surgeon", "Orthopaedic surgeon", "Nephrologist", "Nephrologist", "Gynaecologist", "Gynaecologist", "Physician", "Physician", "Neurologist",
                  "Neurologist", 'X-ray', 'X-ray', 'X-ray', 'X-ray']
        d = {}
        for i in range(len(depart)):
            if depart[i] not in d:
                d[depart[i]] = [names[i]]
            else:
                d[depart[i]].append(names[i])

        alter_doc(doc_dict=d)

        self.l = Label(self.root2, text="Department", font=(
            "Times New Roman", 20, "italic"),fg="maroon")
        self.l.place(x=50, y=10)
        count = 30
        for i in list(d.keys()):
            count = count+80
            l = Label(self.root2, text=i)
            l.place(x=50, y=count)
        self.l1 = Label(self.root2, text="Name of Doctors", font=(
            "Times New Roman", 20, "italic"), fg="maroon")
        self.l1.place(x=270, y=10)
        count = 20
        for i in list(d.values()):
            count = count+80
            s = ""
            for j in i:
                s += j+", "
            l = Label(self.root2, text=s[:-2])
            l.place(x=270, y=count)

        bt = Button(self.root2, text="Back to Homepage",
                    font=("Times New Roman", 18), command=back)
        bt.place(x=900, y=600)

        self.root2.mainloop()

    # SERVICES AVAILABLE PAGE

    def services_avail(self):
        self.root3 = Tk()
        self.root3.title("services available")
        self.w = self.root3.winfo_screenwidth()
        self.h = self.root3.winfo_screenheight()
        self.root3.geometry(f"{self.w}x{self.h}")
        self.root3.configure(bg="#d2adbd")

        self.l1 = Label(self.root3, text="Services Available", font=(
            "Times New Roman", 24, "italic"), bg="#d2adbd", fg="maroon")
        self.l1.place(x=20, y=10)
        f = ["ULTRASOUND", "X-RAY", "CT Scan", "MRI",
             "BLOOD COLLECTION", "DIALYSIS", "ECG", "CHEMIST", "LAB"]
        count = 30
        for i in f:
            count = count+40
            self.l2 = Label(self.root3, text=i, bg="#d2adbd",
                            font=("Times New Roman", 16))
            self.l2.place(x=40, y=count)

        self.l3 = Label(self.root3, text="Room No.", font=(
            "Times New Roman", 24), bg="#d2adbd", fg="maroon")
        self.l3.place(x=500, y=10)
        g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        count1 = 30
        for i in g:
            count1 = count1+40
            self.l4 = Label(self.root3, text=i, font=(
                "Times New Roman", 16), bg="#d2adbd")
            self.l4.place(x=500, y=count1)

        self.l5 = Label(self.root3, text="To avail any of these please contact on our no.:- 7042****55",
                        font=("Times New Roman", 18), bg="#d2adbd", fg="maroon")
        self.l5.place(x=20, y=480)

        bt = Button(self.root3, text="Back to Homepage",
                    font=("Times New Roman", 18), command=bck)
        bt.place(x=800, y=550)

        self.root3.mainloop()

    # APPOINTMENT PAGE
    def appointment(self):
        global x1
        self.root4 = Tk()
        self.root4.title("Appointment")
        self.w = self.root4.winfo_screenwidth()
        self.h = self.root4.winfo_screenheight()
        self.root4.geometry(f"{self.w}x{self.h}")
        self.root4.configure(bg="#9ab6c2")

        self.img = Image.open(r'./appointment.jpg')
        self.resize_img = self.img.resize((1280, 720))
        self.img = ImageTk.PhotoImage(self.resize_img)
        self.l = Label(self.root4, image=self.img)
        self.l.place(relx=0.0, rely=0.0)

        self.l1 = Label(self.root4, text="Id No:",
                        font=("Times New Roman", 20),bg="pink")
        self.l1.place(x=400, y=400)

        self.x1 = Entry(self.root4, font=("Times New Roman", 20),bg="pink")
        self.x1.place(x=520, y=400)

        self.bt = Button(self.root4, text="submit", font=(
            "Times New Roman", 20),bg="pink", command=get_appoint)
        self.bt.place(x=500, y=500)

        self.root4.mainloop()

    # creating Modification page

    def modification(self):
        global x1
        self.root8 = Tk()
        self.root8.title("Modification")
        self.w = self.root8.winfo_screenwidth()
        self.h = self.root8.winfo_screenheight()
        self.root8.geometry(f"{self.w}x{self.h}")
        #self.root8.configure(bg="#9ab6c2")
        
        self.img = Image.open(r'./mod.png')
        self.resize_img = self.img.resize((1280, 720))
        self.img = ImageTk.PhotoImage(self.resize_img)
        self.l = Label(self.root8, image=self.img)
        self.l.place(relx=0.0, rely=0.0)
        self.l = Label(self.root8, text="Modification", font=(
            "Times New Roman", 24, "italic"), bg="sky blue", fg="dark blue")
        self.l.place(x=500, y=10)

        self.l1 = Label(self.root8, text="Id No:",
                        font=("Times New Roman", 20),bg="sky blue")
        self.l1.place(x=730, y=300)

        self.x1 = Entry(self.root8, font=("Times New Roman", 20),bg="sky blue")
        self.x1.place(x=880, y=300)

        self.bt = Button(self.root8, text="submit", font=(
            "Times New Roman", 20),bg="sky blue", command=modify)
        self.bt.place(x=830, y=380)

        self.root8.mainloop()


# CREATING OBJECT FOR CLASS
obj = hospital()


def register():
    obj.root.destroy()
    obj.registeration()


def entry():
    global p1, p2, p3, p4, p5, p6
    p1 = obj.e1.get()
    p2 = obj.e2.get()
    p3 = obj.e3.get()
    p4 = obj.val.get()
    if p4 == 0:
        p4 = "M"
    elif p4 == 1:
        p4 = "F"
    p5 = obj.e5.get()
    p6 = obj.v.get()

    try:
        cur.execute(
            f"insert into Register values('{p1}','{p2}','{p3}','{p4}','{p5}','{p6}');")
        messagebox.showinfo("Done")

    except:
        messagebox.showinfo("Error")

    obj.e1.delete(0, END)
    obj.e2.delete(0, END)
    obj.e3.delete(0, END)
    obj.e5.delete(0, END)
    obj.root1.destroy()
    obj.homepage()


def lst_doc():
    obj.root.destroy()
    obj.list_of_doctors()


def back():
    obj.root2.destroy()
    obj.homepage()


def services():
    obj.root.destroy()
    obj.services_avail()


def bck():
    obj.root3.destroy()
    obj.homepage()


def appoint():
    obj.root.destroy()
    obj.appointment()


def get_appoint():
    global p1, x1, choice, date_, time_
    p1 = obj.x1.get()
    cur.execute(f"select * from Register where id_no='{p1}';")
    lst = []
    data = cur.fetchall()

    for i in data:
        lst.append(i)
    if len(lst) == 0:
        messagebox.showerror("NO User")
    else:
        obj.root4.destroy()
        root5 = Tk()
        root5.title(" Get Appointment")
        w = root5.winfo_screenwidth()
        h = root5.winfo_screenheight()
        root5.geometry(f"{w}x{h}")
        root5.configure(bg="pink")

        def back():
            root5.destroy()
            obj.homepage()

        l = Label(root5, text="Get Appointment", font=(
            "Times New Roman", 30, "italic"), bg="pink", fg="Green")
        l.place(x=480, y=10)

        if i[3] == "M":
            x = "Mr."
            name2 = Label(root5, text=i[1], font=(
                "Times New Roman", 16), bg="pink")
            name2.place(x=240, y=80)
        else:
            x = "Mrs/Ms."
            name2 = Label(root5, text=i[1], font=(
                "Times New Roman", 16), bg="pink")
            name2.place(x=280, y=80)
        for i in data:
            name = Label(root5, text='WELCOME', font=(
                "Times New Roman", 16), bg="pink")
            name.place(x=50, y=80)
            name1 = Label(root5, text=x, font=(
                "Times New Roman", 16), bg="pink")
            name1.place(x=200, y=80)
            age = Label(root5, text='AGE:-',
                        font=("Times New Roman", 16), bg="pink")
            age.place(x=50, y=110)
            age1 = Label(root5, text=i[2], font=(
                "Times New Roman", 16), bg="pink")
            age1.place(x=150, y=110)
            phone = Label(root5, text='PHONE:-',
                          font=("Times New Roman", 16), bg="pink")
            phone.place(x=50, y=140)
            phone1 = Label(root5, text=i[4], font=(
                "Times New Roman", 16), bg="pink")
            phone1.place(x=150, y=140)
            bg = Label(root5, text='BLOOD GROUP:-',
                       font=("Times New Roman", 16), bg="pink")
            bg.place(x=50, y=170)
            bg1 = Label(root5, text=i[5], font=(
                "Times New Roman", 16), bg="pink")
            bg1.place(x=230, y=170)

        l1 = Label(root5, text="Departments", font=(
            "Times New Roman", 24, "italic"), bg="pink", fg="green")
        l1.place(x=30, y=210)
        l2 = Label(root5, text="1.Orthopaedic surgeon ",
                   font=("Times New Roman", 16), bg="pink")
        l2.place(x=50, y=260)
        l3 = Label(root5, text='2.Physician', font=(
            "Times New Roman", 16), bg="pink")
        l3.place(x=50, y=290)
        l4 = Label(root5, text='3.Nephrologist', font=(
            "Times New Roman", 16), bg="pink")
        l4.place(x=50, y=320)
        l5 = Label(root5, text='4.Neurologist', font=(
            "Times New Roman", 16), bg="pink")
        l5.place(x=50, y=350)
        l6 = Label(root5, text='5.Gynaecologist', font=(
            "Times New Roman", 16), bg="pink")
        l6.place(x=50, y=380)
        l7 = Label(root5, text='6.X-ray',
                   font=("Times New Roman", 16), bg="pink")
        l7.place(x=50, y=410)

        l8 = Label(root5, text='Enter your Choice :',
                   font=("Times New Roman", 16), bg="pink")
        l8.place(x=50, y=450)
        choice = Entry(root5)
        choice.place(x=230, y=450)
        l9 = Label(root5, text="Enter Date:", font=(
            "Times New Roman", 16), bg="pink")
        l9.place(x=50, y=480)

        date_ = DateEntry(root5, width=19)
        date_.place(x=230, y=480)

        l10 = Label(root5, text="Enter time :", font=(
            "Times New Roman", 16), bg="pink")
        l10.place(x=50, y=510)
        val = StringVar()
        l = ['10am', '12pm', '3pm', '5pm']
        time_ = ttk.Combobox(root5, textvariable=val, values=l, width=19)
        time_.place(x=230, y=510)
        bt = Button(root5, text="Submit", font=(
            "Times New Roman", 16), command=app_details)
        bt.place(x=550, y=560)
        bt1 = Button(root5, text="Back To Homepage", font=(
            "Times New Roman", 16), command=back)
        bt1.place(x=950, y=560)

        root5.mainloop()


def app_details():
    global q1, q2, q3, choice, date_, time_, doc, ap_no
    q1 = choice.get()
    q2 = date_.get()
    q3 = time_.get()
    if int(q1) == 1:
        a=True
        while True:
            i = "Dr. sharma"
            j = "Dr. Verma"
            q = (i, j)
            doc = random.choice(q)
            o = [i for i in range(1,11)]
            ap_no = random.choice(o)
            t=int(get_slot(name=doc,time=q3))
            if t>0:

                if alter_slot(name=doc,time=q3)>0:
                    break   
            else: 
                messagebox.showinfo("Time slot is not available")
                a=False
                break


        
        cur.execute(
            f"insert into appointment_details values('{p1}','{doc}','{q2}','{q3}','{ap_no}');")
        cur.execute(f"select * from appointment_details where id_no='{p1}';")
        data = cur.fetchall()
        lst = []
        for i in data:
            lst.append(i)
        if len(lst) == 0:
            messagebox.showerror("Error")
        elif a:
            root7 = Tk()
            root7.title("Appointment details")
            root7.geometry("500x200")
            root7.configure(bg="#D291BC")

            def ok():
                root7.destroy()
            l = Label(root7, text="Your appointment is fixed with:", bg="#D291BC")
            l.place(x=30, y=30)
            l1 = Label(root7, text=i[1], bg="#D291BC")
            l1.place(x=260, y=30)
            l2 = Label(root7, text="Date :", bg="#D291BC")
            l2.place(x=30, y=70)
            l3 = Label(root7, text=i[2], bg="#D291BC")
            l3.place(x=80, y=70)
            l4 = Label(root7, text="Time :", bg="#D291BC")
            l4.place(x=30, y=110)
            l5 = Label(root7, text=i[3], bg="#D291BC")
            l5.place(x=80, y=110)
            l6 = Label(root7, text="Appointment No. :", bg="#D291BC")
            l6.place(x=30, y=150)
            l7 = Label(root7, text=i[4], bg="#D291BC")
            l7.place(x=170, y=150)
            bt = Button(root7, text="Ok", command=ok)
            bt.place(x=230, y=170)
            root7.eval('tk::PlaceWindow . center')
            root7.mainloop() 

    if int(q1) == 2:
        a=True
        while True:
            i = ("Dr. Sidharth")
            j = ("Dr. Tendulkar ")
            q = (i, j)
            doc = random.choice(q)
            o = [i for i in range(1,11)]
            ap_no = random.choice(o)
            t=int(get_slot(name=doc,time=q3))
            if t>0:
                if alter_slot(name=doc,time=q3)>0:
                    break
            else:
                messagebox.showerror("Time slot is not available")
                a=False
                break

        cur.execute(
            f"insert into appointment_details values('{p1}','{doc}','{q2}','{q3}','{ap_no}');")
        cur.execute(f"select * from appointment_details where id_no='{p1}';")
        data = cur.fetchall()
        lst = []
        for i in data:
            lst.append(i)
        if len(lst) == 0:
            messagebox.showerror("Error")
        else:
            root7 = Tk()
            root7.title("Appointment details")
            root7.geometry("500x200")
            root7.configure(bg="#D291BC")

            def ok():
                root7.destroy()
            l = Label(root7, text="Your appointment is fixed with:", bg="#D291BC")
            l.place(x=30, y=30)
            l1 = Label(root7, text=i[1], bg="#D291BC")
            l1.place(x=260, y=30)
            l2 = Label(root7, text="Date :", bg="#D291BC")
            l2.place(x=30, y=70)
            l3 = Label(root7, text=i[2], bg="#D291BC")
            l3.place(x=80, y=70)
            l4 = Label(root7, text="Time :", bg="#D291BC")
            l4.place(x=30, y=110)
            l5 = Label(root7, text=i[3], bg="#D291BC")
            l5.place(x=80, y=110)
            l6 = Label(root7, text="Appointment No. :", bg="#D291BC")
            l6.place(x=30, y=150)
            l7 = Label(root7, text=i[4], bg="#D291BC")
            l7.place(x=170, y=150)
            bt = Button(root7, text="Ok", command=ok)
            bt.place(x=230, y=170)
            root7.eval('tk::PlaceWindow . center')
            root7.mainloop()

    if int(q1) == 3:
        a=True
        while True:
            i = ("Dr. Kumar")
            j = ("Dr. Khan ")
            q = (i, j)
            doc = random.choice(q)
            o = [i for i in range(1,11)]
            ap_no = random.choice(o)
            t=int(get_slot(name=doc,time=q3))
            if t>0:
                if alter_slot(name=doc,time=q3)>0:
                    break
            else:
                messagebox.showerror("Time slot is  not vailable")
                a=False
                break
        cur.execute(
            f"insert into appointment_details values('{p1}','{doc}','{q2}','{q3}','{ap_no}');")
        cur.execute(f"select * from appointment_details where id_no='{p1}';")
        data = cur.fetchall()
        lst = []
        for i in data:
            lst.append(i)
        if len(lst) == 0:
            messagebox.showerror("Error")
        else:
            root7 = Tk()
            root7.title("Appointment details")
            root7.geometry("500x200")
            root7.configure(bg="#D291BC")

            def ok():
                root7.destroy()
            l = Label(root7, text="Your appointment is fixed with:", bg="#D291BC")
            l.place(x=30, y=30)
            l1 = Label(root7, text=i[1], bg="#D291BC")
            l1.place(x=260, y=30)
            l2 = Label(root7, text="Date :", bg="#D291BC")
            l2.place(x=30, y=70)
            l3 = Label(root7, text=i[2], bg="#D291BC")
            l3.place(x=80, y=70)
            l4 = Label(root7, text="Time :", bg="#D291BC")
            l4.place(x=30, y=110)
            l5 = Label(root7, text=i[3], bg="#D291BC")
            l5.place(x=80, y=110)
            l6 = Label(root7, text="Appointment No. :", bg="#D291BC")
            l6.place(x=30, y=150)
            l7 = Label(root7, text=i[4], bg="#D291BC")
            l7.place(x=170, y=150)
            bt = Button(root7, text="Ok", command=ok)
            bt.place(x=230, y=170)
            root7.eval('tk::PlaceWindow . center')
            root7.mainloop()

    if int(q1) == 4:
        a=True
        while True:
            i = ("Dr. Virat")
            j = ("Dr. Leo")
            q = (i, j)
            doc = random.choice(q)
            o = [i for i in range(1,11)]
            ap_no = random.choice(o)
            t=int(get_slot(name=doc,time=q3))
            if t>0:
                if (alter_slot(name=doc,time=q3))>0:
                    break
            else:
                messagebox.showerror("Time slot is not available")
                a=False
                break
        cur.execute(
            f"insert into appointment_details values('{p1}','{doc}','{q2}','{q3}','{ap_no}');")
        cur.execute(f"select * from appointment_details where id_no='{p1}';")
        data = cur.fetchall()
        lst = []
        for i in data:
            lst.append(i)
        if len(lst) == 0:
            messagebox.showerror("Error")
        else:
            root7 = Tk()
            root7.title("Appointment details")
            root7.geometry("500x200")
            root7.configure(bg="#D291BC")

            def ok():
                root7.destroy()
            l = Label(root7, text="Your appointment is fixed with:", bg="#D291BC")
            l.place(x=30, y=30)
            l1 = Label(root7, text=i[1], bg="#D291BC")
            l1.place(x=260, y=30)
            l2 = Label(root7, text="Date :", bg="#D291BC")
            l2.place(x=30, y=70)
            l3 = Label(root7, text=i[2], bg="#D291BC")
            l3.place(x=80, y=70)
            l4 = Label(root7, text="Time :", bg="#D291BC")
            l4.place(x=30, y=110)
            l5 = Label(root7, text=i[3], bg="#D291BC")
            l5.place(x=80, y=110)
            l6 = Label(root7, text="Appointment No. :", bg="#D291BC")
            l6.place(x=30, y=150)
            l7 = Label(root7, text=i[4], bg="#D291BC")
            l7.place(x=170, y=150)
            bt = Button(root7, text="Ok", command=ok)
            bt.place(x=230, y=170)
            root7.eval('tk::PlaceWindow . center')
            root7.mainloop()

    if int(q1) == 5:
        a=True
        while True:
            i = ("Dr. Kohli ")
            j = ("Dr. singh ")
            q = (i, j)
            doc = random.choice(q)
            o = [i for i in range(1,11)]
            ap_no = random.choice(o)
            t=int(get_slot(name=doc,time=q3))
            if t>0:
                if alter_slot(name=doc,time=q3)>0:
                    break
            else:
                messagebox.showerror("Time slot is not available")
                a=False
                break

        cur.execute(
            f"insert into appointment_details values('{p1}','{doc}','{q2}','{q3}','{ap_no}');")
        cur.execute(f"select * from appointment_details where id_no='{p1}';")
        data = cur.fetchall()
        lst = []
        for i in data:
            lst.append(i)
        if len(lst) == 0:
            messagebox.showerror("Error")
        else:
            root7 = Tk()
            root7.title("Appointment details")
            root7.geometry("500x200")
            root7.configure(bg="#D291BC")

            def ok():
                root7.destroy()
            l = Label(root7, text="Your appointment is fixed with:", bg="#D291BC")
            l.place(x=30, y=30)
            l1 = Label(root7, text=i[1], bg="#D291BC")
            l1.place(x=260, y=30)
            l2 = Label(root7, text="Date :", bg="#D291BC")
            l2.place(x=30, y=70)
            l3 = Label(root7, text=i[2], bg="#D291BC")
            l3.place(x=80, y=70)
            l4 = Label(root7, text="Time :", bg="#D291BC")
            l4.place(x=30, y=110)
            l5 = Label(root7, text=i[3], bg="#D291BC")
            l5.place(x=80, y=110)
            l6 = Label(root7, text="Appointment No. :", bg="#D291BC")
            l6.place(x=30, y=150)
            l7 = Label(root7, text=i[4], bg="#D291BC")
            l7.place(x=170, y=150)
            bt = Button(root7, text="Ok", command=ok)
            bt.place(x=230, y=170)
            root7.eval('tk::PlaceWindow . center')
            root7.mainloop()

    if int(q1) == 6:
        a=True
        while True:
            i = ("Dr. Irfan ")
            j = ("Dr. John ")
            k = ("Dr. Sanjay ")
            l = ("Dr. Shahid ")
            q = (i, j, k, l)
            doc = random.choice(q)
            o = [i for i in range(1,11)]
            ap_no = random.choice(o)
            t=int(get_slot(name=doc,time=q3))
            if t>0:
                if alter_slot(name=doc,time=q3)>0:
                    break
            else:
                messagebox.showerror("Time slot is not avilable")
                a=False
                break

        cur.execute(
            f"insert into appointment_details values('{p1}','{doc}','{q2}','{q3}','{ap_no}');")
        cur.execute(f"select * from appointment_details where id_no='{p1}';")
        data = cur.fetchall()
        lst = []
        for i in data:
            lst.append(i)
        if len(lst) == 0:
            messagebox.showerror("Error")
        else:
            root7 = Tk()
            root7.title("Appointment details")
            root7.geometry("500x200")
            root7.configure(bg="#D291BC")

            def ok():
                root7.destroy()
            l = Label(root7, text="Your appointment is fixed with:", bg="#D291BC")
            l.place(x=30, y=30)
            l1 = Label(root7, text=i[1], bg="#D291BC")
            l1.place(x=260, y=30)
            l2 = Label(root7, text="Date :", bg="#D291BC")
            l2.place(x=30, y=70)
            l3 = Label(root7, text=i[2], bg="#D291BC")
            l3.place(x=80, y=70)
            l4 = Label(root7, text="Time :", bg="#D291BC")
            l4.place(x=30, y=110)
            l5 = Label(root7, text=i[3], bg="#D291BC")
            l5.place(x=80, y=110)
            l6 = Label(root7, text="Appointment No. :", bg="#D291BC")
            l6.place(x=30, y=150)
            l7 = Label(root7, text=i[4], bg="#D291BC")
            l7.place(x=170, y=150)
            root7.eval('tk::PlaceWindow . center')
            bt = Button(root7, text="Ok", command=ok)
            bt.place(x=230, y=170)
            root7.mainloop()


def mod():
    obj.root.destroy()
    obj.modification()


def modify():
    global e1, e2, p1
    p1 = obj.x1.get()
    cur.execute(f"select * from Register where id_no='{p1}';")
    lst = []
    data = cur.fetchall()
    for i in data:
        lst.append(i)

    if len(lst) == 0:
        messagebox.showerror("NO User")
    else:
        obj.root8.destroy()
        root9 = Tk()
        root9.title("Modify data ")
        w = root9.winfo_screenwidth()
        h = root9.winfo_screenheight()
        root9.geometry(f"{w}x{h}")
        root9.configure(bg="#E799A3")

        def b():
            root9.destroy()
            obj.homepage()
        l = Label(root9, text="Modify Details", font=(
            "Times New Roman", 30, "italic"), bg="#E799A3", fg="GREEN")
        l.place(x=500, y=10)
        l1 = Label(root9, text="Old Detiails:", font=(
            "Times New Roman", 18, "italic"), bg="#E799A3")
        l1.place(x=20, y=60)

        for i in data:
            name = Label(root9, text='NAME:-',
                         font=("Times New Roman", 16), bg="#E799A3")
            name.place(x=50, y=100)
            name1 = Label(root9, text=i[1], font=(
                "Times New Roman", 16), bg="#E799A3")
            name1.place(x=150, y=100)
            age = Label(root9, text='AGE:-',
                        font=("Times New Roman", 16), bg="#E799A3")
            age.place(x=50, y=130)
            age1 = Label(root9, text=i[2], font=(
                "Times New Roman", 16), bg="#E799A3")
            age1.place(x=150, y=130)
            gen = Label(root9, text='GENDER:-',
                        font=("Times New Roman", 16), bg="#E799A3")
            gen.place(x=50, y=160)
            gen1 = Label(root9, text=i[3], font=(
                "Times New Roman", 16), bg="#E799A3")
            gen1.place(x=150, y=160)
            pho = Label(root9, text='PHONE:-',
                        font=("Times New Roman", 16), bg="#E799A3")
            pho.place(x=50, y=190)
            pho1 = Label(root9, text=i[4], font=(
                "Times New Roman", 16), bg="#E799A3")
            pho1.place(x=150, y=190)
            bg = Label(root9, text='BLOOD GROUP:-',
                       font=("Times New Roman", 16), bg="#E799A3")
            bg.place(x=50, y=220)
            bg1 = Label(root9, text=i[5], font=(
                "Times New Roman", 16), bg="#E799A3")
            bg1.place(x=220, y=220)
        l = Label(root9, text="What do you want to change:", font=(
            "Times New Roman", 18, "italic"), bg="#E799A3")
        l.place(x=20, y=260)
        l1 = Label(root9, text="1. Name  ", font=(
            "Times New Roman", 16), bg="#E799A3")
        l1.place(x=50, y=310)
        l2 = Label(root9, text="2. Age ", font=(
            "Times New Roman", 16), bg="#E799A3")
        l2.place(x=50, y=340)
        l3 = Label(root9, text="3. Gender ", font=(
            "Times New Roman", 16), bg="#E799A3")
        l3.place(x=50, y=370)
        l4 = Label(root9, text="4. Phone Number ", font=(
            "Times New Roman", 16), bg="#E799A3")
        l4.place(x=50, y=400)
        l5 = Label(root9, text="5. Blood Group ", font=(
            "Times New Roman", 16), bg="#E799A3")
        l5.place(x=50, y=430)
        l6 = Label(root9, text="Enter Your Choice :-",
                   font=("Times New Roman", 16, "italic"), bg="#E799A3")
        l6.place(x=20, y=470)
        e1 = Entry(root9, font=("Times New Roman", 16))
        e1.place(x=250, y=470)
        l7 = Label(root9, text="Enter New Detail :-",
                   font=("Times New Roman", 16, "italic"), bg="#E799A3")
        l7.place(x=20, y=520)
        e2 = Entry(root9, font=("Times New Roman", 16))
        e2.place(x=250, y=520)
        bt = Button(root9, text="Submit", font=(
            "Times New Roman", 16), command=do_modify)
        bt.place(x=530, y=580)
        bt1 = Button(root9, text="Back To Homepage",
                     font=("Times New Roman", 16), command=b)
        bt1.place(x=950, y=580)
        root9.mainloop()


def do_modify():
    m1 = e1.get()
    m2 = e2.get()
    try:
        if int(m1) == 1:
            cur.execute(
                f"update  Register set name='{m2}' where id_no='{p1}';")
        if int(m1) == 2:
            cur.execute(f"update  Register set age='{m2}' where id_no='{p1}';")
        if int(m1) == 3:
            cur.execute(
                f"update  Register set gender='{m2}' where id_no='{p1}';")
        if int(m1) == 4:
            cur.execute(
                f"update  Register set ph_no='{m2}' where id_no='{p1}';")
        if int(m1) == 5:
            cur.execute(f"update  Register set bg='{m2}' where id_no='{p1}';")

        cur.execute(f"select * from Register where id_no='{p1}';")
        data = cur.fetchall()
        for i in data:
            root10 = Tk()
            root10.title("Modified Data")
            root10.geometry("500x200")
            root10.configure(bg="light green")

            def ok():
                root10.destroy()
            l = Label(root10, text="Your Data After modification is:", font=(
                "Times New Roman", 16, "italic"), bg="light green")
            l.place(x=30, y=10)
            l1 = Label(root10, text="Name:-",
                       font=("Times New Roman", 14), bg="light green")
            l1.place(x=10, y=40)
            l2 = Label(root10, text=i[1], font=(
                "Times New Roman", 14), bg="light green")
            l2.place(x=70, y=40)
            l3 = Label(root10, text="Age:-",
                       font=("Times New Roman", 14), bg="light green")
            l3.place(x=10, y=70)
            l4 = Label(root10, text=i[2], font=(
                "Times New Roman", 14), bg="light green")
            l4.place(x=60, y=70)
            l5 = Label(root10, text="Gender:-",
                       font=("Times New Roman", 14), bg="light green")
            l5.place(x=10, y=100)
            l6 = Label(root10, text=i[3], font=(
                "Times New Roman", 14), bg="light green")
            l6.place(x=80, y=100)
            l7 = Label(root10, text="Phone Number:-",
                       font=("Times New Roman", 14), bg="light green")
            l7.place(x=10, y=130)
            l8 = Label(root10, text=i[4], font=(
                "Times New Roman", 14), bg="light green")
            l8.place(x=150, y=130)
            l9 = Label(root10, text="Blood Group :-",
                       font=("Times New Roman", 14), bg="light green")
            l9.place(x=10, y=160)
            l10 = Label(root10, text=i[5], font=(
                "Times New Roman", 14), bg="light green")
            l10.place(x=140, y=160)
            b = Button(root10, text="OK", command=ok)
            b.place(x=200, y=170)

            root10.eval('tk::PlaceWindow . center')
            root10.mainloop()
    except:
        messagebox.showerror("Error")


def get_slot(name, time):
    try:
        cur.execute(f'select time_{time} from slots where name="{name}";')
        return cur.fetchall()[0][0]
    except Exception as e:
        print(e)
        return -999


def alter_doc(doc_dict):
    for i in list(doc_dict.values()):
        for j in i:
            try:
                cur.execute(f"insert into slots values('{j}',10,10,10,10);")
                conn.commit()
            except:
                pass


def alter_slot(name, time):
    name+=" "
    try:
        cur.execute(f'select time_{time} from slots where name="{name}";')
        temp=cur.fetchall()[0][0]
        if temp>0:
            cur.execute(
                f'update slots set time_{time} ={temp-1} where name ="{name}";')
            conn.commit()
            return 1
        else:
            return -999
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # calling homepage
    obj.homepage()
    conn.commit()
    conn.close()