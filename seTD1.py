
import threading

tampon = [" "] * 4
pointeurLecture = 0
pointeurEcriture = 0

def verifErreur(pos):
	global pointeurLecture
	if pos == len(tampon):
		pointeurLecture = 0
	else:
		return False

def readBuffer():
	global pointeurLecture
	if not verifErreur(pointeurLecture):		
		if tampon[pointeurLecture] == "E":
			tampon[pointeurLecture] = " "
			pointeurLecture += 1
		else:
			tampon[pointeurLecture] = "L"
		

def writeBuffer():
	global pointeurEcriture
	if not verifErreur(pointeurEcriture):
		tampon[pointeurEcriture] = "E"
		pointeurEcriture += 1
		


writeBuffer()

print(tampon)
readBuffer()
print(tampon)

writeBuffer()
print(tampon)
readBuffer()
print(tampon)
writeBuffer()
print(tampon)
writeBuffer()
print(tampon)
writeBuffer()
print(tampon)
writeBuffer()
print(tampon)
writeBuffer()
print(tampon)




