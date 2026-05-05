import json
import os
import sys
import time

FILE_NAME = "tasks.json"

# ---------------------------
# COLOR HELPERS (ANSI)
# ---------------------------
class Color:
    RESET  = "\033[0m"
    GREEN  = "\033[92m"
    RED    = "\033[91m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    BOLD   = "\033[1m"

# ---------------------------
# SPECIAL EFFECTS
# ---------------------------
def beep():
    print("\a", end="")

def typewrite(text, delay=0.04):
    """Prints text one character at a time for a subtle typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def saving_animation():
    """Briefly shows a saving indicator."""
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.15)
    print()

# ---------------------------
# LOAD / SAVE TASKS
# ---------------------------
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    sys.stdout.write(f"{Color.YELLOW}Saving{Color.RESET}")
    saving_animation()
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# ---------------------------
# CORE FUNCTIONS
# ---------------------------
def show_tasks(tasks):
    print(f"\n{Color.CYAN}{Color.BOLD}YOUR TASKS:{Color.RESET}")
    if not tasks:
        print(f"{Color.YELLOW}No tasks yet.{Color.RESET}")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✗"
        color = Color.GREEN if task["done"] else Color.RED
        print(f"{color}[{status}] {i}. {task['title']}{Color.RESET}")

def add_task(tasks, title):
    """Adds a new task to the list. Returns True if added, False if empty."""
    title = title.strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        beep()
        print(f"{Color.GREEN}Task added!{Color.RESET}")
        return True
    else:
        print(f"{Color.RED}Task cannot be empty.{Color.RESET}")
        return False

def complete_task(tasks, index):
    """Marks a task complete by index. Returns True if successful."""
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        beep()
        print(f"{Color.GREEN}Task completed!{Color.RESET}")
        return True
    except IndexError:
        print(f"{Color.RED}Invalid selection.{Color.RESET}")
        return False

def delete_task(tasks, index):
    """Deletes a task by index. Returns the removed task title if successful."""
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        beep()
        print(f"{Color.RED}Deleted: {removed['title']}{Color.RESET}")
        return removed["title"]
    except IndexError:
        print(f"{Color.RED}Invalid selection.{Color.RESET}")
        return None

# ---------------------------
# UI LOOP
# ---------------------------
def main():
    typewrite(f"{Color.CYAN}{Color.BOLD}Welcome to CLI Todo App!{Color.RESET}")
    tasks = load_tasks()

    while True:
        print("\n" + "=" * 30)
        print(f"{Color.BOLD}CLI TODO APP{Color.RESET}")
        print("=" * 30)
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("\nChoose option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter new task: ")
            add_task(tasks, title)
        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Task number to mark complete: ")) - 1
                complete_task(tasks, index)
            except ValueError:
                print(f"{Color.RED}Please enter a number.{Color.RESET}")
        elif choice == "4":
            show_tasks(tasks)
            try:
                index = int(input("Task number to delete: ")) - 1
                delete_task(tasks, index)
            except ValueError:
                print(f"{Color.RED}Please enter a number.{Color.RESET}")
        elif choice == "5":
            typewrite("Goodbye!")
            break
        else:
            print(f"{Color.YELLOW}Invalid option.{Color.RESET}")

        time.sleep(0.5)

if __name__ == "__main__":
    main()