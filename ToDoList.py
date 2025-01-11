import tkinter as tk
from tkinter import messagebox

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")

# Create a frame for the input
frame = tk.Frame(root)
frame.pack(pady=10)

# Entry widget for new tasks
entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT)

# Button to add tasks
add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Button to remove tasks
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=10)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Load existing tasks
tasks = load_tasks()
update_task_list()

# Start the GUI event loop
root.mainloop()