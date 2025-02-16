
import sqlite3
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import ctypes
try: ctypes.windll.shcore.SetProcessDpiAwareness(1)
except: print("error: can't set the Dpi Awareness")

aps=Tk()
aps.geometry("1420x692+0+0")
aps.resizable(False,False)
#aps.iconbitmap('icon path')
aps.title('my aps')

#__________________Frames________________________________________________________________________

frame_1=Frame(aps,width=300,height=700,background='#7e7cf2')
frame_1.place(x=0,y=0)
frame_2=Frame(aps,width=1108,height=50,background='#7e7cf2')
frame_2.place(x=301,y=0)
frame_3=Frame(aps,width=1108,height=648,background='#c1c1c1')
frame_3.place(x=301,y=51)
 
#__________________Labels________________________________________________________________________

label_frame1=LabelFrame(frame_1,text='<  Control  >',bg='#7e7cf2',fg='red',width=280,height=190,bd=3)
label_frame1.place(x=5,y=478)
label1=Label(frame_1,text='Welcome',bg='#7e7cf2',fg='red',font=('tajwal',20,'bold'))
label1.place(x=50,y=12)
label2=Label(frame_1,text='Full Name  :',bg='#7e7cf2',fg='black')
label2.place(x=15,y=102)
label3=Label(frame_1,text='Gander  :',bg='#7e7cf2',fg='black')
label3.place(x=15,y=152)
label4=Label(frame_1,text='Age  :',bg='#7e7cf2',fg='black')
label4.place(x=15,y=202)
label5=Label(frame_1,text='Phone Namber  :',bg='#7e7cf2',fg='black')
label5.place(x=15,y=252)
label6=Label(frame_1,text='Adress  :',bg='#7e7cf2',fg='black')
label6.place(x=15,y=302)
label7=Label(frame_1,text='Gmail  :',bg='#7e7cf2',fg='black')
label7.place(x=15,y=352)
label8=Label(frame_1,text='ID for update  :',fg='red',bg='#7e7cf2')
label8.place(x=15,y=403)
Time_Label=Label(frame_2,background='#7e7cf2')
Time_Label.place(x=1000,y=15)

#__________________Entrys________________________________________________________________________

style=ttk.Style()
style.map('Treeview',background=[('selected','blue')])
style.configure('TRadiobutton',background='#7e7cf2') 
entry_2=StringVar()
ttk.Radiobutton(frame_1, text='Male',value='Male',variable=entry_2).place(x=30,y=180)
ttk.Radiobutton(frame_1, text='Fmale',value='Fmale',variable=entry_2).place(x=120,y=180)

entry_10=StringVar();entry_30=StringVar();entry_40=StringVar();entry_50=StringVar()
entry_60=StringVar();entry_70=StringVar();entry_80=StringVar();entry_90=StringVar()

entry_1=Entry(frame_1,textvariable=entry_10,width=25,justify='center')
entry_1.place(x=15,y=130)
entry_3=Entry(frame_1,textvariable=entry_30,width=25,justify='center')
entry_3.place(x=15,y=230)
entry_4=Entry(frame_1,textvariable=entry_40,width=25,justify='center')
entry_4.place(x=15,y=280)
entry_5=Entry(frame_1,textvariable=entry_50,width=25,justify='center')
entry_5.place(x=15,y=330)
entry_6=Entry(frame_1,textvariable=entry_60,width=25,justify='center')
entry_6.place(x=15,y=380)
entry_7=Entry(frame_1,textvariable=entry_70,width=25,justify='center',fg='blue')
entry_7.place(x=15,y=430)
entry_8=Entry(frame_2,textvariable=entry_80,width=25,justify='center')
entry_8.place(x=180,y=10)
entry_9=Entry(frame_2,textvariable=entry_90,width=25,justify='center')
entry_9.place(x=650,y=10) 

#__________________buttons________________________________________________________________________

