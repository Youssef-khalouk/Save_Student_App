import sqlite3
class DBConect :
    def __init__(self):
        self.rot=sqlite3.connect('Data_x.db')
        self.rot.row_factory=sqlite3.Row
        self.rot.execute('create table if not exists Data(ID integer primary key autoincrement ,name text,Gander text,age text,namber text,adress text,gmail text)')
        self.rot.commit()
    def Add(self,name,Gander,age,namber,adress,gmail):
        self.rot.execute('insert into Data(name,Gander,age,namber,adress,gmail) values(?,?,?,?,?,?)' , (name,Gander,age,namber,adress,gmail))
        self.rot.commit()

DBC=DBConect()
import random
import string
var11=0
while var11<200:
    s1=list(string.ascii_uppercase)
    s2=list(string.ascii_lowercase)
    s3=list(string.digits)
    s4=['Male','Fmale']
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)
    s11=s1[1]+s2[2]+s2[3]+s2[4]+s2[5]+' '+s1[6]+s2[7]+s2[8]+s2[9]+s2[10]
    s22=s4[0]
    s33=s3[0]+s3[1]
    s44='+121'+s3[4]+s3[5]+s3[6]+s3[7]+s3[8]+s3[9]+s3[3]
    s55='morocco'
    s66=s1[0]+s2[6]+s2[9]+s2[12]+s2[13]+s2[14]+'@gmail.com'

    DBC.Add(s11,s22,s33,s44,s55,s66)
    var11+=1