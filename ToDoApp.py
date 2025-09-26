tasks = []

def addTask():
    while True:
        newTask = input("Enter task: ")

        if newTask.capitalize() in tasks: 
            print("Task already exists.")

        elif newTask.isdigit(): #Checks if the input is a number
            print("Invalid Input.")
    
        else:
            tasks.append(newTask.capitalize()) #Appends the "Task" if it is not a number or duplicate

            print("Task added!")
            break
    print("---------------------------")

def showTasks( ):
    print("---------------------------")
    print("TASKS:")

    if len(tasks) == 0 :
        print("No tasks yet")

    else:
        for i in range (len(tasks)):
            print(i+1,".",tasks[i])
    print("---------------------------")        

def removeTask(removeIndex):
    if removeIndex < 1 or removeIndex > len(tasks):
       print("Invalid Task Number")

    else:
        removeIndex -= 1
        taskToRemove = tasks[removeIndex]  #get the last removed task name
        tasks.pop(removeIndex) 
        print(f"Task \"{taskToRemove}\" has been removed!")
    print("---------------------------")

def main():
    while True:
        print("\tMAIN MENU")
        print("---------------------------")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice : ")
        if choice == "1":

            addTask()

        elif choice == "2":
            showTasks()

        elif choice == "3":
            removeIndex = int(input("Enter Task No. to Remove: "))
            removeTask(removeIndex)  

        elif choice == "4":
            break #this has a semi-colon which is not needed
        
        else:
            print("Invalid Input! Please try again.")

main()

