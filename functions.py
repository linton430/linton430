n = int(input("please provide the temperature value: "))

corf = input("Is this Celsius, y/n? ")

def ctof(c):
    f = (c *9/5) + 32
    return f

def ftoc(f):
    c = (f - 32)/1.8
    return c
if corf == 'y':
    print(ctof(n))
else :
    print(ftoc(n)) 
