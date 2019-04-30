gh = input("Enter hours: ")
gr = input("Enter rate: ")
xh = float(gh)
xr = float(gr)

if xh > 40 :
    reg = xr * xh
    otp = (xh - 40.0) * (xr * 0.5)
    xp = reg + otp
else:
    xp = xh * xr
print ("Pay:",xp)
