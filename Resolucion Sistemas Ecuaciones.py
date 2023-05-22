# -*- coding: utf-8 -*-
"""
Fecha: 22/05/2023
Autor: cheng
Contacto: bigdata.cheng@gmail.com

Objetivo: resolver sistemas de ecuaciones determinados
"""

import numpy as np


# Definimos las matrices A y B de la ecuacion matricial AX = B
A = np.array([[1,2,-3,-1], 
              [0,-3,2,6], 
              [-3,-1,3,1],
              [2,3,2,-1] ],float)

B = np.array([-2.5,7,2.5,-10.5],float) #terminos independientes
B = B.reshape(-1,1) # lo convierto en vector columna


AB = np.hstack((A,B)) # creo la matriz ampliada

m,n = AB.shape

print('-'*25)
print('\nLa matriz problema es:')
print(AB)


for j in np.arange(start=0, stop=m-1, step=1): 
    
    maxvalue = AB[j][j]
    maxindex =[j,j]
    
    
    
    
    for i in np.arange(start=j+1, stop=m, step=1): 
        
        if abs(AB[i][j])>abs(maxvalue):
            
            maxvalue=AB[i][j]
            maxindex=[i,j] #guardo los indices del maximo valor para luego intercambiar

    # print(maxindex)    
    # print(maxvalue)
   
    if maxindex[0] != j : 
        
        #hago el pivoteo del modo a,b = b,a  término a término usando un bucle 
        
        for k in range(len(AB[j])):
            
            AB[j,k], AB[maxindex[0],k] = AB[maxindex[0],k] , AB[j,k] 
        
        """
        Si hago Ab[j], Ab[maxindex[0]] = Ab[maxindex[0]] , Ab[j]  directamente el pivoteo cambiando 
        filas completas da error, por eso se utiliza el bucle para ir término a término
        
        
        Otra manera sería utilizar una matriz auxiliar para el pivoteo:
        c = np.copy(Ab) 
        Ab[j] = c[maxindex[0]] 
        Ab[maxindex[0]] = c[j]
        
        """
        
 
        
        print('\nTras el intercambio de la fila %d con la %d:' %(maxindex[0]+1,j+1))
        print(AB)
        
    else:
        
        print('\nNo hacemos intercambio')
            
    # print('Maximo valor de la columna %d es %.f' %(j,maxvalue))
    

    

    #tras hacer el intercambio procedo a la eliminacion por Gauss:-----------------
        
    for k in np.arange(start=j+1, stop=n-1, step=1): 
        
        
        aux = AB[j]*AB[k][j] / AB[j][j]
        AB[k]= AB[k] - aux
        
        
    np.set_printoptions(precision=4) #en el output se muestran hasta cuatro decimales si el numero es periodico 
    print('\n-----Eliminación de Gauss por pivote a(%d,%d)-----' %(j+1,j+1)) 
    print(AB)
    print('-'*25)
    


# Obtengo finalmente la matriz equivalente en forma triangular superior
print('\nMatriz triangular superior Ab:')
print(AB) 
    
    
    
    
#----------------------------SOLUCION POR SUSTITUCION REGRESIVA:

x = [0]*m #creo un vector donde guardo las soluciones del sistema

        
for i in np.arange(start=m-1, stop=-1, step=-1): 
    aux = 0 
    
    for j in np.arange(start=m-1, stop=-1, step=-1):
        aux += x[j]*AB[i,j] 
         
    x[i] = AB[i][n-1] - aux
    x[i] = x[i]/AB[i][i]


#------------------------PRESENTACION/PRINT DE LA SOLUCION:
    
print('-'*25)
print('\nSolución por sustitución regresiva: ')
for i in range(m):
    print('x(%d) = %0.2f' % (i+1,x[i]) )