import random
# genero una lista con los valores del 0 al 250
a = range(0,251)
print(a)
#reordeno lista aleatoriamente para obtener los nuevos indices
random.shuffle(a)
print(a)
#abro el archivo que contiene los datos a ser ordenados
archi = open("C:/Users/Casa/Desktop/datos.txt","r")
#lista = range(1,251)
i = 0
for linea in archi.readlines():
    lista[a[i]] = linea
    i = i + 1

archi.close()

#gusdo la lista con los datos ordenadas en un nuevo archivo datosAleatorios.txt
archivo = open("C:/Users/Casa/Desktop/datosAleatorios.txt","wb")

final_de_archivo = archivo.tell()
archivo.writelines(lista)
archivo.seek(final_de_archivo)
archivo.close()