button_1=Button(frame_1,text='√ Save',width=25,padx=1,pady=1,bd=1,cursor='hand2')
button_1.place(x=13,y=540)
button_2=Button(frame_1,text='© Update',width=25,padx=1,pady=1,bd=1,cursor='hand2')
button_2.place(x=13,y=590)
button_4=Button(frame_2,text='⎋ Searsh by name',padx=0,pady=0,bd=1,cursor='hand2')
button_4.place(x=10,y=5)
button_5=Button(frame_2,text='〤 Delete by ID',padx=0,pady=0,bd=1,cursor='hand2')
button_5.place(x=500,y=5)
 
#__________________fonctions________________________________________________________________________
 
class DBConect :
    def __init__(self):
        self.rot=sqlite3.connect('Data_x.db')
        self.rot.row_factory=sqlite3.Row
        self.rot.execute('create table if not exists Data(ID integer primary key autoincrement ,name text,Gander text,age text,namber text,adress text,gmail text)')
        self.rot.commit()
    def Add(self,name,Gander,age,namber,adress,gmail):
        self.rot.execute('insert into Data(name,Gander,age,namber,adress,gmail) values(?,?,?,?,?,?)' , (name,Gander,age,namber,adress,gmail))
        self.rot.commit()
        return 'requste is saved' 
    def Update(self,name,Gander,age,namber,adress,gmail,ID):
        self.rot.execute('UPDATE Data set name=? , Gander=? , age=? ,namber=? , adress=? , gmail=? where ID=?',(name,Gander,age,namber,adress,gmail,ID))
        self.rot.commit()
        return 'Record is Updated'
    def Delete(self,ID):
        self.rot.execute('DELETE from Data where ID={}'.format(ID))
        self.rot.commit()
        return 'Record is deleted'
    def List_Requst(self):
        List=self.rot.execute('select * from Data')
        return List 
    def Search(self,name):
        Search=self.rot.execute("SELECT * from Data where name Like '%{}%'".format(name))
        print(Search)
        return Search
    def Get_ID(self,name):
        Get_ID1=self.rot.execute("SELECT ID , name FROM Data WHERE name LIKE '%{}%'".format(name))
        return Get_ID1
    def All_Name(self):
        allname=self.rot.execute("SELECT * FROM Data WHERE name")
        return allname
DBC=DBConect()
cur=DBC.All_Name()
for row in cur:
    print(row)

def Treeview():
    def Get_Cursor(event):
        cursor_row=tv.focus() 
        contents=tv.item(cursor_row)
        row=contents['values']
        row1=contents['text']
        entry_10.set(row[0])
        entry_2.set(row[1])
        entry_30.set(row[2])
        entry_40.set(row[3])
        entry_50.set(row[4])
        entry_60.set(row[5])    
        entry_70.set(row1)
        entry_90.set(row1)
    scroll_y=ttk.Scrollbar(frame_3,orient=VERTICAL)
    scroll_y.place(x=1094,y=1,height=618,width=14)   
    tv=ttk.Treeview(frame_3)
    tv.place(x=1,y=0)
    tv.configure(columns=('#Name','#Gander','#Age','#Namber','#Adress','#Gmail'),height=30,yscrollcommand=scroll_y.set)
    tv.column('#0',width=50)
    tv.column('#Name',width=200)
    tv.column('#Gander',width=150)
    tv.column('#Age',width=150)
    tv.column('#Namber',width=153)
    tv.column('#Adress',width=200)
    tv.column('#Gmail',width=188)
    tv.heading('#0',text='ID')
    tv.heading('#Name',text='Name')
    tv.heading('#Gander',text='Gander')
    tv.heading('#Age',text='Age')
    tv.heading('#Namber',text='Namber')
    tv.heading('#Adress',text='Adress')
    tv.heading('#Gmail',text='Gmail')
    tv.bind("<ButtonRelease-1>",Get_Cursor)
    scroll_y.config(command=tv.yview)
    listR=DBC.List_Requst()
    for row in listR:
        tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
        tv.set('#{}'.format(row['ID']),'#Name', row['Name'])
        tv.set('#{}'.format(row['ID']),'#Gander', row['Gander'])
        tv.set('#{}'.format(row['ID']),'#Age', row['Age'])
        tv.set('#{}'.format(row['ID']),'#Namber', row['Namber'])
        tv.set('#{}'.format(row['ID']),'#Adress', row['Adress'])
        tv.set('#{}'.format(row['ID']),'#Gmail', row['Gmail'])
