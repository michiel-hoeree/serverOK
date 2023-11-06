import os

def singlePing(host):
    # return True         #ik wil niet wachten op een respons.
    response = os.system("ping -n 4 " + host)
    if response == 0:
        return True
    else:
        return False


def listPing(hostList):
    responses = []
    for host in hostList:
        responses.append(singlePing(host))
    return responses