from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mycon

window_main = Tk()
window_main = window_main
window_main.geometry("1600x950+0+0")
window_main.title("Main Program")
window_main.configure(bg="White")
#window_main.state('zoomed')

bg = ImageTk.PhotoImage(file=r"images\bg_crud.jpg")
lbl_bg = Label(window_main, image=bg)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame_main_sub = Frame(window_main, bg="NavajoWhite2")
frame_main_sub.place(width=930, height=530, anchor="center", relx=.5, rely=.33)
frame_main = Frame(window_main, bg="White")
frame_main.place(width=900, height=500, anchor="center", relx=.5, rely=.33)



def GetValue(event):

    et_id.config(state="normal")
    et_id.delete(0, END)
    et_name.delete(0, END)
    et_surn.delete(0, END)
    combo_gen.delete(0, END)
    et_phone.delete(0, END)
    et_email.delete(0, END)
    row_id = listBox_emp.selection()[0]
    select = listBox_emp.set(row_id)
    et_id.insert(0, select['ID'])
    et_name.insert(0, select['Name'])
    et_surn.insert(0, select['Surname'])
    combo_gen.insert(0, select['Gen'])
    et_phone.insert(0, select['Phone'])
    et_email.insert(0, select['Email'])
    et_id.config(state="disabled")


def Add_emp():
    ename = name_value.get()
    esur = surn_value.get()
    egen = gen_value.get()
    ephone = phone_value.get()
    eemail = email_value.get()

    if ename == "" or esur == "" or egen == "None" or ephone == "" or eemail == "":
        messagebox.showerror("Error", "Please fill in the blank again.", parent=window_main)
    else:
        try:
            conn = mycon.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='password1234',
                                 database='dbo.employee')
            cs1 = conn.cursor()

            cs1.execute("INSERT INTO employee (emname,surname,gen,phone,email,pass) VALUES ('"+ename+"','"+esur+"','"+egen+"','"+ephone+"','"+eemail+"','""')")
            cs1.execute("commit");
            conn.close();
            messagebox.showinfo("Success", "Record Add is successful...!!", parent=window_main)
            fetch_data()

            et_id.delete(0, END)
            et_name.delete(0, END)
            et_surn.delete(0, END)
            combo_gen.delete(0, END)
            et_phone.delete(0, END)
            et_email.delete(0, END)


        except Exception as e:
            print(e)
def fetch_data():
    conn = mycon.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='password1234',
                         database='dbo.employee')
    cs1 = conn.cursor()
    cs1.execute("SELECT id,emname,surname,gen,phone,email FROM employee")
    rows = cs1.fetchall()
    if len(rows)!=0:
        listBox_emp.delete(*listBox_emp.get_children())
        for row in rows:
            listBox_emp.insert('',END, values=row)
        cs1.execute("commit");
    conn.close()

def Update_emp():
    ename = name_value.get()
    esur = surn_value.get()
    egen = gen_value.get()
    ephone = phone_value.get()
    eemail = email_value.get()

    if ename == "" or esur == "" or egen == "None" or ephone == "" or eemail == "":
        messagebox.showerror("Error", "Please fill in the blank again.", parent=window_main)
    else:
        try:
            conn = mycon.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='password1234',
                                database='dbo.employee')
            cs1 = conn.cursor()
            cs1.execute("Update employee set emname=%s,surname=%s,gen=%s,phone=%s,email=%s where id=%s",(ename,esur,egen,ephone,eemail,et_id.get()))
            cs1.execute("commit");
            conn.close();
            messagebox.showinfo("Success", "Record Update is successful...!!", parent=window_main)
            fetch_data()

            et_id.delete(0, END)
            et_name.delete(0, END)
            et_surn.delete(0, END)
            combo_gen.delete(0, END)
            et_phone.delete(0, END)
            et_email.delete(0, END)
        except Exception as e:
            print(e)

def Delete():
    conn = mycon.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='password1234',
                         database='dbo.employee')
    cs1 = conn.cursor()
    try:
        cs1.execute("DELETE from employee where id= "+ et_id.get())
        cs1.execute("commit");
        conn.close();
        messagebox.showinfo("Success", "Record Delete is successful...!!", parent=window_main)
        fetch_data()

        et_id.delete(0, END)
        et_name.delete(0, END)
        et_surn.delete(0, END)
        combo_gen.delete(0, END)
        et_phone.delete(0, END)
        et_email.delete(0, END)

    except Exception as e:
        print(e)

