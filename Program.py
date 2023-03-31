from tkinter import *

root = Tk()
root.title("my GUI")
root.geometry("450x350+600+500")

def showChoice():
    print(language1.get(),language2.get(),language3.get(),language4.get())
language1 = IntVar()
Checkbutton(text="Python",variable=language1).pack(anchor=W)
language2 = IntVar()
Checkbutton(text="Java",variable=language2).pack(anchor=W)
language3 = IntVar()
Checkbutton(text="PHP",variable=language3).pack(anchor=W)
language4 = IntVar()
Checkbutton(text="C#",variable=language4).pack(anchor=W)

Button(text="Show Option",command=showChoice).pack(anchor=W)
root.mainloop()