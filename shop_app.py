from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password='',database='product')
mycursor=db.cursor()

a=Tk()
a.title('product')
a.geometry('900x600')
a.configure(bg='purple')
a.resizable(0,0)
la_head=Label(a, text='Welcome To My Shop',bg='purple',fg='white',font=('Times new roman',26,'bold'))
la_head.place(x=200,y=30)

img_shop=PhotoImage(file='shopping1.png')
img_search1=PhotoImage(file='search4.png')

def clear():
    en.delete(0, END)
global product

def add():
    global product
    def clear1():
        en_no.delete(0,END)
        en_name.delete(0,END)
        en_price.delete(0,END)
        en_details.delete(0,END)
    b=Toplevel(a)
    b.geometry('600x400')
    b.configure(bg='green')
    b.resizable(0,0)
    l_head=Label(b,text='ADD PRODUCTS',bg='green',fg='white',font=('rockwell',23,'bold')).pack()
    la_prno=Label(b,text='Product Number',bg='green',fg='white',font=('times new roman',16,'bold')).place(x=20,y=90)
    la_prname=Label(b,text='Product Name',bg='green',fg='white',font=('times new roman',16,'bold')).place(x=20,y=140)
    la_prprice=Label(b,text='Product Price',bg='green',fg='white',font=('times new roman',16,'bold')).place(x=20,y=190)
    la_prdetails=Label(b,text='Product Quantity',bg='green',fg='white',font=('times new roman',16,'bold')).place(x=20,y=240)
    en_no=Entry(b,width=15,font=('arial',16),bd=0)
    en_name=Entry(b,width=15,font=('arial',16),bd=0)
    en_price=Entry(b,width=15,font=('arial',16),bd=0)
    en_details=Entry(b,width=15,font=('arial',16),bd=0)
    en_no.place(x=200,y=90)
    en_name.place(x=200,y=140)
    en_price.place(x=200,y=190)
    en_details.place(x=200,y=240)
    Frame(b,width=180,height=2,bg='black').place(x=200,y=116)
    Frame(b,width=180,height=2,bg='black').place(x=200,y=166)
    Frame(b,width=180,height=2,bg='black').place(x=200,y=216)
    Frame(b,width=180,height=2,bg='black').place(x=200,y=266)
    product=[]
    def process():
        no=Entry.get(en_no)
        name=Entry.get(en_name)
        price=Entry.get(en_price)
        details=Entry.get(en_details)
        pr_total=[no,name,price,details]
        product.append(pr_total)
        sql="insert into add_product (number,name,price,details) values (%s,%s,%s,%s)"
        val=(no,name,price,details)
        mycursor.execute(sql,val)
        db.commit()
        print(product)
        clear1()
    btn_sub=Button(b,command=process,text='Submit',bg='black',fg='white',font=('arial',16),activeforeground='black',activebackground='white',bd=4)
    btn_sub.place(x=150,y=300)

def view():
    global product
    c=Toplevel(a)
    c.geometry('750x350')
    c.configure(bg='green')
    mycursor.execute('select * from add_product')
    val=mycursor.fetchall()
    x=ttk.Treeview(c,selectmode='browse')
    x['columns']=('1','2','3','4')
    x['show']='headings'
    x.column('1',width=50,anchor='c')
    x.column('2',width=200,anchor='c')
    x.column('3',width=200,anchor='c')
    x.column('4',width=200,anchor='c')
    x.heading('1',text='No. ')
    x.heading('2',text='Name')
    x.heading('3',text='Price')
    x.heading('4',text='Details')
    for dt in val:
        x.insert('','end',values=(dt[0],dt[1],dt[2],dt[3],))
    x.pack()

def update():
    pass

def delete():
    global product
    en1=Entry.get(en)
    mycursor.execute('delete from add_product where number ={}'.format(en1))
    db.commit()
    clear()
def search():
    en_1=Entry.get(en)
    mycursor.execute('select * from add_product where number ={}'.format(en_1))
    v=mycursor.fetchall()
    clear()
    for i in v:
        print(i)
        msg.showinfo('answer',i)

btn_new=Button(a,text='New Project',command=add,bd=5,bg='dark blue',fg='white',width=10,height=1,font=('monotype corsiva',15,'bold'))
btn_view=Button(a,text='List View',command=view,bd=5,bg='dark blue',fg='white',width=10,height=1,font=('monotype corsiva',15,'bold'))
btn_update=Button(a,text='Update',command=update,bd=5,bg='dark blue',fg='white',width=10,height=1,font=('monotype corsiva',15,'bold'))
btn_del=Button(a,text='Delete',command=delete,bd=5,bg='dark blue',fg='white',width=10,height=1,font=('monotype corsiva',15,'bold'))
btn_search=Button(a,text='Search',command=search,bd=5,bg='dark blue',fg='white',width=10,height=1,font=('monotype corsiva',15,'bold'))
btn_search1=Button(a,command=search,image=img_search1,bd=0)

btn_new.place(x=20,y=110)
btn_view.place(x=20,y=190)
btn_update.place(x=20,y=270)
btn_del.place(x=20,y=350)
btn_search.place(x=20,y=430)
btn_search1.place(x=845,y=60)

en=Entry(a,width=15,font=('arial',16),highlightthickness=3,bd=1,highlightcolor='white')
en.config(highlightbackground='blue',highlightcolor='black')
en.place(x=650,y=60)
main_pic=Label(a,image=img_shop)
main_pic.place(x=200,y=112)
a.mainloop()

