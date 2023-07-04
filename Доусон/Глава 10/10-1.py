
from tkinter import *

root = Tk()
root.title('Это я, метка')
root.geometry('200x50')
app = Frame(root)
app.grid()
lbl = Label(app, text = 'Вот она я !!!')
lbl.grid()

root.mainloop()