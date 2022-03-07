import serial

connectie = serial.Serial('/dev/ttyACM1',baudrate=1200)
print(connectie)
WACHTWOORD = "kerstpuzzel" # TEMP
gekregen_data = []
poging_wachtwoord = ""

while True:
    print(connectie.read().decode())

