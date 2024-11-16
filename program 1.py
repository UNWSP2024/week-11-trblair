import tkinter
window=tkinter.Tk()
# add widgets here
lbl=tkinter.Label(window, text="Life isnt about waiting for storms to pass, it's about learning how to dance in the rain ", font=("Helvetica", 16))
lbl.pack()

window.title('My GUI')
window.geometry("1000x200+10+20")
window.mainloop()
