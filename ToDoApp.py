tasks = []

def addTask():
    while True:
        new_task = input("Enter task: ")

        if new_task.capitalize() in tasks:
            print("You already have that task")

        elif new_task.isdigit():
            print("You cannot have a digit in here")
    
        else:
            tasks.append(new_task.capitalize())
            print("task added!")
            break

def showTasks():
    if len(tasks) == 0:
      print("no tasks yet")

    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i], sep = "")

def removeTask(tasknumber):
    tasks.pop(tasknumber) 
    print("task removed!!")

def main():
    while True: #TODO: improve user interface
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        user_choice = input("enter choice : ")

        if user_choice == "1":
            addTask()

        elif user_choice == "2":
            showTasks()

        elif user_choice == "3": #BUG: logical error here -- index mismatch (removes element at index n+1)
            n = int(input("enter task no to remove: "))
            removeTask(n)   

        elif user_choice == "4":
            break

        else:
            print("wrong choice!!")

main()
