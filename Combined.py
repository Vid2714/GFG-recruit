import mysql.connector as sqltor
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

sqlcon = sqltor.connect(host = 'localhost',user = 'root',password='vid316',database='library')
cursor = sqlcon.cursor()

root = Tk()#main window
root.title("Home Page")
root.minsize(width=400,height=400)
root.geometry("660x500")#height x width 

name_var=tk.StringVar()
passw_var=tk.StringVar()
    
def lglib():
    login("Admin")
    
def lgmem():
    login("Member")
    
def login(pers):
    global Login
    Login = Toplevel(root)
    Login.geometry("660x500")
    Login.title("Login Page")

    #background()
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(Login, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    
    headingFrame1 = Frame(Login,bg="orange",bd=3)#for box
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)#rel enters value as a fraction of parent widget
    headingLabel = Label(headingFrame1, text="LOGIN "+pers, bg='brown', fg='white', font=('Courier',26))#for text inside box
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    global user_name_input_area   
    # the label for user_name  
    user_name = Label(Login, text = "ID",font=('Candara',18)).place(relx = 0.02, rely = 0.4,relwidth=0.2,relheight=0.08)   
    user_name_input_area = Entry(Login,textvariable = name_var, width = 30,font=('Bookman Old Style',18)).place(relx = 0.23,rely = 0.4,relwidth=0.5,relheight=0.08)
    
    # the label for user_password
    global user_password_entry_area
    user_password = Label(Login,text = "Password",font=('Candara',18)).place(relx = 0.02, rely = 0.6,relwidth=0.2,relheight=0.08)#add password rules   
    user_password_entry_area = Entry(Login, textvariable = passw_var,width = 30,show="*",font=('Bookman Old Style',18)).place(relx = 0.23, rely = 0.6,relwidth=0.5,relheight=0.08)

    #submit button
    if pers=="Admin":
        submit_button = Button(Login,text="Submit",bg='brown', fg='white',font=('Candara',18),command = submitadmin)
        
    else:
        submit_button = Button(Login,text="Submit",bg='brown', fg='white',font=('Candara',18),command = submitmem)
        
    submit_button.place(relx=0.27,rely=0.8, relwidth=0.45,relheight=0.1)
    
def submitadmin():
    Login.destroy()
    name=name_var.get()
    password=passw_var.get()

    cursor.execute('select * from librarian where ID = {}'.format(name))
    data = cursor.fetchone()
    count = cursor.rowcount
    print(data)
    print("Count: ",count)
    if count == -1:
        print("Admin does not exist")
        messagebox.showerror("Invalid","Invalid ID")
        name_var.set("")
        passw_var.set("")
        login("Admin")
        
    else:    
        global adminid
        adminid = name
    
        print("The name is : " + name)
        print("The password is : " + password)

        if data[2]==password:
            name_var.set("")
            passw_var.set("")
            adminpage()
        else:
            messagebox.showerror("Invalid","Incorrect password")
            #user_name_input_area.delete("1.0","end")
            
            passw_var.set("")
            login("Admin")
        
def submitmem():
    Login.destroy()
    name=name_var.get()
    password=passw_var.get()

    cursor.execute('select * from members where MemberID = {}'.format(name))
    data = cursor.fetchone()
    count = cursor.rowcount
    print("Count: ",count)
    if count == -1:
        print("Admin does not exist")
        messagebox.showerror("Invalid","Invalid ID")
        name_var.set("")
        passw_var.set("")
        login("Member")
        
    else:    
        global memid
        memid = name
        global memname
        memname=data[1]
        print("The name is : " + name)
        print("The password is : " + password)

        if data[2]==password:
            name_var.set("")
            passw_var.set("")
            memberpage()
        else:
            messagebox.showerror("Invalid","Incorrect password")
            
            passw_var.set("")
            login("Member")
        
