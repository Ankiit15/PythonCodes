x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def divide(arr):
    #print(arr)
    ctr = 0
    a,b,c,d = [],[],[],[]
    for e in arr:
        ctr = ctr + 1
	print('ctr:' + str(ctr))
        if ctr>=0 and ctr<=5:
            a.append(e)
	    print('condition 1 is executing, adding ' + str(e) + 'to array b...')
        if ctr>=6 and ctr<=10:
            b.append(e)
	    print('condition 2 is executing, adding ' + str(e) + ' to array c...')
        if ctr>=11 and ctr<=15:
            c.append(e)
	    print('condition 3 is executing, adding ' + str(e) + ' array d...')
        if ctr>=16 and ctr<=20:
            d.append(e)
	    print('condition 4 is executing, returning a b c d')
     
    return a, b, c, d 

result = divide(x)
print('------------result-----------')
print(result)
