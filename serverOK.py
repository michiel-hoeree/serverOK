import sys

def addServer():
     print("adding server")

def rmServer():
     print("rming server")


def lsServer():
     print("here are all servers")


def interface():
    print("Wilt u:")
    print("1)Een server toevoegen?")
    print("2)Een server verwijderen?")
    print("3)Alle servers zien?")
    toDo = input("")
    match toDo:
         case "1":
              addServer()
         case "2":
              rmServer()
         case "3":
              lsServer()

def terminal():
     pass


def main():
    if len(sys.argv) > 1:
        terminal()
    else:
        interface()
            

if __name__ == "__main__":
	main()