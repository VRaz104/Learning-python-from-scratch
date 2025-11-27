#Simple to do list!
import os
FILENAME = "tasks.txt"
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")
def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            if not tasks:
                print("No tasks yet.")
            else:
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")
        elif choice == "2":
            task = input("Enter the task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")
                num = input("Enter task number to remove: ")
                idx = int(num) - 1
                if 0 <= idx < len(tasks):
                     removed = tasks.pop(idx)
                     save_tasks(tasks)
                     print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option (1-4).")
main()
                
