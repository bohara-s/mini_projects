task = []

def show_menu():
    print("this is a todo app")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def add_task():
    task_name = input("enter the task name : ")
    task.append(task_name)
    print(f"task's added successfully : {task_name}")
def view_tasks():
    if not task :
        print("No tasks available.")
    else:
        print("/n---your Task---")
        for index, task_name in enumerate(task, start = 1):
            print(f"{index}.{task_name}")

def mark_task_done():
    view_tasks()
    if not task :
        print("no task avaliable")
        return
    try:
        task_num = int (input("enter the task number to make it done :"))
        if task_num < 1 or task_num> len(task ):
            task[task_num - 1]["done"]= True
            print(f"task {task_num} marked as done")
        else:
            print("invilad task number ")

    except ValueError:
        print("invalid input. please enter a number")


def delete_task():
    view_tasks()
    if not task :
        print("no task avaliable")
        return
    try:
        task_num = int (input("enter the task number to delete :"))
        if 1 <= task_num <=len(task):
            deleted_task = task.pop(task_num - 1)
            print(f"task {deleted_task} deleted successfully")
        else:
            print("invalid task number")
    except ValueError:
        print("invalid input. please enter a number")


while True :
        show_menu()
        choice = input("enter your choice (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":     
            delete_task()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


    