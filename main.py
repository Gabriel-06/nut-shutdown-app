import PyNUT
import time

originalTime=0
state=0

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
shutdownTime = cleanString(dataFile.readline())

shutdownTime = shutdownTime*60,000

print(login)
print(password)
print(host)
print(port)
print(upsName)
print(shutdownTime)

ups_handler=PyNUT.PyNUTClient(host=host, port=port, login=login, password=password)
upsInfo = ups_handler.GetUPSVars(upsName)

while True:
    upsInfo = ups_handler.GetUPSVars(upsName)

    if upsInfo['ups.status']=='OB DISCHRG' and state!=1:
        originalTime = time.time()
        state=1
        
    if upsInfo['ups.status']=='OB DISCHRG' :
        if(int(originalTime)+int(  shutdownTime))==time.time():
            #TODO shutdown computer
        print("PANIC")
    if upsInfo['ups.status']=='OL':
        state=0

