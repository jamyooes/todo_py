from tkinter import *
from tkinter import ttk

class Task_List():
    def __init__(self):
        self.stack = []

    def add_tasks(self, task):
        self.stack.push(task)
        # send ID back to task
    
    def length(self):
        # Gets the length of the list
        return len(self.stack)

    def delete_tasks(self):
        pass
    
    def update_tasks(self):
        pass

def erase_widgets(root):
    # Utility function to clearing out the screen
    for widget in root.winfo_children():
        widget.destroy()

# TO-DO maybe add some kind of db connection or local storage with csv
def task_list_screen(root):
    erase_widgets(root)
    
    # Maybe load a csv here
    
    # Instantiate an instance of Tasklist
    todo_list = Task_List()

    empty_label = Label(root, text = "")
    if todo_list.length() == 0:
        empty_label = Label(root, text = "To-Do List is empty")
        empty_label.pack()
    
    add_task_btn = ttk.Button(root, text = "Add Task", command=create_new_task_win(root, todo_list))
    add_task_btn.pack()

def create_new (root):
    pass
        
def create_new_task_win(root, todo_list):
    erase_widgets(root)
    task_list_btn = ttk.Button(root, text = "Task List", command=lambda: task_list_screen(root))
    task_list_btn.pack()
    user_input = Entry(root, width= 40)
    user_input.focus_set()
    user_input.pack()
    
        


# Creating TK Class
root = Tk()
root.geometry("800x500")

# Creates a fgrame widget
frm = ttk.Frame(root, padding=10)

# Grid is to specify layout
frm.grid()

# Home screen - current option is clicking on the task list
ttk.Button(frm, text = "Task List", command=lambda: task_list_screen(root)).grid(column=0, row=0)

# Button Widget to the right of label (col, row)
ttk.Button(frm, text="Close App", command=root.destroy).grid(column=0, row=1)

# Method to put everything on display and responds to user input
root.mainloop()


