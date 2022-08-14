import webbrowser
from tkinter import *

root = Tk( )

root.title("Abrir browser")
root.geometry("300x200")

def google():
    webbrowser.open('www.google.com')


Button(root, text='Abrir o google', command=google).pack(pady=20)

root.mainloop()
