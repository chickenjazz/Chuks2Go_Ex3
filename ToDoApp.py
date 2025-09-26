# toDoApp.py

tasks=[]

def addtask(task) :
  tasks.append(task)
  print("task added!")

def showTasks( ):
    if len(tasks) == 0 :
        print("no tasks yet")
    else:
        for i in range (len(tasks)):
            print(i+1,".",tasks[i])

def removeTask(removeIndex):
    if removeIndex < 1 or removeIndex > len(tasks):
       print("Invalid Task Number")
    else:
        removeIndex -= 1
        taskToRemove = tasks[removeIndex]  #get the last removed task name
        tasks.pop(removeIndex) 
        print(f"Task \"{taskToRemove}\" has been removed!")

def main():
    while True: #TODO: improve user interface
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")

        ch = input("enter choice : ")
        if ch=="1":
            t = input("enter task : ")
            addtask(t)

        elif ch=="2":
            showTasks()

        elif ch=="3":
            removeIndex = int(input("Enter Task No. to Remove: "))
            removeTask(removeIndex)  

        elif ch=="4":
            break #this has a semi-colon which is not needed
        
        else:
            print("wrong choice!!")
main()
#commented