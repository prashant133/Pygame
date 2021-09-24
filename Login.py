
from tkinter import *
from PIL import ImageTk ,Image
import sqlite3
from tkinter import messagebox
from create_an_account import reg
from bird import play
import os.path


def login ():
    if user.get() == "" and password.get() == "":
        messagebox.showinfo("INVALID DETAILS", "Invalid username or password")
    elif user.get() == "" :
        messagebox.showinfo("INVALID DETAILS", "Invalid username or password")
    elif password.get()== "":
        messagebox.showinfo("INVALID DETAILS","Invalid username or password")
    else :
        connector = sqlite3.connect("registration.db")
        cur = connector.cursor()
        query = "SELECT * FROM Information WHERE username=?and password=?"
        user_name = user.get()
        password_name = password.get()
        cur.execute(query,(user_name,password_name))
        rows = cur.fetchall()
        print(rows)
        #checking wheter it is empyt or not <if empty show error message , if not login
        if len(rows)> 0:
            #messagebox.showinfo(":Account created" ,login has been sudcess')
            play()
        else :
            messagebox.showerror("Error","invalid username and password ")
#creating the window
root = Tk()

#giving the title for the project
root.title("Loginpage")

#set the geometry for the root window
root.geometry('350x320')

#adding the background
bg = ImageTk.PhotoImage(Image.open("Image/bgg.jpg"))


#create a label
my_label = Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

#add something to the top of our image
my_text = Label(root,text="Login",font=("helvetica",15),bg='#ffb347')
my_text.pack(pady=20)


# create a frame
my_frame = Frame(root,bg='#b9f1f0')
my_frame.pack()

#creating label
user_name = Label(my_frame,text='UserName',bg="#ffb347",bd=2)
user_name.grid(row=0,column=0)
password = Label(my_frame,text='Password',bg='#ffb347',bd=4)
password.grid(row =2 , column =0)

#creating textbox
user = Entry(my_frame,width=30,bg='#fafcfb',borderwidth=5, font=" aerial 10 bold")
user.grid(row=0,column = 2 ,padx=10,pady=10)
password = Entry(my_frame,width=30,bg="#fafcfb",bd=4,borderwidth=5, font=" aerial 10 bold",show="*")
password.grid(row=2 ,column=2,padx=10,pady=10)


 #creting button to open an account
create_button = Button(my_frame,text="create an account",bg='#ffb347',borderwidth = 5,command=reg)
create_button.grid(row=3,column=2)
#creating sumbit button
submit_button = Button(my_frame,text="login",bd=6,bg="#ffb347",command = login)
submit_button.grid(row=5 ,column = 2,pady=10 )




root.mainloop()
