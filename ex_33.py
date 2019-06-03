def multiply(myarray) :
    result = 0
    for x in myarray :
        result = result + (2*x) 
    return result

def sumOfProducts(a):
    sum = 0
    for e in a:
        sum = sum + (e * 2)
    return sum

def combine(a1, a2):
    arr = []
    for i in a1 :
        arr.append(i)
    for e in a2 :
        arr.append(e)
    return arr
      

array1 = [1,2,3,4,5]
array2 = [6,7,8,9,10]


print(multiply(array1))
print(sumOfProducts(array1))

print(combine(array1, array2))




