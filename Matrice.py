Matrice=[[1 ,2 ,3 ,4 ,5],
        [7 ,8 ,9 ,10 ,11],
        [12 ,13 , 14 ,15 ,16],
        [17 ,18 ,19 ,20 ,21],
        [22 ,23 ,24 ,25 ,26]]
R1=Matrice[0][0]+Matrice[0][1]+Matrice[0][2]+Matrice[0][3]+Matrice[0][4]
print('Suma la randul 1=' , R1)
R2=Matrice[1][0]+Matrice[1][1]+Matrice[1][2]+Matrice[1][3]+Matrice[1][4]
print('Suma la randul a 2=' ,R2)
R3=Matrice[2][0]+Matrice[2][1]+Matrice[2][2]+Matrice[2][3]+Matrice[2][4]
print('Suma la randul a 3=' ,R3)
R4=Matrice[3][0]+Matrice[3][1]+Matrice[3][2]+Matrice[3][3]+Matrice[3][4]
print('Suma la randul a 4=' ,R4)
R5=Matrice[4][0]+Matrice[4][1]+Matrice[4][2]+Matrice[4][3]+Matrice[4][4]
print('Suma la randul a 5=' ,R5)
C1=Matrice[0][0]+Matrice[1][0]+Matrice[2][0]+Matrice[3][0]+Matrice[4][0]
print('Suma la coloana 1=' , C1)
c2=Matrice[0][1]+Matrice[1][1]+Matrice[2][1]+Matrice[3][1]+Matrice[4][1]
print('Suma la coloana a 2=' , c2)
c3=Matrice[0][2]+Matrice[1][2]+Matrice[2][2]+Matrice[3][2]+Matrice[4][2]
print('Suma la coloana a 3=' , c3)
c4=Matrice[0][3]+Matrice[1][3]+Matrice[2][3]+Matrice[3][3]+Matrice[4][3]
print('Suma la coloana a 4=' , c4)
c5=Matrice[0][4]+Matrice[1][4]+Matrice[2][4]+Matrice[3][4]+Matrice[4][4]
print('Suma la coloana a 5=' , c5 )
dp=Matrice[0][0]+Matrice[1][1]+Matrice[2][2]+Matrice[3][3]+Matrice[4][4]
print('Suma la diagonala principala =' , dp )
ds=Matrice[0][4]+Matrice[1][3]+Matrice[2][2]+Matrice[3][1]+Matrice[4][0]
print('Suma la diagonala principala =' , ds )