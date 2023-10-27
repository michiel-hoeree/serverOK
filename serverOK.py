import sys

def addServer(serverName):
     print(f"adding server {serverName}")

def rmServer(serverName):
     print(f"rming server {serverName}")


def lsServer():
     print("here are all servers")


def interface():
    toDo= input("""Wilt u:
1)Een server toevoegen?
2)Een server verwijderen?
3)Alle servers zien?
""")
    while toDo not in ["1","2","3"]:
         toDo= input(f"""\"{toDo}\" was geen optie
Wilt u:
1)Een server toevoegen?
2)Een server verwijderen?
3)Alle servers zien?
""")
    match toDo:
         case "1":
              serverName = input("hoe noemt de nieuwe server?\n")
              addServer(serverName)
         case "2":
              serverName = input("Welke server wilt u verwijderen?\n")
              rmServer(serverName)
         case "3":
              lsServer()

def terminal():
    if len(sys.argv) > 2 and sys.argv[1] == "man":
          match sys.argv[2]:
                case "add":
                    if len(sys.argv) > 3: 
                        addServer(sys.argv[3])
                    else:
                        serverName = input("hoe noemt de nieuwe server?\n")
                        addServer(serverName)
                case "rm":
                    if len(sys.argv) > 3: 
                        rmServer(sys.argv[3])
                    else:
                        serverName = input("Welke server wilt u verwijderen?\n")
                        rmServer(serverName)
                case "ls":
                    lsServer()
                case _:
                    print("incorrect man commando")
    else:
         print("do not man things")


def main():
    if len(sys.argv) > 1:
        terminal()
    else:
        interface()
            

if __name__ == "__main__":
	main()