import PyNUT
import time
import os

originalTime=0
state=0

def cleanString(inText):
    inText = inText.rstrip()
    params, inText = inText.split("=",1)
    inText = str(inText)
    return inText

def notify(title, text, sound):
    os.system("""osascript -e 'display notification "{}" with title "{}" sound name "{}"'
              """.format(text, title, sound))



dataFile = open("NUT.conf", "r")
login = cleanString(dataFile.readline())
password = cleanString(dataFile.readline())
host = cleanString(dataFile.readline())
port = cleanString(dataFile.readline())
upsName = cleanString(dataFile.readline())
shutdownTime = cleanString(dataFile.readline())

shutdownTimeMS = shutdownTime*60,000

print(login)
print(password)
print(host)
print(port)
print(upsName)
print(shutdownTimeMS)

ups_handler=PyNUT.PyNUTClient(host=host, port=port, login=login, password=password)
upsInfo = ups_handler.GetUPSVars(upsName)

while True:
    upsInfo = ups_handler.GetUPSVars(upsName)
    print(upsInfo['ups.status'])

    if upsInfo['ups.status']=='OB DISCHRG' and state!=1:
        print("PANIC")
        originalTime = time.time()
        state=1

    if upsInfo['ups.status']=='OB DISCHRG' :
        if(int(originalTime)+int(shutdownTimeMS))==time.time():
            notify("UPS Alert", "Detected UPS power loss. Shutting down computer in "+shutdownTime+" minute(s).", "Funk")
            os.system("open quitall.app")

    if upsInfo['ups.status']=='OL':
        state=0

    time.sleep(10)
