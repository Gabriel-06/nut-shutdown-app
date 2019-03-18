import PyNUT
import time

def cleanString(inText):
    inText = inText.rstrip()
    params, inText = inText.split("=",1)
    inText = str(inText)
    return inText


dataFile = open("NUT.conf", "r")
login = cleanString(dataFile.readline())
password = cleanString(dataFile.readline())
host = cleanString(dataFile.readline())
port = cleanString(dataFile.readline())
upsName = cleanString(dataFile.readline())

print(login)
print(password)
print(host)
print(port)
print(upsName)

ups_handler=PyNUT.PyNUTClient(host=host, port=port, login=login, password=password)
upsInfo = ups_handler.GetUPSVars("qnapups")

print(upsInfo)

while True:
    upsInfo = ups_handler.GetUPSVars("qnapups")
    time.sleep(1000)
