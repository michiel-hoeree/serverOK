import sys
import json


def addServer(serverName):
    servers = lsServer()
    servers.append({"name": serverName})
    y = json.dumps(servers)
    with open("servers.json","w") as file:
        file.write(y)


def rmServer(serverName):
    servers = lsServer()
    for index, server in enumerate(servers):
        if server["name"] == serverName:
            servers.pop(index)
    y = json.dumps(servers)
    with open("servers.json","w") as file:
        file.write(y)


def printLsServer():
    servers = lsServer()
    for server in servers:
        print(server["name"])


def lsServer():
    with open("servers.json") as file:
        servers = json.load(file)
    return servers


def interface():
    while True:
        toDo= input("""Wilt u:
1)Een server toevoegen?
2)Een server verwijderen?
3)Alle servers zien?
0)Exit
""")
        while toDo not in ["1","2","3","0"]:
            toDo= input(f"""\"{toDo}\" was geen optie
Wilt u:
1)Een server toevoegen?
2)Een server verwijderen?
3)Alle servers zien?
0)Exit
""")
        match toDo:
            case "1":
                serverName = input("hoe noemt de nieuwe server?\n")
                addServer(serverName)
            case "2":
                serverName = input("Welke server wilt u verwijderen?\n")
                rmServer(serverName)
            case "3":
                printLsServer()
            case "0":
                sys.exit(0)

def terminal():
    if len(sys.argv) > 2 and sys.argv[1] == "man":
          match sys.argv[2]:
                case "add":
                    if len(sys.argv) > 3: 
                        for server in sys.argv[3:]:
                            addServer(server)
                    else:
                        serverName = input("hoe noemt de nieuwe server?\n")
                        addServer(serverName)
                case "rm":
                    if len(sys.argv) > 3: 
                        for server in sys.argv[3:]:
                            rmServer(server)
                    else:
                        serverName = input("Welke server wilt u verwijderen?\n")
                        rmServer(serverName)
                case "ls":
                    printLsServer()
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