Treeview()
def Time_1 ():
    Time_=time.strftime('%H:%M:%S %p')
    Time_Label.config(text=Time_)
    Time_Label.after(1000,Time_1)
Time_1()

def Save_Data():
    s1='{}'.format(entry_1.get())
    s2='{}'.format(entry_2.get())
    s3='{}'.format(entry_3.get())
    s4='{}'.format(entry_4.get())
    s5='{}'.format(entry_5.get())
    s6='{}'.format(entry_6.get())
    try:
        s1 = int(s1)
        if s1:
            messagebox.showwarning(title='Warning',message='You have to insert the rel name!')
    except:
        try:
            s3 == int(s3) 
            
            list=DBC.List_Requst()
            rows=[]
            for row in list:
                rows.append(row['name'])

            if s1 == '' or s1 == '' or s2 == '' or s3 == '' or s4 == '' or s5 == '' or s6 == '' :
                messagebox.showerror(title='Erorr',message='there is some entry is vide')

            elif s1 in rows :
                messagebox.showwarning(title='Warning',message='This Name exested !')
                
            else:
                d_b=DBC.Add(s1,s2,s3,s4,s5,s6)
                messagebox.showinfo(title='Add info',message=d_b)
                entry_1.delete(0,'end')
                entry_3.delete(0,'end')
                entry_4.delete(0,'end')
                entry_5.delete(0,'end')
                entry_6.delete(0,'end')
                entry_2.set('')
                Treeview()
        except:
            if s1 == '' or s1 == '' or s2 == '' or s3 == '' or s4 == '' or s5 == '' or s6 == '' :
                messagebox.showerror(title='Erorr',message='there is some entry is vide')
            else:
                messagebox.showwarning(title='Warning',message='enter the rel Age!')

def Up_Date (): 
    s1='{}'.format(entry_1.get())
    s2='{}'.format(entry_2.get())
    s3='{}'.format(entry_3.get())
    s4='{}'.format(entry_4.get())
    s5='{}'.format(entry_5.get())
    s6='{}'.format(entry_6.get())
    s7='{}'.format(entry_7.get())
    try:
        s1 = int(s1)
        if s1:
            messagebox.showwarning(title='Warning',message='You have to insert the rel name!')
    except:
        try:
            s3==int(s3)

            if s1 == '' or s1 == '' or s2 == '' or s3 == '' or s4 == '' or s5 == '' or s6 == '' or s7 == '':
                messagebox.showerror(title='Erorr',message='there is some entry is vide')
            else:
                up_date=DBC.Update(s1,s2,s3,s4,s5,s6,s7)
                messagebox.showinfo(title='Update info',message=up_date)
                entry_1.delete(0,'end')
                entry_3.delete(0,'end')
                entry_4.delete(0,'end')
                entry_5.delete(0,'end')
                entry_6.delete(0,'end')
                entry_7.delete(0,'end')
                entry_2.set('')
                Treeview()
        except:
            messagebox.showwarning(title='warning',message='enter the rel Age')
def Delete():
    vr='{}'.format(entry_9.get())
    if vr== '':
        messagebox.showwarning(title='Warning',message='Enter ID for Deleted Requste! ')
    else:  
        mesage=messagebox.askquestion(title='Delete',message='are you sure ?')
        if mesage == 'yes':
            DBC.Delete('{}'.format(entry_9.get()))
            entry_9.delete(0,'end')
            Treeview()
        else:
            pass
