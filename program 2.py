import tkinter
import tkinter.messagebox
win= tkinter.Tk()
win.geometry("200x150")
def show_msg():
#I would prefer to not post my adress in plaintext, but the program should work
   tkinter.messagebox.showinfo("Info", "My name is Tristan Blair,\n I live at [Address]")
tkinter.Button(win, text= "Show Info", command=show_msg).pack()
win.mainloop()
