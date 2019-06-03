d=input("Enter your file name : ")
s = open("romeo.txt")
c = dict()
t = list()
for i in s:
        words = .split()
        for word in words:
            if word not in t:
                t.append(word)
t.sort()
print(t)
