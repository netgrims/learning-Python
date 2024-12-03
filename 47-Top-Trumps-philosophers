import os, time, random

philosophers = {
  "Kant":{"consistency":8,"ethics":4,"novelty":9,"Je ne sais quoi":2},
  "Sartre":{"consistency":3,"ethics":2,"novelty":7,"Je ne sais quoi":9},
  "Plato":{"consistency":2,"ethics":4,"novelty":9,"Je ne sais quoi":4},
  "Zizek":{"consistency":6,"ethics":2,"novelty":9,"Je ne sais quoi":10}
               }

def titlePrint():
  print("""
==================================================================
   _____              _____                                  
  /__   \___  _ __   /__   \_ __ _   _ _ __ ___  _ __  ___ _ 
    / /\/ _ \| '_ \    / /\/ '__| | | | '_ ` _ \| '_ \/ __(_)
   / / | (_) | |_) |  / /  | |  | |_| | | | | | | |_) \__ \_ 
   \/   \___/| .__/   \/   |_|   \__,_|_| |_| |_| .__/|___(_)
             |_|                                |_|          
------------------------------------------------------------------
                _____                                            
               (, /   ) /)   ,  /)                /)             
                _/__ / (/      // ___ _   _____  (/    _  __  _  
                /      / )__(_(/_(_) /_)_(_) /_)_/ )__(/_/ (_/_)_
             ) /                          .-/                    
            (_/                          (_/                     
==================================================================
  """)

def prettyPrintNames():
  for key, value in philosophers.items():
    print(f"- {key}")

def prettyPrintStats(playerPhilosopher):
  counter = 0
  for key, value in playerPhilosopher.items():
    counter += 1
    print(f"{counter}. {key:<16}:{value}")

def computerChoice():
  while True:
    computerPick = random.choice(list(philosophers.keys()))
    if computerPick == playerPhilosopherName:
      continue
    else:
      return computerPick

while True:
  os.system("clear")
  titlePrint()
  menu = input("Do you want to play Top Trumps or add a new philosopher to your deck? \n(play/add)\n> ")
  os.system("clear")
  titlePrint()
  if menu.strip().lower()[0] == "a":
    name = input("Which philosopher do you want to add? \n> ")
    consistency = int(input("What is their consistency score? \n> "))
    ethics = int(input("What is their ethics score? \n> "))
    novelty = int(input("What is their novelty score? \n> "))
    quoi = int(input("What is their je-ne-sais-quoi score? \n> "))
    philosophers[name] = {"consistency":consistency,"ethics":ethics,"novelty":novelty,"Je ne sais quoi":quoi}
    print(philosophers)

  elif menu.strip().lower()[0] == "p":
    print()
    print("Pick a philosopher: ")
    prettyPrintNames()
    print()
    while True:
      playerChoice = input("> ")
      found = False
      for key, value in philosophers.items():
        if playerChoice.strip().title() == key:
          playerPhilosopherDict = philosophers[key]
          playerPhilosopherName = playerChoice.strip().title()
          found = True
      if found == False:
        print("This philosopher cannot be found. Please enter another one, or add this philosopher to your deck.")
        continue
      elif found == True: 
        print()
        print(f"{playerChoice.strip().title()} selected.")
        print()
        computerPhilosopher = computerChoice()
        print()
        print(f"The compuiter has picked {computerPhilosopher}")
        print()
        time.sleep(3)
        os.system("clear")
        titlePrint()
        print("Choose your stat (1/2/3/4):")
        prettyPrintStats(playerPhilosopherDict)
        statMenu = input("\n> ")
        print()
        if statMenu == "1":
          statChoice = "consistency"
        elif statMenu == "2":
          statChoice = "ethics"
        elif statMenu == "3":
          statChoice = "novelty"
        elif statMenu == "4":
          statChoice = "Je ne sais quoi"
        else: 
          print("Error. Returning to menu.")
          continue
        print(f"You chose {statChoice}:")
        print(f"{playerPhilosopherName}: {philosophers[playerPhilosopherName][statChoice]}")
        print(f"{computerPhilosopher}: {philosophers[computerPhilosopher][statChoice]}")
        print()
        time.sleep(3)
        os.system("clear")
        titlePrint()
        print()
        if (philosophers[playerPhilosopherName][statChoice]) > (philosophers[computerPhilosopher][statChoice]):
          winner = NotImplemented
          print("""
          
            __  __                        _       __
            \ \/ /___  __  __   _      __(_)___  / /
             \  / __ \/ / / /  | | /| / / / __ \/ / 
             / / /_/ / /_/ /   | |/ |/ / / / / /_/  
            /_/\____/\__,_/    |__/|__/_/_/ /_(_)   

                                                        
          """)
        elif (philosophers[playerPhilosopherName][statChoice]) < (philosophers[computerPhilosopher][statChoice]):
          winner = NotImplemented
          print("""

            __  __               __           __ 
            \ \/ /___  __  __   / /___  _____/ /_
             \  / __ \/ / / /  / / __ \/ ___/ __/
             / / /_/ / /_/ /  / / /_/ (__  ) /_  
            /_/\____/\__,_/  /_/\____/____/\__/  
                                                     

          """)
        elif (philosophers[playerPhilosopherName][statChoice]) == (philosophers[computerPhilosopher][statChoice]):
          winner = NotImplemented
          print("""
                    
        ______ _                       __                       
       /  _/ /( )_____   ____ _   ____/ /________ __      __    
       / // __/// ___/  / __ `/  / __  / ___/ __ `/ | /| / /    
     _/ // /_  (__  )  / /_/ /  / /_/ / /  / /_/ /| |/ |/ / _ _ 
    /___/\__/ /____/   \__,_/   \__,_/_/   \__,_/ |__/|__(_|_|_)
                                                                      
          
          """)
        print()
        time.sleep(1.5)
        input("Play again? ")
        break
      continue
