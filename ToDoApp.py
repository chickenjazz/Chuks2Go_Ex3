tasks = []

def add_task():
    while True:
        new_task = input("Enter task: ")

        if new_task.capitalize() in tasks: 
            print("Task already exists.")

        elif new_task.isdigit(): #Checks if the input is a number
            print("Invalid Input.")
    
        else:
            tasks.append(new_task.capitalize()) #Appends the "Task" if it is not a number or duplicate

            print("Task added!")
            break
    print("---------------------------")

def show_tasks( ):
    print("---------------------------")
    print("TASKS:")

    if len(tasks) == 0 :
        print("No tasks yet")

    else:
        for i in range (len(tasks)):
            print(i+1,".",tasks[i])
    print("---------------------------")        

def remove_task(remove_index):
    if remove_index < 1 or remove_index > len(tasks):
       print("Invalid Task Number")

    else:
        remove_index -= 1
        task_to_remove = tasks[remove_index]  #get the last removed task name
        tasks.pop(remove_index) 
        print(f"Task \"{task_to_remove}\" has been removed!")
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

            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            try:
                remove_index = int(input("Enter Task No. to Remove: "))
                remove_task(remove_index)  
            except ValueError:
                print("Invalid Input! Please enter a digit")

        elif choice == "4":
            break #this has a semi-colon which is not needed
        
        else:
            print("Invalid Input! Please try again.")

 
main()

