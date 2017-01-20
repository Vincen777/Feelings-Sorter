#Libreria herramienta de lenguaje natural
from textblob import TextBlob
#Se habre el archivo de fraces recopiladas
archivo = open("C:\Users\Casa\Desktop\Frases.txt", "r") 
lista=[]
#Lazo que permite recorrer las lineas del archivo
for linea in archivo.readlines():
    datos= linea.rstrip('\n').split(' ', 1 )
    texto= datos[1]
    texto = TextBlob(texto)
    #Se verifican las lineas que no tienen polaridad es decir que no expresan sentimientos
    if texto.sentiment.polarity == 0:
        #Se carga en una lista las fraces neutras concatenadas con el texto |Neutral| 
        lista.append(str(texto) + " |Neutral| \n")

#Se grava la lista generada en un nuevo archivo llamado neutros.txt
archivo.close()
archi = open("C:/Users/Casa/Desktop/neutros.txt","wb")
final_de_archivo = archi.tell()
archi.writelines(lista)
archi.seek(final_de_archivo)
archi.close()