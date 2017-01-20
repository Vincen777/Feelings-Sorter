# Librerias de procesamiento de lenguaje natural
from textblob import TextBlob
from nltk.corpus import stopwords
import re, string
#Lectura de archivo de donde provienen los datos
archi = open("C:/Users/Casa/Desktop/datosAleatorios.txt","r")
lista = []
#Creacion de la cabecera del documento ARFF
lista.append("@relation tarea-feelings\n")
lista.append("\n")
lista.append("@attribute feelAdjetive {SuperPositive,Positive,None,SuperNegative,Negative}\n")
lista.append("@attribute existFeelVerb {yes,no}\n")
lista.append("@attribute feelVerbPositive {yes,no}\n")
lista.append("@attribute existNegation {yes,no}\n")
lista.append("@attribute existNever {yes,no}\n")
lista.append("@attribute feeling {Positive,Negative,Neutral}\n")
lista.append("\n")
lista.append("@data\n")
#Bucle para rrecorrer el archivo linea por linea
for linea in archi.readlines():
    linea=linea.split("|")
    mensaje = str(linea[0])
    #Creación de un objeto de procesamiento de texto de lenguaje natural
    wiki = TextBlob(mensaje)
    #identificar si la frase esta escrita de forma correcta y transformación de los datos
    data= wiki.correct().lower()
    #Transformacio del mensaje en una lista doble que contiene las partes de la oracion de cada palabra por ejemplo JJ Adjetivo
    tagsC= data.tags
    #tagsC
    #print(tagsC[1])
    #inicializacion de variables que van a almacenar los atributos
    existeVerbo="no"
    adjetivoPositivo="None"
    verboPositivo="no"
    existeno="no" 
    existenever="no"
    polarity=0
    polarityVerbo=0
    #Identificación si existe la palabra never en la frase
    if data.find("never") <> -1:
        existenever="yes"
    for i in range(0,len(tagsC)):
        #Identificación de una negación en la frase
        if tagsC[i][0] in ["not", "no", "n't"]:
            existeno="yes"
        #comprobación de la existencia o no de un adjetivo en la frase
        if tagsC[i][1] in [ "JJ", "JJR", "JJS"]:  
            texto1=TextBlob(tagsC[i][0])
            #verificación si el adjetivo expresa emociones
            if texto1.sentiment.polarity <> 0:
                #existeAdjetivo="yes"
                polarity += texto1.sentiment.polarity
        #comprobación de la existencia o no de un verbo en la frase
        if tagsC[i][1] in [ "VB", "VBP", "VBZ", "VBD", "VBN", "VBG"]: 
            texto1=TextBlob(tagsC[i][0])
            #verificación si el vervo expresa emociones
            if texto1.sentiment.polarity <> 0:
                existeVerbo="yes"
                polarityVerbo += texto1.sentiment.polarity
                #polarity
    #Discreitización del valor continuo de la polaridad acumulada de los adjetivos
    if polarity <> 0:
        if polarity < -0.5:
            adjetivoPositivo="SuperNegative"
        elif polarity < 0:
            adjetivoPositivo= "Negative"
        elif polarity <= 0.5 : 
            adjetivoPositivo= "Positive"
        else :
            adjetivoPositivo= "SuperPositive"
    if polarityVerbo > 0:
        verboPositivo="yes"
    lista.append( adjetivoPositivo + "," + existeVerbo + "," + verboPositivo +"," +existeno+"," + existenever +"," + str(linea[1])+"\n")

lista
len(lista)
archi.close()
#Escritura el archivo ARFF
archivo = open("C:/Users/Casa/Desktop/tarea-feelings-final.arff","wb")
final_de_archivo = archivo.tell()
archivo.writelines(lista)
archivo.seek(final_de_archivo)
archivo.close()

