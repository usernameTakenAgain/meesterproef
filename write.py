import serial

connectie = serial.Serial('/dev/ttyACM0', baudrate=1200)
print(connectie)
while True:
	connectie.write(b"18")
