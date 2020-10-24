b=0
suma=0
while not((b%2!=0) and (b%3==0)):
    b=eval(input('Introduceti numarul:'))
    if b%2==0:
        suma+=b

print('Suma numerelor =', suma)
