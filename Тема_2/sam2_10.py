a,b,c = "hello"," my ","world!"
print(a[:4]+a[:3][2:]*len(b)+a[4:]*len(b) + b + c)