from tkinter import *
from PIL import ImageTk ,Image
import sqlite3
#creating the window
root = Tk()

#giving the title for the project
root.title("Loginpage")

#set the geometry for the root window
root.geometry('279x180')

#adding the background
bg = ImageTk.PhotoImage(Image.open("background.jpg"))


#DATABASES
#create a databases or connect to one
conn = sqlite3.connect('Login_book.db')

#create cursor
c = conn.cursor()
'''
#create Table
c.execute("""CREATE TABLE Login(
    user text,
    password text
)""")
'''
#create submit button for databases
def submit():
    #create a databases or connect to one
    conn = sqlite3.connect('Login_book.db')

    #create cursor
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO Login VALUES (:user,:password)",{
        'user':user.get(),
        'password':password.get()
    })

    #commit change
    conn.commit()

    #close connection
    conn.close()

    #clear the text boxes
    user.delete(0,END)
    password.delete(0,END)

#create a label
my_label = Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

#add something to the top of our image
my_text = Label(root,text="welcome",font=("helvetica",15) ,fg ="#235f73",bg='#58d3ff')
my_text.pack(pady=20)

# create a frame
my_frame = Frame(root)
my_frame.pack()

#creating label
user_name = Label(my_frame,text='UserName',bg="#9ce0f6")
user_name.grid(row=0,column=0)
password = Label(my_frame,text='Password',bg='#368872')
password.grid(row =1 , column =0)

#creating textbox
user = Entry(my_frame,width=30,bg='#9ce0f6')
user.grid(row=0,column = 2 )
password = Entry(my_frame,width=30,bg="#368872")
password.grid(row=1 ,column=2)

#creating the button for submit
submit_btn = Button(my_frame,text='Submit',bg='#486577',command=submit)
submit_btn.grid(row=2,column = 2, columnspan=2)

#commit change
conn.commit()

#close connection
conn.close()



root.mainloop()