dh = input("Enter your file name:")
dh = open("words.txt")

for rh in dh:
    fh = rh.rstrip()
    print(fh.upper())
