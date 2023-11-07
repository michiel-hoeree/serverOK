import sys
import json
import os


def createHtml():
    servers = lsServer()
    with open("htmlTemplates/template.html") as file:
        template = file.read()
    with open("htmlTemplates/headColumn.txt") as file:
        headColumnTemplate = file.read()
    with open("htmlTemplates/serverColumn.txt") as file:
        serverColumnTemplate = file.read()

    html = template
    headColumn = headColumnTemplate.replace("name","servername")
    html = html.replace("headColumn",f"{headColumn}headColumn")
    serverColumn = serverColumnTemplate.replace("data","pingCheck")
    html = html.replace("serverColumn",f"{serverColumn}serverColumn")

    for server in servers:
        headColumn = headColumnTemplate.replace("name",server["name"])
        html = html.replace("headColumn",f"{headColumn}headColumn")
        for check in server:
            if check != "name":
                serverColumn = serverColumnTemplate.replace("data",str(server[check]))
                html = html.replace("serverColumn",f"{serverColumn}serverColumn")

    html = html.replace("headColumn","")
    html = html.replace("serverColumn","")
    
    
    
    with open("results.html","w") as file:
        file.write(html)
    


def ping(host):
    return True         #ik wil niet wachten op een respons.
    response = os.system("ping -n 4 " + host)
    if response == 0:
        return True
    else:
        return False



def pingCheck():
    servers = lsServer()
    responses = []
    for server in servers:
        response = ping(server["name"])
        server["ping"].append(response)
    y = json.dumps(servers)
    with open("servers.json","w") as file:
        file.write(y)
    return responses

def checks():
    pingCheck()
    createHtml()

def addServer(serverName):
    servers = lsServer()
    servers.append({"name": serverName,"ping": []})
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


def lsServer():                 # return dict of servers
    with open("servers.json") as file:
        servers = json.load(file)
    return servers


def interface():
    while True:
        toDo= input("""Wilt u:
1)Een server toevoegen?
2)Een server verwijderen?
3)Alle servers zien?
4)De checks uivoeren?
0)Exit
""")
        while toDo not in ["1","2","3","4","0"]:
            toDo= input(f"""\"{toDo}\" was geen optie
Wilt u:
1)Een server toevoegen?
2)Een server verwijderen?
3)Alle servers zien?
4)De checks uitvoeren?
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
            case "4":
                pingCheck()
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
    elif len(sys.argv) > 1 and sys.argv[1] == "checks":
        checks()
    else:
         print("do not man things")


def main():
    if len(sys.argv) > 1:
        terminal()
    else:
        interface()
            

if __name__ == "__main__":
	main()