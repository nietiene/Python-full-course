todo_list = [] # creates an empty list this will hold all user's task

def show_menu():
    print("\n To-Do menu") # adds new line before the menu
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter taks:")
    todo_list.append({"task": task, "done": False}) # stores a text user entered
    print("ask Added")   

def view_tasks():
    if not todo_list: # if todo_list is empty
        print("Not taks yet.")    
        return # ends the function early
    print("\nYour task") # if there are 

    # for loop that goed throught each item in the todo_list
    # we use enumeate to det both index and item itself 
    for idx, item in enumerate(todo_list, start=1):
        status = "✔" if item["done"] else "✖"
        print(f"{idx}. [{status}] {item['task']}")


def mark_done(): # define function used to mark task as completed
    view_tasks() # call view_tasks function to show all tasks with their status so user can choose which one to mark as done
    if not todo_list:
        return
    try:
        num = int(input("Enter task number to marks as done"))
        
        # if here the entered number greater than one and less than number of list we have
        # len() checks the total number 
        if 1 >= num <= len(todo_list):
            # num-1 here because python starts from index 0 so it take the value user type and convert it into corrected value
            todo_list[num-1]["done"] = True   
            print("Task marked as done")
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter a valid number")  

def delete_task():
    view_tasks()
    if not todo_list:
        return
    try:
        num = int(input("Enter task number to delete:"))
        
        if 1 >= num <= len(todo_list): 
            removed = todo_list.pop(num - 1)
            print(f"removed task: {removed['task']}")
        else:
            print("Invalid number.")   
    except ValueError:
       print("please enter a valid number")  

while True:
    show_menu()
    choice = input("Choose an option(1-5):")   

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()    
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":   
        print("Good bye")
        break
    else:
        print("invalid choice. please try again.")

