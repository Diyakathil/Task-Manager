import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Entry box
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add Task Button
        add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
        add_button.pack()

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Buttons below list
        del_button = tk.Button(root, text="Delete Task", width=20, command=self.delete_task)
        del_button.pack()

        done_button = tk.Button(root, text="Mark as Done", width=20, command=self.mark_done)
        done_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected.")

    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index] = self.tasks[index] + " ✅"
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()



def __init__(self, root):
    self.root = root
    self.root.title("To-Do List App")

    self.tasks = []

    #GUI SETUP
    self.load_tasks()
    
    self.task_entry = tk.Entry(root, width=40)
    self.task_entry.pack(pady=10)

    add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
    add_button.pack()

    self.task_listbox = tk.Listbox(root, width=50, height=10)
    self.task_listbox.pack(pady=10)

    del_button = tk.Button(root, text="Delete Task", width=20, command=self.delete_task)
    del_button.pack()

    done_button = tk.Button(root, text="Mark as Done", width=20, command=self.mark_done)
    done_button.pack()

    # Add Save button
    save_button = tk.Button(root, text="Save Tasks", width=20, command=self.save_tasks)
    save_button.pack(pady=(5, 0))

    # Load saved tasks
    self.load_tasks()

def save_tasks(self):
    with open("tasks.txt", "w") as file:
        for task in self.tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks(self):
    try:
        with open("tasks.txt", "r") as file:
            self.tasks = [line.strip() for line in file.readlines()]
            self.update_listbox()
    except FileNotFoundError:
        self.tasks = []