def show_db():
    try :
        conn = mycon.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='password1234',
                             database='dbo.employee')
        cs1 = conn.cursor()
        cs1.execute("SELECT id,emname,surname,gen,phone,email FROM employee ")
        records = cs1.fetchall()
        #print(records)

        for i, (id, emname, surname, gen, phone, email) in enumerate(records,start=1):
            listBox_emp.insert("","end", values=(id, emname, surname, gen, phone, email))
            conn.close();

    except Exception as e:
        print(e)
Label(frame_main, text="Employee Management System", font=("Impact", 30, "bold"), fg="Green",bg="white").place(relx=.5,rely=.15,anchor="s")
Label(frame_main, text="Emp ID", font=("Impact", 20), fg="black", bg="White").place(relx=.08,rely=.25)
Label(frame_main, text="Name", font=("Impact", 20), fg="black", bg="White").place(relx=.08,rely=.37)
Label(frame_main, text="Surname", font=("Impact", 20), fg="black", bg="White").place(relx=.08,rely=.49)
Label(frame_main, text="Gen", font=("Impact", 20), fg="black", bg="White").place(relx=.08,rely=.61)
Label(frame_main, text="Phone", font=("Impact", 20), fg="black", bg="White").place(relx=.08,rely=.73)
Label(frame_main, text="Email", font=("Impact", 20), fg="black", bg="White").place(relx=.08,rely=.85)

global id_value,name_value,surn_value,gen_value,phone_value,email_value
id_value= StringVar()
name_value = StringVar()
surn_value = StringVar()
gen_value = StringVar(value="None")
phone_value = StringVar()
email_value = StringVar()


et_id = Entry(frame_main ,state="disabled",textvariable=id_value, font = ("tahoma", 20), width = 15,fg="Black", bg = "lightgrey")
et_id.place(relx=.21,rely=.25)
et_name = Entry(frame_main,textvariable = name_value, font = ("tahoma", 20), width = 25, bg = "white")
et_name.place(relx=.21,rely=.37)
et_surn = Entry(frame_main,textvariable = surn_value, font = ("tahoma", 20), width = 25, bg = "white")
et_surn.place(relx=.21,rely=.49)
combo_gen = ttk.Combobox(frame_main, textvariable = gen_value, font = ("tahoma", 20), width = 10,)
combo_gen["values"] = ("Male", "Female")
combo_gen.place(relx=.21,rely=.61)
et_phone = Entry(frame_main,textvariable = phone_value, font = ("tahoma", 20), width = 25, bg = "white")
et_phone.place(relx=.21,rely=.73)
et_email = Entry(frame_main,textvariable = email_value, font = ("tahoma", 20), width = 25, bg = "white")
et_email.place(relx=.21,rely=.85)

btn_add = Button(frame_main, text="+Add", command = Add_emp, font = ("Impact", 25),
                                width=12,fg="AntiqueWhite1",bg="burlywood4").place(relx=.7,rely=.3)
btn_update = Button(frame_main, text="Update", command = Update_emp, font = ("Impact", 25),
                                width=12,fg="AntiqueWhite1",bg="burlywood4").place(relx=.7,rely=.5)
btn_delete = Button(frame_main, text="Delete", command = Delete, font = ("Impact", 25),
                                width=12,fg="AntiqueWhite1",bg="burlywood4").place(relx=.7,rely=.7)

frame_tree_sub = Frame(window_main, bg="NavajoWhite2")
frame_tree_sub.place(width=930, height=300, anchor="center", relx=.5, rely=.80)
frame_tree = Frame(window_main, bg="NavajoWhite2")
frame_tree.place(width=900, height=270, anchor="center", relx=.5, rely=.80)

scroll_x = Scrollbar(frame_tree,orient=HORIZONTAL)
scroll_y = Scrollbar(frame_tree,orient=VERTICAL)
cols = ("ID","Name","Surname","Gen","Phone","Email")
listBox_emp = ttk.Treeview(frame_tree, columns=cols, show='headings',xscrollcommand=scroll_x,yscrollcommand=scroll_y)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=listBox_emp.xview)
scroll_y.config(command=listBox_emp.yview)

for col in cols:
    listBox_emp.heading(col, text=col)
    listBox_emp.column(col, anchor="w",width=150)
    listBox_emp.column("ID", anchor=CENTER,width=80)
    listBox_emp.column("Email",width=200)
    listBox_emp.column("Gen", width=100)
    listBox_emp.pack(fill=BOTH ,expand=1)

style = ttk.Style()
style.theme_use("alt")
style.configure('Treeview',
                background="grey94",
                foreground="White",
                rowheight=25,
                fieldbackground="grey94"
                )
style.map('Treeview',
        background=[('selected','black')])

show_db()
listBox_emp.bind('<Double-Button-1>', GetValue)

window_main.mainloop()