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
        
def create_new_task_win(root, todo_list):
    task_list_btn = ttk.Button(root, text = "Task List", command=lambda: task_list_screen(root))
    task_list_btn.pack()
    user_input = Entry(root, width= 40)
    user_input.focus_set()
    user_input.pack()

class App(Tk):
    def __init__(self, parent):
        # Set parent as the root
        self.parent = parent
        # Set the size of the window
        self.parent.geometry("800x500")

        # The name container for all the frames
        container = Frame(self.parent)
        container.pack()

        # Stores the frames
        self.frames = {}
        # Loop through all the potential pages and save them into the frames
        for F in (StartPage, PageOne, PageTwo, TaskList):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        task_list_nav = Button(self, text="Go to Task List",
                            command=lambda: controller.show_frame("TaskList"))
        button1.pack()
        button2.pack()
        task_list_nav.pack()


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 2")
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class TaskList(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.controller = controller
        
        # Title of the page
        label = Label(self, text = "Task list")
        label.pack (side="top", fill = "x", pady = 10)
        
        # Store the tasks
        self.tasks = []
        text_name = ""
        text_description = ""
        def display_text():
            text_name = task_name.get()
            text_description = task_description.get()
            if text_name != "" and text_description != "":
                empty_warning.config(text="")
                self.add_tasks(text_name, text_description, len(self.tasks) + 1)
                self.display_tasks()
                text_name = ""
                text_description = ""
            else:
                empty_warning.config(text="Enter an actual task")
            
        def delete_text_tasks():
            delete_id = delete_text.get()
            try:
                for pos in range(len(self.tasks)):
                    # print(pos)
                    if self.tasks[pos].get_id() == int(delete_id):
                        # print(self.tasks[pos].get_id())
                        self.delete_tasks(pos)
            except:
                pass
            
        # Textbox for user to enter the name and description for their task
        task_name = Entry(self)
        task_name.pack()
        task_description = Entry(self)
        task_description.pack()

        submit_name_btn = Button(self, text="Display", command=display_text)
        submit_name_btn.pack()
        
        delete_text = Entry(self)
        delete_text.pack()
        
        delete_label = Label(self, text="Enter Task number above to delete")
        delete_label.pack()
        
        delete_text_button = Button(self, text="Delete", command=delete_text_tasks)
        delete_text_button.pack()

        empty_warning = Label(self, text="")
        empty_warning.pack()
        
        self.task_label = Label(self, text ="")
        self.task_label.pack()
        
    def add_tasks(self, task_name, description, id):
        self.tasks.append(Tasks(task_name, description, id))
    
    def delete_tasks(self, loc):
        self.tasks.pop(loc)
        # print(loc)
        self.display_tasks()
    
    def display_tasks(self):
        text = ""
        for i in self.tasks:
            text += f"Task Number {i.get_id()} - {i.get_task_name()} : {i.get_description()}\n"
        self.task_label.config(text=text)


class Tasks():
    def __init__(self, task_name, description, id):
        self.task_name = task_name
        self.description = description
        self.id = id
    def get_task_name(self):
        return self.task_name
    def get_description(self):
        return self.description
    def get_id(self):
        return self.id

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()

# class Task_List(Frame):
#     def __init__(self, frame):
#         self.frame = ttk.Frame(master = frame)
#         self.frame.grid(column= 0, row= 0, sticky="nsew")
#         ttk.Button(text="Raise", command=self.frame.tkraise).pack()
#     def return_frame(self):
#         pass

# App()

"""
# Creates a fgrame widget
frm = ttk.Frame(self.root, padding=10)
frm.pack()

# Grid is to specify layout

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
self.root.mainloop()
"""