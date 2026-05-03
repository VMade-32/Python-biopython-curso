import numpy as np

arreglo0=np.array([[1,2,3,4], [4,5,6,7], [8,9,10,11]])
arreglo1=np.array([[11,12,13,14], [15,16,17,18], [19,20,21,22]])

suma=arreglo0+arreglo1
multiplicacion=arreglo0*arreglo1

print(arreglo0)
column=arreglo0[1,1]
print(column)   
print(suma)
print(multiplicacion)

#operaciones con transpuesta

arreglot0=np.transpose(arreglo0)
print(arreglot0)

multiplicacion_t=np.dot(arreglo0, arreglot0)
print(multiplicacion_t)

adicion=arreglo0 + 2
print(adicion)

#extra

arreglo3=np.array([[10,20,30]])
arreglo4=np.array([[2,4,6]])

