import tkinter
import tkinter.messagebox
window= tkinter.Tk()
window.geometry("200x150")
def show_msg():
#I would prefer to not post my address, but the program should work
   tkinter.messagebox.showinfo("Info", "My name is Tristan Blair,\n I live at [Address]")
def quit():
   window.destroy()

tkinter.Button(window, text= "Show Info", command=show_msg).pack()
tkinter.Button(window, text= "Quit", command=quit).pack()

window.mainloop()
