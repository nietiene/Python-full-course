todo_list = [] # creates an empty list named

def show_menu():
    print("\n To-Do menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter taks:")
    todo_list.append({"task": task, "done": False})
    print("✅ Task Added")   

def view_tasks():
    if not todo_list:
        print("📭 Not taks yet.")    
        return
    print("\n📝 Your task") 
    for idx, item in enumerate(todo_list, start=1):
        status = "✔️" if item["done"] else "❌"
        print(f"{idx}. [{status}] {item['task']}")


def mark_done():
    view_tasks()
    if not todo_list:
        return
    try:
        num = int(input("Enter task number to marks as doen"))
        
        if 1 <= num <= len(todo_list):
            todo_list[num-1]["done"] = True   
            print("✅ Task marked as done")
        else:
            print("❌ Invalid number")
    except ValueError:
        print("❌ Please enter a valid number")  

def delete_task():
    view_tasks()
    if not todo_list:
        return
    try:
        num = int(input("Enter task number to delete:"))
        if 1 <= num <= len(todo_list): 
            removed = todo_list.pop(num - 1)
            print(f"🗑️ removed task: {removed['task']}")
        else:
            print("❌ Invalid number.")   
    except ValueError:
       print("❌ please enter a valid number")  

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
        print("❌ invalid choice. please try again.")

