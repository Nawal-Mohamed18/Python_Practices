print("----TO DO LIST----")
print("""1. View Tasks
2. Add Task
3. Remove Task
4. Exit""")

while True:
    choice = int(input("Enter your choice (1-4): "))

    to_do_list = []

    if choice == 1:
        if len(to_do_list) == 0:
            print("No tasks yet.")
        else:    
            print(f"TO DO LIST:\n{to_do_list}")

    elif choice == 2:
        new_task = input("Enter new task: ")
        to_do_list.append(new_task)

        print(f"{new_task} added.")

    elif choice == 3:
         if len(to_do_list) == 0:
             print("No task to remove.")
         else:
             task_num = int(input("Choose a task number: "))
             index =+ task_num-1

             to_do_list.pop(index)

             print(f"{to_do_list[index]} removed.")
             
    elif choice == 4:
          print("Exitting..")
          exit()
          
             
             
