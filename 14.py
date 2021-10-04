n=int(input('Introduceti numarul de linii matrice: '))
m=[]
dp=0
ds=0
c=0
d=0
e=0
f=0
if n>=2 and n<=10:
    for x in range(n):
        m.append([])
    for x in m:
        print('sir:',m.index(x)+1)
        for j in range(n):
            x.append(int(input('nuamrul: ')))
    for z in range(0,len(m)):
        dp+= m[z][z]
        print('a)suma pe diagonala principala: ',dp)
        
        ds += m[len(m)-z-1][z]
        print('b)suma pe diagonala secundara: ',ds)
    for x in range(n):
        for z in range(n):
            if x<z:
                c +=m[x][z]
                print('c)Suma mai sus de diagonala principală este ', c)
            if x>z: 
                d+=m[x][z]
                print('d)Suma mai joc de diagonala principală este ', d)
            if z+x<n-1:
                e+=m[x][z]
                print('e)Suma mai sstanga de diagonala principală este ', e)
            if z+x>n-1:
                f+=m[x][z]
                print('f)Suma mai dreapta de diagonala principală este ', f)
else:
    print('erorrr')