file = open("questions2.txt")


a = [0,1]
for pos, i in enumerate(file):
    if pos in a:
        print(i)
    
file.close()

file = open("questions2.txt")

b = [2]
for pos, i in enumerate(file):
    if pos in b:
        if 