def Searsh_by_name():
    var_1='{}'.format(entry_8.get())
    if var_1=='':
        messagebox.showinfo(title='?',message='plase select the real name!')
    else: 
        app=Tk()
        app.geometry('700x187+300+200')
        app.resizable(False,False)
        app.title('Searshed')
        #app.iconbitmap('C:\\Users\\khalouk\\Desktop\\project\\write.ico')  

        tv1=ttk.Treeview(app)
        tv1.place(x=1,y=1)
        tv1.configure(columns=('#Name','#gander','#Age','#Namber','#Adress','#Gmail'),height=8)
        
        tv1.column('#0',width=66)
        tv1.column('#Name',width=100)
        tv1.column('#gander',width=100)
        tv1.column('#Age',width=100)
        tv1.column('#Namber',width=100)
        tv1.column('#Adress',width=100)
        tv1.column('#Gmail',width=130)
        tv1.heading('#0',text='ID')
        tv1.heading('#Name',text='Name')
        tv1.heading('#gander',text='gander')
        tv1.heading('#Age',text='Age')
        tv1.heading('#Namber',text='Namber')
        tv1.heading('#Adress',text='Adress')
        tv1.heading('#Gmail',text='Gmail')
        listR1=DBC.Search(var_1)
        for row in listR1:
            tv1.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv1.set('#{}'.format(row['ID']),'#Name', row['Name'])
            tv1.set('#{}'.format(row['ID']),'#gander', row['gander'])
            tv1.set('#{}'.format(row['ID']),'#Age', row['Age'])
            tv1.set('#{}'.format(row['ID']),'#Namber', row['Namber'])
            tv1.set('#{}'.format(row['ID']),'#Adress', row['Adress'])
            tv1.set('#{}'.format(row['ID']),'#Gmail', row['Gmail'])
        entry_8.delete(0,'end')
    app.mainloop()
def About_Us():
    ap=Tk()
    ap.geometry('400x200+450+250')
    ap.config(background='white')
    ap.resizable(False,False)
    ap.title('About Us')
    #ap.iconbitmap('C:\\Users\\khalouk\\Desktop\\project\\write.ico')
    var2='''this app is created by Mr.Youssef khalouk 
    and the app is for save student information '''
    ttk.Label(ap,text=var2,background='white',foreground='blue',font=('tajwal',13,'bold')).place(x=10,y=50)
    ttk.Label(ap,text='facebook : Youss Ef').place(x=290,y=180)
    ap.mainloop()

#__________________Themes___________________________________________________________________________

def Light_mode_1():
    label_frame1.config(background='#7e7cf2')
    frame_1.config(background='#7e7cf2')
    frame_2.config(background='#7e7cf2')
    frame_3.config(background='white') 
    Time_Label.config(bg='#7e7cf2',fg='black')
    label1.config(bg='#7e7cf2')
    label2.config(bg='#7e7cf2',fg='black')
    label3.config(bg='#7e7cf2',fg='black')
    label4.config(bg='#7e7cf2',fg='black')
    label5.config(bg='#7e7cf2',fg='black')
    label6.config(bg='#7e7cf2',fg='black')
    label7.config(bg='#7e7cf2',fg='black')
    label8.config(bg='#7e7cf2')
    button_1.config(bg='white',fg='black')
    button_2.config(bg='white',fg='black')
    button_4.config(bg='white',fg='black')
    button_5.config(bg='white',fg='black')
    entry_1.config(bg='white',fg='black')
    entry_3.config(bg='white',fg='black')
    entry_4.config(bg='white',fg='black')
    entry_5.config(bg='white',fg='black')
    entry_6.config(bg='white',fg='black')
    entry_7.config(bg='white',fg='black')
    entry_8.config(bg='white',fg='black')
    entry_9.config(bg='white',fg='black')
    style=ttk.Style()
    style.theme_use('vista')
    style.configure('TRadiobutton',background='#7e7cf2',foreground='black')
    style.configure('Treeview',background='white',foreground='black',fieldbackground='white')
    style.map('Treeview',background=[('selected','blue')])
