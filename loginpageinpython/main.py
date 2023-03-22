from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()
    if username == 'admin' and password == '1':
        # print('Assalamalaikum')
        screen = Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Assalamalaikum', bg='#fff', font=(
            'calibri(Body)', 50, 'bold')).pack(expand=True)
        
        screen.mainloop()
    elif username != 'admin' and password != '1':
        messagebox.showerror('Invalid', 'Invalid username and password')
    elif password != '1':
        messagebox.showerror('Invalid', 'Invalid password')
    elif username != 'admin':
        messagebox.showerror('Invalid', 'Invalid username')
    else:
        messagebox.showerror('Invalid', 'Invalid data')


# get the absolute path to the image file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'login.png')

try:
    # try to load the image file
    img = PhotoImage(file=filename)
    label = Label(root, image=img, bg='white')
    label.place(x=50, y=50)

    frame = Frame(root, width=350, height=350, bg='white')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign in', fg='#57a1f8',
                    bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0,
                 bg='white', font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if code == '':
            code.insert(0, 'Password')
    code = Entry(frame, width=25, fg='black', border=0,
                 bg='white', font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    Button(frame, width=39, pady=7, text='Sign in',
           bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
    label = Label(frame, text="Don't have an account?", fg='black',
                  bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=75, y=270)

    sign_up = Button(frame, width=6, text='Sign up', border=0,
                     bg='white', cursor='hand2', fg='#57a1f8')
    sign_up.place(x=215, y=270)

except Exception as e:
    # display an error message if the image file cannot be loaded
    messagebox.showerror("Error", "Failed to load image file: {}".format(e))

root.mainloop()
