import serial
import os

connectie = serial.Serial('/dev/ttyACM1',baudrate=1200)
print(connectie)
WACHTWOORD = "kerstpuzzel" # TEMP
poging_wachtwoord = ""
i = []
file = 'bigdata.txt'
size = os.path.getsize(file)
pointer = 0
fouten = 0

def readbyte(pointer):
    f = open(file, "r")
    f.seek(pointer)
    re: str = f.read(1)
    return re

def verstuur_bestand(pointer):
    for x in range(size):
        returned = readbyte(pointer)
        print(returned.encode('utf-8').hex())
        connectie.write(bytes(returned, 'utf-8'))
        if pointer == size:
            pointer = 0
        else:
            pointer = pointer + 1



while True:
    if fouten == 3:
        print("teveel foute wachtwoorden.")
        connectie.close()
        # Connectie gesloten
        while True:
            pass # hier later constant reset knop uitlezen, dan alles resetten. 

    a = connectie.read()
    i.append(a.decode())
    try:
        i.remove('\n')
        i.remove('\r')
    except:
        pass

    poging_wachtwoord = "".join(i)
    poging_wachtwoord.replace('\r', '')

    if len(WACHTWOORD) == len(poging_wachtwoord):
        if '\r' in i or '\r' in poging_wachtwoord:
            i.remove('\r')
            poging_wachtwoord = ''.join(i)
            poging_wachtwoord.replace('\r', '')
            print(poging_wachtwoord)
            continue
        if WACHTWOORD == poging_wachtwoord:
            print("wachtwoord correct")
            verstuur_bestand(pointer)
        else:
            fouten = fouten + 1
            poging_wachtwoord = ""
            print("wachtwoord fout")
