def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        f.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("Vazifalar yo‘q.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Vazifa qo‘shish\n2. Ko‘rish\n3. O‘chirish\n4. Chiqish")
        choice = input("Tanlang: ")

        if choice == "1":
            task = input("Yangi vazifa: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Qaysi vazifani o‘chirish (raqami)? "))
            if 0 < idx <= len(tasks):
                tasks.pop(idx - 1)
                save_tasks(tasks)
        elif choice == "4":
            break
        else:
            print("Noto‘g‘ri tanlov.")

if __name__ == "__main__":
    main()
