c=eval(input('Introduceti numarul :'))
x=1
suma=0
Produsul=1
while x<=c:
    Produsul*=x
    suma+=x
    x+=1

print('Suma numerelor =', suma )
print('Produsul numerelor =', Produsul)
print('Media aritmetica a numerelor =',suma/c)