def Light_mode_2():
    label_frame1.config(background='#63D471')
    frame_1.config(background='#63D471')
    frame_2.config(background='#63D471')
    frame_3.config(background='#63D471') 
    Time_Label.config(bg='#63D471',fg='black')
    label1.config(bg='#63D471')
    label2.config(bg='#63D471',fg='black')
    label3.config(bg='#63D471',fg='black')
    label4.config(bg='#63D471',fg='black')
    label5.config(bg='#63D471',fg='black')
    label6.config(bg='#63D471',fg='black')
    label7.config(bg='#63D471',fg='black')
    label8.config(bg='#63D471')
    button_1.config(bg='#7ED5C5',fg='black')
    button_2.config(bg='#7ED5C5',fg='black')
    button_4.config(bg='#7ED5C5',fg='black')
    button_5.config(bg='#7ED5C5',fg='black')
    entry_1.config(bg='white',fg='black')
    entry_3.config(bg='white',fg='black')
    entry_4.config(bg='white',fg='black')
    entry_5.config(bg='white',fg='black')
    entry_6.config(bg='white',fg='black')
    entry_7.config(bg='white',fg='black')
    entry_8.config(bg='white',fg='black')
    entry_9.config(bg='white',fg='black')
    style=ttk.Style()
    style.theme_use('default')
    style.configure('TRadiobutton',background='#63D471',foreground='black')
    style.configure('Treeview',background='#D8C794',foreground='blue',fieldbackground='#D8C794')
    style.map('Treeview',background=[('selected','gray')])
def Dark_mode():
    label_frame1.config(background='#0d0225')
    Time_Label.config(bg='#0d0225',fg='white')
    frame_1.config(background='#0d0225')
    frame_2.config(background='#0d0225')
    frame_3.config(background='black')
    label1.config(bg='#0d0225')
    label2.config(bg='#0d0225',fg='white')
    label3.config(bg='#0d0225',fg='white')
    label4.config(bg='#0d0225',fg='white')
    label5.config(bg='#0d0225',fg='white')
    label6.config(bg='#0d0225',fg='white')
    label7.config(bg='#0d0225',fg='white')
    label8.config(bg='#0d0225')
    button_1.config(bg='#8FDEC2',fg='black')
    button_2.config(bg='#8FDEC2',fg='black')
    button_4.config(bg='#8FDEC2',fg='black')
    button_5.config(bg='#8FDEC2',fg='black')
    entry_1.config(bg='#303030',fg='#13FF00')
    entry_3.config(bg='#303030',fg='#13FF00')
    entry_4.config(bg='#303030',fg='#13FF00')
    entry_5.config(bg='#303030',fg='#13FF00')
    entry_6.config(bg='#303030',fg='#13FF00')
    entry_7.config(bg='#303030',fg='#13FF00')
    entry_8.config(bg='#303030',fg='#13FF00')
    entry_9.config(bg='#303030',fg='#13FF00')
    style=ttk.Style()
    style.theme_use('default')
    style.configure('TRadiobutton',background='#0d0225',foreground='white')
    style.configure('Treeview',background='#242524',foreground='white',fieldbackground='#242524')
    style.map('Treeview',background=[('selected','green')])

#__________________Menu____________________________________________________________________________

menu_bar=Menu(aps)
aps.config(menu=menu_bar)

file_menu_0=Menu(menu_bar,tearoff=0)

menu_bar.add_cascade(label='File',menu=file_menu_0)
file_menu_0.add_command(label='Open')
file_menu_0.add_command(label='Save')
file_menu_0.add_cascade(label='Other')
file_menu_0.add_separator()

file_menu_0.add_command(label='Exit',command=exit)

file_menu_1=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Theme',menu=file_menu_1)
file_menu_1.add_command(label='Light mode 1',command=Light_mode_1)
file_menu_1.add_command(label='Light mode 2',command=Light_mode_2)
file_menu_1.add_command(label='Dark mode',command=Dark_mode)

file_menu_2=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='About',menu=file_menu_2)
file_menu_2.add_command(label='About Us',command=About_Us)

#__________________commands____________________________________________________________________

button_1.config(command=Save_Data)
button_2.config(command=Up_Date)
button_5.config(command=Delete)
button_4.config(command=Searsh_by_name)

aps.mainloop()


