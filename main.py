# Development done here, will move code into their own modules once features are completed

class Task_List():
    def __init__(self):
        # Temporary Data structure
        self.stack = []

    def add_tasks(self, task):
        self.stack.push(task)
        # send ID back to task
    
    def delete_tasks(self):
        pass
    
    def update_tasks(self):
        pass
    
class Task():
    def __init__(self, name, category, description, due_date):
        self.name = name
        self.category = category
        self.description = description
        self.due_date = due_date
    
    def update_name(self, new_name):
        # Update the name of the task
        self.name = new_name
    
    def remove_name(self):
        self.name = f"Untitled {self.task_num}"
    
    def remove_description(self):
        self.description = ""
    
    def update_description(self):
        # connect it to GUI button
        pass
    
    def description(self):
        pass
    
    def task_num(self):
        pass
    
    def set_category(self):
        pass
    
    def remove_category(self):
        pass

    def update_category(self):
        pass
    
    def set_date(self):
        pass

task = Task("Programming", "Code", "Coding", "today")
task.update_name()