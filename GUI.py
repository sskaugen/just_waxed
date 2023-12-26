import tkinter as tk
#imported tkinter
window = tk.Tk()

window.geometry("500x500") #changes the dimensions of the window
window.title("TEST") #title for the window

label = tk.Label(window, text="TEST", background="black", foreground="white")
label.pack()

textbox = tk.Text(window, height=5)
textbox.pack()

button = tk.Button(window, text="TEST", width=25, height=5, bg="black", fg="white")
button.pack(padx=10, pady=10)



window.mainloop()
#calls constructor