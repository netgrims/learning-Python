import time, os

todoList = []

def prettyPrint():
  for row in range(len(todoList)):
    print("-------------------------|----------------|-----------|")
    print(f"{todoList[row][0]:<25}| {todoList[row][1]:<15}| {todoList[row][2]:<10}|")
    print("-------------------------|----------------|-----------|")

def prettyPrintRow(row):
  print("-----------NAME----------|------DUE-------|-PRIORITY--|")
  print("-------------------------|----------------|-----------|")
  print(f"{todoList[row][0]:<25}| {todoList[row][1]:<15}| {todoList[row][2]:<10}|")
  print("-------------------------|----------------|-----------|")

while True:
  print("""
  
      ████████╗ ██████╗       ██████╗  ██████╗ 
      ╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗
         ██║   ██║   ██║█████╗██║  ██║██║   ██║
         ██║   ██║   ██║╚════╝██║  ██║██║   ██║
         ██║   ╚██████╔╝      ██████╔╝╚██████╔╝
         ╚═╝    ╚═════╝       ╚═════╝  ╚═════╝ 
                                         
======================================================
  """)
  print()
  menu = input("Do you want to add, view, remove, or edit a task? \n(add/view/remove/edit)\n> ")
  print()
  # add option
  if menu.strip().lower()[0] == "a":
    taskName = input("What is the task? ")
    taskDue = input("When is it due by? ")
    taskPrior = input("What is the priority? ")
    newTask = [taskName, taskDue, taskPrior]
    todoList.append(newTask)
    print()
    print("Your task has been added.")
    time.sleep(1.5)
    os.system("clear")
  # remove option
  if menu.strip().lower()[0] == "r":
    removeMenu = input("Which item do you want to remove? \n> ")
    found = False
    for taskRow in range(len(todoList)):
      if todoList[taskRow][0] == removeMenu:
        found = True
        toRemove = todoList[taskRow]
    todoList.remove(toRemove)
    print(f"{toRemove[0]} removed from the to-do list.")
    toRemove = None
    time.sleep(1.5)
    os.system("clear")
    if found == False:
      print()
      print("Sorry, the task you are looking for cannot be found.")
  # view option
  if menu.strip().lower()[0] == "v":
    viewMenu = input("Do you want to view all tasks, or only tasks of a certain priority? \n(all/priority) \n> ")
    if viewMenu == "all": 
      prettyPrint()
    elif viewMenu == "priority":
      viewPriorityMenu = input("Which priority would you like to view? \n> ")
      for taskRow in range(len(todoList)):
        if viewPriorityMenu in todoList[taskRow]:
          prettyPrintRow(taskRow)
    print()
    returnMenu = input("Return to menu? (yes/no) \n> ")
    if returnMenu.strip().lower()[0] == "y":
      os.system("clear")
      continue
  # edit option
  if menu.strip().lower()[0] == "e":
    editName = input("Which task do you want to edit? \n> ")
    found = False
    for taskRow in range(len(todoList)):
      if todoList[taskRow][0] == editName:
        found = True
        prettyPrintRow(taskRow)
        editMenu = input("Do you want to edit the task name, due time, or priority? \n(name/due/priority) \n> ")
        editInput = input("What do you want to change it to? \n> ")
        if editMenu == "name":
          editCode = 0
        elif editMenu == "due":
          editCode = 1
        elif editMenu == "priority":
          editCode = 2
        todoList[taskRow][editCode] = editInput
        print()
        print("Task modified.")
        time.sleep(1.5)
        os.system("clear")
      elif found == False:
        print()
        print("Sorry, the task you are looking for cannot be found.")
        time.sleep(1.5)
        os.system("clear")
  os.system("clear")
