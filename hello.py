import tkinter as tk

root = tk.Tk()
root.title('Hello')
root.geometry("300x300")
root.config(bg="grey")

label1 = tk.Label(root, text='Hello tkinter', bg="black", fg="blue")
label1.pack(ipadx=70, ipady=100, expand=True)
label1.config(font=200)

root.mainloop()