def adminpage():
    global admin
    admin = Toplevel(root)
    admin.geometry("660x500")
    admin.title("Admin Page")
    
    #add background image
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(admin, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    
    headingFrame1 = Frame(admin,bg="yellow",bd=3)#for box
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)#rel enters value as a fraction of parent widget
    headingLabel = Label(headingFrame1, text="Welcome Admin", bg='black', fg='white', font=('Courier',22))#for text inside box
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(admin,text="Add Book",bg='black', fg='white',font =(13),command=addbooks)#redirect all buttons to respective pages
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(admin,text="Remove Book",bg='black', fg='white',font =(13),command=removebooks)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(admin,text="Add Member",bg='black', fg='white',font =(13),command=addmembers)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(admin,text="Remove Member",bg='black', fg='white',font =(13),command=removemembers)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(admin,text="View Available Books",bg='black', fg='white',font =(13),command=Viewb)
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn6 = Button(admin,text="View Borrowed Books",bg='black', fg='white',font =(13),command=Viewbb)
    btn6.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

    logout =Button(admin,text="Logout",bg='red', fg='white',font=('Segoe',13),command = admin.destroy)
    logout.place(relx=0.8,rely=0.8, relwidth=0.1,relheight=0.1)

def memberpage():
    global member
    member = Toplevel(root)
    member.geometry("660x500")
    member.title("Member Page")

    #background('member')
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(member, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    
    headingFrame1 = Frame(member,bg="orange",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    
    headingLabel = Label(headingFrame1, text="Welcome {}".format(memname), bg='brown', fg='white', font=('Courier',26))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(member,text="Return borrowed books",bg='black', fg='white',font=(13),command=returnbooks)#parse memid
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(member,text="Borrow book",bg='black', fg='white',font=(13),command = borrowbooks)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    logout =Button(member,text="Logout",bg='red', fg='white',font=('Rockwell',13),command = member.destroy)
    logout.place(relx=0.8,rely=0.8, relwidth=0.1,relheight=0.1)
    

#borrowing------------------------------------------------------------------------------------------------------------------------------------
def borrowbooks():
    global borrow

    borrow = Toplevel(member)
    borrow.geometry("600x400")
    borrow.title("Borrow Books Page")
    
    #background image
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf2.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(borrow, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    
    global data    
    cursor.execute("select * from books order by BookID")
    data = cursor.fetchall()
    sqlcon.commit()

    if data==[]:
        messagebox.showinfo("Library", "No books Available! Come Again Later")
        borrow.destroy()
        return
    
    for i in data:
        print(i)

    headingFrame1 = Frame(borrow,bg="yellow",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Borrow Books", bg='black', fg='white', font = ('Courier',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    

    # label 
    selection = Label(borrow, text = "Select the Book :",font = ("Times New Roman", 15))
    selection.place(relx=0.1,rely=0.4)  
    # Combobox creation 
    n = tk.StringVar()
    global bookchosen
    bookchosen = ttk.Combobox(borrow, width = 27, textvariable = n) 
  
    # Adding combobox drop down list
    temp=[]
    for i in data:
        temp.append(i[1])
    #print("Temporary list: ",temp)
    global val
    val=tuple(temp)
    bookchosen['values'] = val 
  
    bookchosen.place(relx=0.35,rely=0.41) 
    bookchosen.current()
    '''global xcount
    xcount=0'''
    CancelBtn = Button(borrow,text="Cancel",bg='brown', fg='black',font=('Candara',18),command=borrow.destroy)#, command=next module
    CancelBtn.place(relx=0.08,rely=0.85, relwidth=0.18,relheight=0.08)

    MoreBtn = Button(borrow,text="Borrow More Books",bg='brown', fg='black',font=('Candara',18),command=moreb)#, command=next module
    MoreBtn.place(relx=0.32,rely=0.85, relwidth=0.35,relheight=0.08)

    ContinueBtn = Button(borrow,text="Continue",bg='brown', fg='black',font=('Candara',18),command=confirmb)#, command=next module
    ContinueBtn.place(relx=0.75,rely=0.85, relwidth=0.18,relheight=0.08)

def confirmb():
    borrowing(1)
def moreb():
    borrowing(2)
    
def borrowing(n):
    '''xcount+=1
    if xcount==3:
        messagebox.showinfo("Library", "You have borrowed maximum amount of books allowed!")
        return'''
    value = bookchosen.get()
    messagebox.showinfo("Library", "You have borrowed " + value)
    print('value: ',value)
    cursor.execute("SELECT MemberName FROM members WHERE MemberID = {}".format(memid))
    student_name=cursor.fetchone()
    cursor.execute('SELECT * FROM books WHERE BookName = "{}"'.format(value))                  
    book=cursor.fetchone()
    print("Selected book: ",book)
    print("Borrower Details: ",book[0],book[1],memid,student_name[0])
    cursor.execute('INSERT INTO borrowedbooks VALUES({},"{}",{},"{}")'.format(book[0],book[1],memid,student_name[0]))
    cursor.execute("DELETE FROM books WHERE BookID={}".format(book[0]))
    sqlcon.commit()
    borrow.destroy()
    if n==2:
        borrowbooks()
    


#returning----------------------------------------------------------------------------------------------------------------------------------------------
def returnbooks():
    global ret
    ret = Toplevel(member)
    ret.geometry("600x400")
    ret.title("Return Books Page")
    
    #background image
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(ret, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    
    global data    
    cursor.execute("select * from borrowedbooks where MemberID = {} order by BookID".format(memid))
    data = cursor.fetchall()
    print(data)
    if data==[]:
        messagebox.showinfo("Library", "You have no books to return!")
        ret.destroy()
        return
    sqlcon.commit()

    headingFrame1 = Frame(ret,bg="yellow",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Return Books", bg='black', fg='white', font = ('Courier',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    for i in data:
        print(i)   

    # label 
    selection = Label(ret, text = "Select the Book :",font = ("Times New Roman", 15))
    selection.place(relx=0.1,rely=0.4)  
    # Combobox creation 
    n = tk.StringVar()
    global bookchosen
    bookchosen = ttk.Combobox(ret, width = 27, textvariable = n) 
  
    # Adding combobox drop down list
    temp=[]
    for i in data:
        temp.append(i[1])
    #print("Temporary list: ",temp)
    global val
    val=tuple(temp)
    bookchosen['values'] = val 
  
    bookchosen.place(relx=0.35,rely=0.41) 
    bookchosen.current()  

    CancelBtn = Button(ret,text="Cancel",bg='brown', fg='black',font=('Candara',18),command=ret.destroy)#, command=next module
    CancelBtn.place(relx=0.08,rely=0.85, relwidth=0.18,relheight=0.08)

    MoreBtn = Button(ret,text="Return More Books",bg='brown', fg='black',font=('Candara',18),command=moreret)#, command=next module
    MoreBtn.place(relx=0.32,rely=0.85, relwidth=0.35,relheight=0.08)

    ContinueBtn = Button(ret,text="Continue",bg='brown', fg='black',font=('Candara',18),command=confirmret)#, command=next module
    ContinueBtn.place(relx=0.75,rely=0.85, relwidth=0.18,relheight=0.08)

def confirmret():
    returning(1)
def moreret():
    returning(2)
    
def returning(n):
    value = bookchosen.get()
    messagebox.showinfo("Library", "You have returned " + value)
    print('value: ',value)
    
    cursor.execute('SELECT * FROM borrowedbooks WHERE BookName = "{}"'.format(value))                  
    book=cursor.fetchone()
    print("Borrower Details: ",book)
    cursor.execute('INSERT INTO books VALUES({},"{}")'.format(book[0],book[1]))
    cursor.execute("DELETE FROM borrowedbooks WHERE BookID={}".format(book[0]))
    sqlcon.commit()
    ret.destroy()
    if n==2:
        returnbooks()
    
    
#adding books---------------------------------------------------------------------------------------------------------------------------------------------
def addbooks():
    
    global addbk
    addbk = Toplevel(admin)
    addbk.title("Library")
    addbk.minsize(width=400,height=400)
    addbk.geometry("660x500")#height x width
    
    #background image
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(addbk, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    
    headingFrame1 = Frame(addbk,bg="orange",bd=3)#for box
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)#rel enters value as a fraction of parent widget
    headingLabel = Label(headingFrame1, text="ADD BOOKS", bg='brown', fg='white', font=('Courier',26))#for text inmemide box
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    global id_var
    id_var=tk.StringVar()
    global name_var
    name_var=tk.StringVar()
    
    # the label for user_name
    
    book_id = Label(addbk, text = "Book ID",font=('Candara',18)).place(relx = 0.02, rely = 0.4,relwidth=0.2,relheight=0.08)   
    book_id_input_area = Entry(addbk,textvariable=id_var, width = 30,font=('Bookman Old Style',18)).place(relx = 0.23,rely = 0.4,relwidth=0.5,relheight=0.08)
    #print(book_id_input_area.get())
    
    
    book_name = Label(addbk,text = "Book Name",font=('Candara',18)).place(relx = 0.02, rely = 0.6,relwidth=0.2,relheight=0.08)   
    book_name_entry_area = Entry(addbk,textvariable=name_var, width = 30,font=('Bookman Old Style',18)).place(relx = 0.23, rely = 0.6,relwidth=0.5,relheight=0.08)  
    #print(book_name_input_area.get())
    
    Cancel_button = Button(addbk,text="Cancel",bg='brown', fg='white',font=('Candara',18),command=addbk.destroy)#change destroy to link to next window
    Cancel_button.place(relx=0.02,rely=0.8, relwidth=0.25,relheight=0.1)

    Add_More_Books_button = Button(addbk,text="Add More Books",bg='brown', fg='white',font=('Candara',18),command=morebooks)#change destroy to link to next window
    Add_More_Books_button.place(relx=0.34,rely=0.8, relwidth=0.30,relheight=0.1)
    
    Confirm_button = Button(addbk,text="Confirm",bg='brown', fg='white',font=('Candara',18),command=confirmbooks)#change destroy to link to next window
    Confirm_button.place(relx=0.7,rely=0.8, relwidth=0.25,relheight=0.1)
def confirmbooks():
    addingbook(1)
def morebooks():
    addingbook(2)
    
def addingbook(n):
    print(id_var.get())
    print(name_var.get())
    bid=int(id_var.get())
    bname=name_var.get()
    
    cursor.execute("select * from books order by BookID")
    data = cursor.fetchall()
    for i in data:
        if i[0]==bid:
            messagebox.showinfo("Library", "Book ID already exists! Please try again")
            return
        elif i[1]==bname:       
            messagebox.showinfo("Library", "Book Name already exists! Please try again")
            return      

    cursor.execute('INSERT INTO books VALUES({},"{}")'.format(bid,bname))
    messagebox.showinfo("Library", "Book added successfully!")
    cursor.execute("select * from books order by BookID")
    data = cursor.fetchall()
    for i in data:
        print(i)
    sqlcon.commit()
    addbk.destroy()
    if n==2:
        addbooks()
    

    
#removing books---------------------------------------------------------------------------------------------------------------------------------------------
def removebooks():
    
    global rembook
    rembook = Toplevel(admin)
    rembook.geometry("600x400")
    rembook.title("Remove Books Page")

    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(rembook, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    
    global data    
    cursor.execute("select * from books order by BookID")
    data = cursor.fetchall()
    sqlcon.commit()

    if data==[]:
        messagebox.showinfo("Library", "No books Available! Come Again Later")
        rembook.destroy()
        return
    
    for i in data:
        print(i)

    headingFrame1 = Frame(rembook,bg="yellow",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Remove Books", bg='black', fg='white', font = ('Courier',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    # label 
    selection = Label(rembook, text = "Select the Book :",font = ("Times New Roman", 15))
    selection.place(relx=0.1,rely=0.4)  
    # Combobox creation 
    n = tk.StringVar()
    global bookchosen
    bookchosen = ttk.Combobox(rembook, width = 27, textvariable = n,font=("Times New Roman", 15)) 
  
    # Adding combobox drop down list
    temp=[]
    for i in data:
        temp.append(i[1])
    #print("Temporary list: ",temp)
    global val
    val=tuple(temp)
    bookchosen['values'] = val 
  
    bookchosen.place(relx=0.35,rely=0.4) 
    bookchosen.current()  

    CancelBtn = Button(rembook,text="Cancel",bg='brown', fg='black',font=('Candara',18),command=rembook.destroy)#, command=next module
    CancelBtn.place(relx=0.08,rely=0.85, relwidth=0.18,relheight=0.08)

    MoreBtn = Button(rembook,text="Remove More Books",bg='brown', fg='black',font=('Candara',18),command=moreremb)#, command=next module
    MoreBtn.place(relx=0.32,rely=0.85, relwidth=0.38,relheight=0.08)

    ContinueBtn = Button(rembook,text="Continue",bg='brown', fg='black',font=('Candara',18),command=confirmremb)#, command=next module
    ContinueBtn.place(relx=0.75,rely=0.85, relwidth=0.18,relheight=0.08)

def  confirmremb():
    removingbooks(1)
def moreremb():
    removingbooks(2)
    
def removingbooks(n):
    value = bookchosen.get()
    messagebox.showinfo("Library", "You have removed " + value)
    print('value: ',value)    
    cursor.execute('SELECT * FROM books WHERE BookName = "{}"'.format(value))                  
    book=cursor.fetchone()
    print("Selected book: ",book)    
    cursor.execute("DELETE FROM books WHERE BookID={}".format(book[0]))
    sqlcon.commit()
    rembook.destroy()
    if n==2:
        removebooks()
    

#adding members---------------------------------------------------------------------------------------------------------------------------------------------
def addmembers():
    
    global addmem
    addmem = Toplevel(admin)
    addmem.title("Library")
    addmem.minsize(width=400,height=400)
    addmem.geometry("660x500")#height x width

    # Adding a background image
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(addmem, image = img)
    panel.image = img
    panel.place(x=0,y=0)

    headingFrame1 = Frame(addmem,bg="orange",bd=3)#for box
    headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)#rel enters value as a fraction of parent widget
    headingLabel = Label(headingFrame1, text="ADD MEMBER", bg='brown', fg='white', font=('Courier',26))#for text inside box
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    global id_var
    id_var=tk.StringVar()
    global name_var
    name_var=tk.StringVar()
    global pass_var
    pass_var=tk.StringVar()
    # the label for member_id  
    member_id = Label(addmem, text = "Member ID",font=('Candara',18)).place(relx = 0.02, rely = 0.3,relwidth=0.25,relheight=0.08)   
    member_id_input_area = Entry(addmem, textvariable=id_var,width = 30,font=('Bookman Old Style',18)).place(relx = 0.32,rely = 0.3,relwidth=0.5,relheight=0.08)

    # the label for member_name   
    member_name = Label(addmem,text = "Member Name",font=('Candara',18)).place(relx = 0.02, rely = 0.5,relwidth=0.25,relheight=0.08)   
    member_name_entry_area = Entry(addmem, textvariable=name_var,width = 30,font=('Bookman Old Style',18)).place(relx = 0.32, rely = 0.5,relwidth=0.5,relheight=0.08)
    #print(member_name_entry_area)

    # the label for member_password   
    member_password = Label(addmem,text = "Member Password",font=('Candara',18)).place(relx = 0.02, rely = 0.7,relwidth=0.29,relheight=0.08)   
    member_password_entry_area = Entry(addmem, textvariable=pass_var,width = 30,show ="*",font=('Bookman Old Style',18)).place(relx = 0.32, rely = 0.7,relwidth=0.5,relheight=0.08)

    #confirming buttons
    cancel_button = Button(addmem,text="Cancel",bg='brown', fg='white',font=('Candara',18),command=addmem.destroy)#change destroy to link to next window
    cancel_button.place(relx=0.02,rely=0.85, relwidth=0.25,relheight=0.1)  
   
    add_button = Button(addmem,text="Add More Members",bg='brown', fg='white',font=('Candara',18),command=moremem)#change destroy to link to next window
    add_button.place(relx=0.34,rely=0.85, relwidth=0.32,relheight=0.1)

    confirm_button = Button(addmem,text="Confirm",bg='brown', fg='white',font=('Candara',18),command=confirmmem)#change destroy to link to next window
    confirm_button.place(relx=0.7,rely=0.85, relwidth=0.25,relheight=0.1)

def confirmmem():
    addingmembers(1)
def moremem():
    addingmembers(2)
    
def addingmembers(n):
    print(id_var.get())
    print(name_var.get())
    print(pass_var.get())
    sid=int(id_var.get())
    sname=name_var.get()
    spass=pass_var.get()
    
    cursor.execute("select * from members order by MemberID")
    data = cursor.fetchall()
    for i in data:
        if i[0]==sid:
            messagebox.showinfo("Library", "Member ID already exists! Please try again")
            return
        elif i[1]==sname:       
            messagebox.showinfo("Library", "Member Name already exists! Please try again")
            return      

    cursor.execute('INSERT INTO members VALUES({},"{}","{}")'.format(sid,sname,spass))
    messagebox.showinfo("Library", "Member added successfully!")
    sqlcon.commit()
    addmem.destroy()
    if n==2:
        addmembers()
    

#removing members---------------------------------------------------------------------------------------------------------------------------------------------
def removemembers():
    
    global remmember
    remmember = Toplevel(admin)
    remmember.geometry("600x400")
    remmember.title("Remove members Page")

    #background image
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(remmember, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    
    global data    
    cursor.execute("select * from members order by MemberID")
    data = cursor.fetchall()
    sqlcon.commit()

    if data==[]:
        messagebox.showinfo("Library", "No members ! Come Again Later")
        remmember.destroy()
        return
    
    for i in data:
        print(i)

    headingFrame1 = Frame(remmember,bg="yellow",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Remove members", bg='black', fg='white', font = ('Courier',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    # label 
    selection = Label(remmember, text = "Select the member :",font = ("Times New Roman", 15))
    selection.place(relx=0.07,rely=0.4)  
    # Combobox creation 
    n = tk.StringVar()
    global memberchosen
    memberchosen = ttk.Combobox(remmember, width = 27, textvariable = n,font = ("Times New Roman", 15)) 
  
    # Adding combobox drop down list
    temp=[]
    for i in data:
        temp.append(i[1])
    #print("Temporary list: ",temp)
    global val
    val=tuple(temp)
    memberchosen['values'] = val 
  
    memberchosen.place(relx=0.35,rely=0.4) 
    memberchosen.current()  

    CancelBtn = Button(remmember,text="Cancel",bg='brown', fg='black',font=('Candara',18),command=remmember.destroy)#, command=next module
    CancelBtn.place(relx=0.08,rely=0.85, relwidth=0.18,relheight=0.08)

    MoreBtn = Button(remmember,text="Remove More members",bg='brown', fg='black',font=('Candara',18),command=moreremmem)#, command=next module
    MoreBtn.place(relx=0.32,rely=0.85, relwidth=0.4,relheight=0.08)

    ContinueBtn = Button(remmember,text="Continue",bg='brown', fg='black',font=('Candara',18),command=confirmremmem)#, command=next module
    ContinueBtn.place(relx=0.75,rely=0.85, relwidth=0.18,relheight=0.08)

def confirmremmem():
    removingmembers(1)
def moreremmem():
    removingmembers(2)
    
def removingmembers(n):
    value = memberchosen.get()
    messagebox.showinfo("Library", "You have removed " + value)
    print('value: ',value)    
    cursor.execute("SELECT * FROM members WHERE memberName = '{}'".format(value))                  
    member=cursor.fetchone()
    print("Selected member: ",member)    
    cursor.execute("DELETE FROM members WHERE memberID={}".format(member[0]))
    sqlcon.commit()
    remmember.destroy()
    if n==2:
        removemembers()
    


#viewing books---------------------------------------------------------------------------------------------------------------------------------------------
def Viewb():
    
    global viewbooks
    viewbooks = Toplevel(admin)
    viewbooks.title("Library")
    viewbooks.minsize(width=400,height=400)
    viewbooks.geometry("660x500")
    
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(viewbooks, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    #================
    headingFrame1 = Frame(viewbooks,bg="yellow",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="View Available Books", bg='black', fg='white', font = ('Courier',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelHead = Frame(viewbooks,bg='black')
    labelHead.place(relx=0.1,rely=0.3,relwidth=0.5,relheight=0.07)
    

    labelFrame = Frame(viewbooks,bg='black')
    labelFrame.place(relx=0.1,rely=0.38,relwidth=0.58,relheight=0.5)
    y = 0.05
    
    scroll = Scrollbar(viewbooks)
    scroll.place(relx=0.7,rely=0.38,relheight=0.5)
    books=Text(labelFrame, yscrollcommand=scroll.set,bg='black',fg='white',font=('Candara',14))
    
    
    Label(labelHead, text=' BookID\t       Title',bg='black',fg='white',font=('Consolas',15)).place(relx=0,rely=0)
    Label(labelHead, text = "----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0,rely=0.75,relheight=0.2)
    
    try:
        cursor.execute("select * from books order by BookID")#put widget,but which?
        data = cursor.fetchall()
        sqlcon.commit()
        for i in data:
            print(i)
            books.insert(END,"     {}\t    {}\n".format(i[0],i[1]))
        books.place(relx=0,relwidth=1,relheight=1)
        scroll.config(command=books.yview)
    except:
        messagebox.showinfo("Failed to fetch files from database")

    
    quitBtn = Button(viewbooks,text="Quit",bg='brown', fg='black',font=('Candara',18), command=viewbooks.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
#viewing borrowed books---------------------------------------------------------------------------------------------------------------------------------------------
def Viewbb():
    
    global viewborrowedbooks
    viewborrowedbooks = Toplevel(admin)
    viewborrowedbooks.title("View Borrowed Books Page")
    viewborrowedbooks.minsize(width=400,height=400)
    viewborrowedbooks.geometry("700x500")
    
    img=Image.open("D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf1.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(viewborrowedbooks, image = img)
    panel.image = img
    panel.place(x=0,y=0)
    #================
    headingFrame1 = Frame(viewborrowedbooks,bg="yellow",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="View Borrowed Books", bg='black', fg='white', font = ('Courier',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelHead = Frame(viewborrowedbooks,bg='black')
    labelHead.place(relx=0.03,rely=0.3,relwidth=0.47,relheight=0.07)
    labelHead2 = Frame(viewborrowedbooks,bg='black')
    labelHead2.place(relx=0.5,rely=0.3,relwidth=0.47,relheight=0.07)

    labelFrame = Frame(viewborrowedbooks,bg='black')
    labelFrame.place(relx=0.03,rely=0.38,relwidth=0.47,relheight=0.5)
    y = 0.05
    labelFrame2 = Frame(viewborrowedbooks,bg='black')
    labelFrame2.place(relx=0.5,rely=0.38,relwidth=0.47,relheight=0.5)
    y = 0.05
    
    yscroll = Scrollbar(viewborrowedbooks)
    yscroll.place(relx=0.95,rely=0.38,relheight=0.5)
    books=Text(labelFrame, yscrollcommand=yscroll.set,bg='black',fg='white',font=('Candara',14))
    members=Text(labelFrame2, yscrollcommand=yscroll.set,bg='black',fg='white',font=('Candara',14))
    
    Label(labelHead, text=' Book ID\t Title',bg='black',fg='white',font=('Consolas',15)).place(relx=0,rely=0)
    Label(labelHead, text = "--------------------------------------------------------------------------",bg='black',fg='white').place(relx=0,rely=0.75,relheight=0.2)
    Label(labelHead2, text=' Student ID\tStudent Name',bg='black',fg='white',font=('Consolas',15)).place(relx=0,rely=0)
    Label(labelHead2, text = "-------------------------------------------------------------------------",bg='black',fg='white').place(relx=0,rely=0.75,relheight=0.2)
    try:
        cursor.execute("select * from borrowedbooks order by BookID")#put widget,but which?
        data = cursor.fetchall()
        if data==[]:
            messagebox.showinfo("Library","No borrowed Books!")
            viewborrowedbooks.destroy()
            return
        sqlcon.commit()
        for i in data:
            print(i)
            books.insert(END,"     {}\t             {}\n".format(i[0],i[1]))
            members.insert(END,"     {}\t\t    {}\n".format(i[2],i[3]))
        books.place(relx=0,relwidth=1,relheight=1)
        members.place(relx=0,relwidth=1,relheight=1)
        yscroll.config(command=books.yview)
        yscroll.config(command=members.yview)
        
    except:
        messagebox.showinfo("Failed to fetch files from database")

    
    quitBtn = Button(viewborrowedbooks,text="Quit",bg='brown', fg='black',font=('Candara',18), command=viewborrowedbooks.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    

#background
C = Canvas(root,bg='blue')
filename = PhotoImage(file = "D:\\Vidhyuth\\Python programs\\Comp Project\\Pictures for GUI\\Bookshelf2.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0)

headingFrameH = Frame(root,bg="yellow",bd=5)#for box
headingFrameH.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)#rel enters value as a fraction of parent widget
headingLabelH = Label(headingFrameH, text="Welcome to \n Hogwarts Library", bg='black', fg='white', font=('Courier',18))#for text inside box
headingLabelH.place(relx=0,rely=0, relwidth=1, relheight=1)

lib = Button(root,text="Librarian",bg='black', fg='white', font=('Segoe UI',15),command = lglib)#command = loginMember() inside btn1
lib.place(relx=0.02,rely=0.5, relwidth=0.45,relheight=0.1)

mem = Button(root,text="Member",bg='black', fg='white', font=('Segoe UI',15),command = lgmem)#change to login page
mem.place(relx=0.53,rely=0.5, relwidth=0.45,relheight=0.1)

xit = Button(root,text="Quit",bg='red', fg='white', font=('Segoe UI',15),command = root.destroy)#change to login page
xit.place(relx=0.8,rely=0.8, relwidth=0.1,relheight=0.1)
