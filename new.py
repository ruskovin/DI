from tkinter import *

win = Tk()

txt = Label(win, text="Hello ! Welcome to the app!", fg='red')
txt.pack()

btn = Button(win, text='Quit!' , bg='black', fg='white',command=win.destroy, height='2',)
btn.pack(fill='x')
win.mainloop()