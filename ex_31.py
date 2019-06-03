x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def divide(arr):
    #print(arr)
    ctr = 0 
    a,b,c,d = [],[],[],[]
    for e in arr:
        ctr = ctr + 1
        a.append(e)
        if ctr>=0 and ctr<=5:
            b.append(e)
        if ctr>=6 and ctr<=10:
            c.append(e)
        if ctr>=11 and ctr<=15:
            d.append(e)
        if ctr>=16 and ctr<=20:
            
print divide(x)
