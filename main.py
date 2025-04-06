def add_task(incomplete_tasks):
    task = input("Please insert task: ")
    incomplete_tasks.append(task)


def list_tasks(pending_tasks, completed_tasks):
    print("\nPending tasks:")
    if len(pending_tasks) == 0:
        print("None")
    else:
        for i, task in enumerate(pending_tasks):
            print(f"{i + 1}: {task}")

    print("\nCompleted tasks:")
    if len(completed_tasks) == 0:
        print("None")
    else:
        for i, task in enumerate(completed_tasks):
            print(f"{i + 1}: {task}")
    print()


def mark_as_completed(pending_tasks, completed_tasks):
    print("\nPending tasks:")
    if len(pending_tasks) == 0:
        print("None")
    else:
        for i, task in enumerate(pending_tasks):
            print(f"{i + 1}: {task}")

    taskNumber = int(input("\nPlease input task number: "))
    while taskNumber < 0:
        taskNumber = int(input("\nPlease input a positive task number: "))


    completed_tasks.append(pending_tasks.pop(taskNumber - 1))


def save(filename, lst):
    string = "\n".join(lst)
    with open(filename, "w") as file:
        file.write(string)


def delete_task(pending_tasks, completed_tasks):
    taskStatus = input("\nIs the task you wish to delete completed? [y/N]: ")
    relevantList = []
    if taskStatus == "y":
        relevantList = completed_tasks
    else:
        relevantList = pending_tasks

    taskNumber = int(input("\nPlease input task number: "))

    if taskNumber > 0 and taskNumber <= len(pending_tasks):
        relevantList.pop(taskNumber - 1)


def load_tasks(filename):
    tasks = []
    with open(filename) as file:
        task = file.readline()
        while task:
            tasks.append(task.strip())
            task = file.readline()
    return tasks


def main():

    quit = False

    print("Todo-listinator 3000\n")

    tasks = load_tasks("data/tasks.txt")
    completed_tasks = load_tasks("data/completed_tasks.txt")

    while not quit:
        print(
            """a: Add task 
l: List tasks 
m: Mark task as completed
d: Delete task
q: Quit and save tasks
"""
        )
        operation = input("Please select operation: ")

        match operation[0]:
            case "a":
                add_task(tasks)
            case "l":
                list_tasks(tasks, completed_tasks)
            case "m":
                mark_as_completed(tasks, completed_tasks)
            case "d":
                delete_task(tasks, completed_tasks)
            case "q":
                save("data/tasks.txt", tasks)
                save("data/completed_tasks.txt", completed_tasks)
                quit = True


if __name__ == "__main__":
    main()
