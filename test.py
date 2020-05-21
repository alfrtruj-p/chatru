test = input(f'ok?: ')
lis = list(test)
new = []
b = []
for x in lis:
    print(x)
   if x in ('a', 'e'):
        if lis.index(x) == 0:
            new.append(x)
            lis.remove(x)
            print('yes')
        else:
            print('no')
    else:
        print('afuera')
print(new)
print(lis)
b = new + lis
print(b)






