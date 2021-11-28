file = open("data.txt","r")
line1 = file.readline()
print(line1.upper())

print(f"Total number of words: {len(line1.split())}")
line2 = file.readline()[1:]
print(line2.upper())
print(f"Total number of words: {len(line2.split())}")
file.close()
