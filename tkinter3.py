import tkinter as tk

root = tk.Tk()
root.title('my app')
root.geometry('400x300')

# Entry widgets
e1 = tk.Entry(root)
e2 = tk.Entry(root)

# Labels and placement
tk.Label(root, text="name").grid(row=0)
tk.Label(root, text="age").grid(row=1)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Action to run when Submit is pressed
def submit():
    name = e1.get()
    age = e2.get()
    print(f"Name: {name}, Age: {age}")
    result_label.config(text=f"Saved: {name}, {age}")

# Submit button and result label
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Keep the window running
root.mainloop()