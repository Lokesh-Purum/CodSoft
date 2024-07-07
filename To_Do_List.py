import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.root.geometry("500x400")
        self.root.configure(bg="#e1f5fe")

        # Create the frames
        self.frame = tk.Frame(root, bg="#e1f5fe")
        self.frame.pack(pady=10)

        # Listbox to display tasks
        self.listbox = tk.Listbox(
            self.frame, width=50, height=10, bd=0, font=("Helvetica", 12),
            bg="#ffffff", fg="#000000", selectbackground="#f0e68c", selectforeground="#000000"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Entry box for adding tasks
        self.task_entry = tk.Entry(
            root, font=("Helvetica", 12), width=42, bd=2, bg="#ffffff", fg="#000000"
        )
        self.task_entry.pack(pady=10)

        # Buttons for adding, completing, updating, and deleting tasks
        button_frame = tk.Frame(root, bg="#e1f5fe")
        button_frame.pack(pady=10)

        self.add_task_btn = tk.Button(
            button_frame, text="Add Task", font=("Helvetica", 12), command=self.add_task,
            bg="#4caf50", fg="#ffffff", padx=10, pady=5
        )
        self.add_task_btn.grid(row=0, column=0, padx=5)

        self.complete_task_btn = tk.Button(
            button_frame, text="Complete Task", font=("Helvetica", 12), command=self.complete_task,
            bg="#2196f3", fg="#ffffff", padx=10, pady=5
        )
        self.complete_task_btn.grid(row=0, column=1, padx=5)

        self.update_task_btn = tk.Button(
            button_frame, text="Update Task", font=("Helvetica", 12), command=self.update_task,
            bg="#ffc107", fg="#ffffff", padx=10, pady=5
        )
        self.update_task_btn.grid(row=0, column=2, padx=5)

        self.delete_task_btn = tk.Button(
            button_frame, text="Delete Task", font=("Helvetica", 12), command=self.delete_task,
            bg="#f44336", fg="#ffffff", padx=10, pady=5
        )
        self.delete_task_btn.grid(row=0, column=3, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def complete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task = self.listbox.get(selected_task_index)
            self.listbox.delete(selected_task_index)
            self.listbox.insert(tk.END, task + " (Completed)")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to complete.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task = self.listbox.get(selected_task_index)
            updated_task = simpledialog.askstring("Update Task", "Edit task:", initialvalue=task)
            if updated_task:
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, updated_task)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
