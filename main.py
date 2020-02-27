import PyNUT
import time
import os

originalTime = 0
state = 0


def cleanstring(intext):
    intext = intext.rstrip()
    params, intext = intext.split("=", 1)
    intext = str(intext)
    return intext


def notify(title, text, sound):
    os.system("""osascript -e 'display notification "{}" with title "{}" sound name "{}"'
              """.format(text, title, sound))


logFile = open("../../../NUT_shutdown_log.log", "a")
dataFile = open("../../../NUT.conf", "r")
login = cleanstring(dataFile.readline())
password = cleanstring(dataFile.readline())
host = cleanstring(dataFile.readline())
port = cleanstring(dataFile.readline())
upsName = cleanstring(dataFile.readline())
shutdownTime = cleanstring(dataFile.readline())

shutdownTimeMS = shutdownTime*60000

print(login)
print(password)
print(host)
print(port)
print(upsName)
print(shutdownTimeMS)

ups_handler = PyNUT.PyNUTClient(host=host, port=port, login=login, password=password)
upsInfo = ups_handler.GetUPSVars(upsName)

while True:
    upsInfo = ups_handler.GetUPSVars(upsName)
    print(upsInfo['ups.status'])

    if upsInfo['ups.status'] == 'OL':
        state = 0
        continue

    if upsInfo['ups.status'] == 'OB DISCHRG' and state != 1:
        print("PANIC")
        logFile.write("PANIC: Status OB DISCHRG \n")
        originalTime = time.time()
        state = 1

    if upsInfo['ups.status'] == 'OB DISCHRG':
        if(int(originalTime)+int(shutdownTimeMS)) == time.time():
            notify("UPS Alert", "Detected UPS power loss. "
                                "Shutting down computer in "+shutdownTime+" minute(s).", "Funk")
            os.system("open quitall.app")

    time.sleep(10)
