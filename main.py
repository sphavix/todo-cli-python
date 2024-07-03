def add_task(tasks, title, description=""):
    tasks.append({"title": title, "description": description, "completed": False})

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task index")

def update_task(tasks, index, title, description):
    if 0 <= index < len(tasks):
        tasks[index]["title"] = title
        tasks[index]["description"] = description
    else:
        print("Invalid task index")

def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    else:
        print("Invalid task index")

def print_tasks(tasks):
    result = []
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            result.append(f"{i+1}. [{status}] {task['title']} '\n' {task['description']}")
            return result

def main():
    tasks = []
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Print Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(tasks, title, description)
        elif choice == "2":
            index = int(input("Enter task index to remove: ")) - 1
            remove_task(tasks, index)
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: ")) - 1
            mark_task_completed(tasks, index)
        elif choice == "4":
            result = print_tasks(tasks)
            if result:
                print("\n".join(result))
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()