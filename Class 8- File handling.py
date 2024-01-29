#File handling
#Modes of operations = (r,a,w,r+,w+,a+,x)
"""s = open("Rakuro.txt","r")
data = s.read()
print(data)
s.close()"""
#Write
"""f = open('GM.txt','w')
f.write('Alas Ramos\n')
f.write('turtle.forward()\n')
f.close()"""
#Append
"""f = open('GM.txt','a')
print(f.tell())#1 one
f.write('Hello\n')
f.write('Saajan\n')
print(f.tell())#Last index
f.close()"""
#r+
"""f = open('Rakuro.txt','r+')
#data = f.read()
#print(data)
print(f"File close: {f.closed}")
#f.write('My favourite sport is Badminton\n')
#f.write('I will be going to india\n')
print( )
#f.seek(0)
data2 = f.read()
print(data2)
f.close()
print(f"File close: {f.closed}")"""
"""#Write and read
f = open('Wotashi.txt', 'w+')
f.write('Hello, Wotashi Saajan des\n')
f.write('Ocah kudasai\n')  # This goes to the last position
f.seek(0)  # Get back position to the zero index
data = f.read(5)
data2 = f.readline()  # Reading the second line after f.read()
print(data)
print(data2)
data3 = f.readline()  # Read next line
print(data3)
f.close()"""
#Exclusive operation
"""f = open("Malaysia sebagai.txt",'x')
f.close()"""
"""f = open("tumarah3.txt",'x')
f.write('Hai, Selamat pagi- Good morning\n')
f.write('sat sri akaal- Punjabi form of good morning')
f.close()"""
#Changing from a text to speech
"""import pyttsx3
engine = pyttsx3.init()
f = open("GMS3.txt",'r')
data = f.read()
engine.say(data)
engine.runAndWait()
f.close()"""





