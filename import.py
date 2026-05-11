import tkinter as tk 
ventana= tk.Tk()
ventana.title("prueba tkinter")
ventana.geometry("300x200")

label = tk.Label(ventana,
text="Tkinter funciona!")
label.pack()
ventana.mainloop()