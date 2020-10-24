n=1
suma_p=0
suma_n=0
nr_p=0
nr_n=0
while n<=12:
    t=eval(input('Scriti temperaturile:'))
    if t>=0:
        suma_p+=t
        nr_p+=1
    if t<0:
        suma_n+=t
        nr_n+=1
    n+=1

print('Media anuala a temperaturilor pozitive =',(round(suma_p/nr_p,2)))
print('Media anuala a temperaturilor negative =',(round(suma_n/nr_n,2)))