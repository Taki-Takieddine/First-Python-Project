from tkinter import *
import os

def register_user():
    username_info = username.get()
    password_info = password.get()
    with open(username_info + ".txt","w") as fic:
     fic.write(username_info+"\n")
     fic.write(password_info)

    username_Entry.delete(0, END)
    password_Entry.delete(0, END)

    Label(screen1, text = "").pack()
    Label(screen1, text ="REGISTRATION SUCCESS", fg = "green").pack()


def register():
 global screen1
 screen1 = Toplevel(screen)
 screen1.title("Register")
 screen1.geometry("300x250")
 global username
 global password
 global username_Entry
 global password_Entry

 username = StringVar()
 password = StringVar()

 Label(screen1, text = "please enter details belows").pack()
 Label(screen1, text = "").pack()
 Label(screen1, text = "Username").pack()
 username_Entry = Entry(screen1, textvariable = username)
 username_Entry.pack()
 Label(screen1, text = "").pack()
 Label(screen1, text = "Password").pack()
 password_Entry = Entry(screen1, textvariable = password, show = "*")
 password_Entry.pack()
 Label(screen1, text="").pack()
 Button(screen1, text = "Register", width = "20", height = "1", command = register_user).pack()

def login_virify():
    username1 = username_virify.get()
    password1 = password_virify.get()
    username_Entry1.delete(0, END)
    password_Entry1.delete(0, END)

    list = os.listdir()

    username1 = username1+".txt"
    if username1 in list:
      with open(username1,"r") as fic:
          virify = fic.read().splitlines()
          if password1 in virify:
              Label(screen2, text="LOGIN SUCCESSFUL", fg = "green").pack()
          else:
            Label(screen2, text="Password error", fg = "red").pack()
    else:
        Label(screen2, text="user not found", fg="red").pack()







def login():
 global screen2
 screen2 = Toplevel(screen)
 screen2.title("Login")
 screen2.geometry("300x250")

 global username_virify
 global password_virify
 global username_Entry1
 global password_Entry1


 username_virify = StringVar()
 password_virify = StringVar()

 Label(screen2, text = "please enter details below to Login").pack()
 Label(screen2, text = "").pack()
 Label(screen2, text="Username").pack()
 username_Entry1 = Entry(screen2, textvariable=username_virify)
 username_Entry1.pack()
 Label(screen2, text="").pack()
 Label(screen2, text="Password").pack()
 password_Entry1 = Entry(screen2, textvariable=password_virify, show = "*")
 password_Entry1.pack()
 Label(screen2, text="").pack()
 Button(screen2, text="Login", width="20", height="1", command = login_virify).pack()





#Fuction main screen
def main_screen():
    global screen
    screen = Tk()
    screen.title("Register and Login")
    Label(text = "Welcome...!", bg = "gray", height = "2", width = "30", font = ("Arial black", 15)).pack()
    Label(text = "").pack()
    Label(text="").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    screen.geometry("300x250")
    screen.mainloop()
#main program
main_screen()