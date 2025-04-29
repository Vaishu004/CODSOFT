import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("TaskStreak")
root.geometry("800x400")
root.configure(bg="#f9f9f9")

# List to store task variables
task_vars = []

def add_task():
    task = task_entry.get()
    if task.strip() != "":
        task_entry.delete(0, tk.END)
        
        var = tk.BooleanVar()
        cb = tk.Checkbutton(task_list_frame, text=task, variable=var, font=("Arial", 12), bg="#f9f9f9", anchor="w")
        cb.pack(fill='x', pady=2, padx=10, anchor='w')
        task_vars.append((task, var))
        
        messagebox.showinfo("Task Added", f"Task '{task}' added!")
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

#delete tasks
def delete_task() :
    for widget in task_list_frame.winfo_children() :
        widget.destroy()
    task_vars.clear()
    messagebox.showinfo("Delete Task", "All tasks Deleted")

# Title
title = tk.Label(root, text="Enter Tasks", font=("Helvetica", 18, "bold"), bg="#f9f9f9")
title.pack(pady=10)

# Input field and Add Task button
input_frame = tk.Frame(root, bg="#f9f9f9")
task_entry = tk.Entry(input_frame, width=80, font=("Arial", 12))
task_entry.pack(side=tk.LEFT, padx=10)
add_button = tk.Button(input_frame, text="Add Task", command=add_task, bg="#007bff", fg="white")
add_button.pack(side=tk.LEFT)
input_frame.pack(pady=10)

# Frame to show tasks with checkboxes
task_list_frame = tk.Frame(root, bg="#f9f9f9")
task_list_frame.pack(fill='both', expand=True, pady=10)

delete_btn = tk.Button(root, text="Delete Tasks", command=delete_task, bg="red", fg="white")
delete_btn.pack(pady=5)

root.mainloop()
