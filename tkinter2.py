import tkinter as tk

root = tk.Tk()
root.title('my app')
root.geometry('400x300')

def on_click():
    label.config(text="Button clicked!")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

root.mainloop()