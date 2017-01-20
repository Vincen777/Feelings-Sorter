from textblob import TextBlob
from nltk.corpus import stopwords
import re, string
archi = open("C:/Users/Casa/Desktop/datosAleatorios.txt","r")
lista = []
lista.append("@relation tarea-feelings-subjetivity\n")
lista.append("\n")
lista.append("@attribute existFeelAdjetive {yes,no}\n")
lista.append("@attribute feelAdjetivePositive {yes,no}\n")
lista.append("@attribute existNegation {yes,no}\n")
lista.append("@attribute existNever {yes,no}\n")
lista.append("@attribute isSubjetive {low,middle,high,extreme}\n")
lista.append("@attribute feeling {Positive,Negative,Neutral}\n")
lista.append("\n")
lista.append("@data\n")
for linea in archi.readlines():
    linea=linea.split("|")
    mensaje = str(linea[0])
    isSubjetive="low"
    #mensaje = re.sub('[%s]' % re.escape(string.punctuation), ' ', mensaje)
    #mensaje
    wiki = TextBlob(mensaje)
    #identificar si la frase esta correcta
    data= wiki.correct().lower()
    if data.sentiment.subjectivity<0.25:
        isSubjetive="low"
    elif data.sentiment.subjectivity<0.5:
        isSubjetive="middle"
    elif data.sentiment.subjectivity<0.75:
        isSubjetive="high"
    else:
        isSubjetive="extreme"
        
        
    tagsC= data.tags
    #tagsC
    #print(tagsC[1])
    existeAdjetivo="no"
    adjetivoPositivo="no"
    existeno="no" 
    existenever="no"
    polarity=0    
    if data.find("never") <> -1:
        existenever="yes"
    for i in range(0,len(tagsC)):
        if tagsC[i][0] in ["not", "no", "n't"]:
            existeno="yes"
        if tagsC[i][1] == "JJ":
            texto1=TextBlob(tagsC[i][0])
            if texto1.sentiment.polarity <> 0:
                existeAdjetivo="yes"
                polarity += texto1.sentiment.polarity
                #polarity
    if polarity > 0:
        adjetivoPositivo="yes"
    lista.append(existeAdjetivo + "," + adjetivoPositivo + "," + existeno+"," + existenever +"," + isSubjetive + "," + str(linea[1])+"\n")

lista
len(lista)

archi.close()
archivo = open("C:/Users/Casa/Desktop/tarea-feelings-subjetivity.arff","wb")
final_de_archivo = archivo.tell()
archivo.writelines(lista)
archivo.seek(final_de_archivo)
archivo.close()

