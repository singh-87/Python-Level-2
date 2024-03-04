"""#Dynamic typing to a file
f = open("999.txt","w")
while True:
    data = input("What do you want to say:")
    f.write(data+'\n')
    user = input("Enter 'c' to continue or 'q' to quit:")
    if user=='q':
        break
f.close()"""
"""#Performing readlines
f = open("Malaysia sebagai.txt",'r')
data = f.readlines()
print(data)
data2 = map(lambda x: x[0:-1],data)
print(list(data2))
data3 = filter(lambda x: x[-2]=='j',data)
print(list(data3))
f.close()"""
#Word count , letter count, line count
f = open("Malaysia sebagai.txt",'r')
word_count=letter_count=line_count = 0
print(letter_count)
for i in f:
    line_count+=1
    word_count = word_count+len(i.split(" "))
    letter_count = letter_count+len(i)
print(f"Line count = {line_count}")
print(f"Word count = {word_count}")
print(f"Letter count = {letter_count}")