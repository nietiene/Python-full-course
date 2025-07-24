todo_list = []

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
        num = int(input("Enter task number"))        