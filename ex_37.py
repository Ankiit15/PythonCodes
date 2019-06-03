h = raw_input("Enter file name: ")
if len(h) < 1 : h = "mbox-short.txt"

ch = open(h)
cd = 0

for line in ch:
    line.rstrip()
    if line.startswith("From "):
        words = line.split()
        print words[1]
        cd += 1

print ("There were 27 lines in the file with From as the first word")
	
    

