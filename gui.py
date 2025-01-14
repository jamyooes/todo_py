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

# TO-DO maybe add some kind of db connection or local storage with csv
def task_list_screen(root): 
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
frm.pack()

# Grid is to specify layout

### TODO: Move everything to a class

# Home screen - current option is clicking on the task list
task_list_frame  = ttk.Frame(master=frm)
task_list_frame.grid(column= 0, row= 0)
# ttk.Button(frm, text = "Task List", command=lambda: task_list_screen(root)).grid(column=0, row=0)

# Button Widget to the right of label (col, row)
quit_frame = ttk.Frame(master=frm)
quit_frame.grid(column=0, row=0)
# ttk.Button(frm, text="Close App", command=root.destroy).grid(column=0, row=1)

# task_list

# Remove Later
ttk.Label(master=task_list_frame,
         text='Conj').grid()
ttk.Label(master=quit_frame,
         text='Trans').grid()

# Remove Later POC for changing frames
ttk.Button(text="Raise Conjugator", command=task_list_frame.tkraise).pack()
ttk.Button(text="Raise Translator", command=quit_frame.tkraise).pack()
task_list_frame.tkraise()
# Keep
# ttk.Button(text="Task List", command=).pack()

# Method to put everything on display and responds to user input
root.mainloop()


