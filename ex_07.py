def computepay(hours, rate) :
    if xh > 40 :
        reg = xr * xh
        otp = (xh - 40.0) * (xr * 0.5)
        pay = reg + otp
    else:
        pay = xh * xr
 
    return pay

gh = input("Enter hours: ")
gr = input("Enter rate: ")
xh = float(gh)
xr = float(gr)


xp = computepay(xh, xr)
print (xp)
