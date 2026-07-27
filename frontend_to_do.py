import tkinter as tk

window = tk.Tk()
window.title("To-Do List")
window.geometry("400x500")

# Title
title = tk.Label(window, text="My To-Do List", font=("Arial", 18))
title.pack(pady=10)

# Text box
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Listbox
listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)

tasks = []

def add_task():
    task = entry.get()

    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
def delete_task():
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
# Buttons

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    command=add_task
)
add_button.pack(side="left", padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    command=delete_task
)
delete_button.pack(side="left", padx=5)

window.mainloop()
