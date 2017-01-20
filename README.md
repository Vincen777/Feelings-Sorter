# Feelings-Sorter

#Procedimiento para la creación de modelo.

##Selección de datos de entrenamiento y test.
Se utilizo un corpus propio de la librería nltk llamado sentence_polarity en el cual se proporciona una listado de frases positivas y frases negativas, para los datos neutros se procedió a recopilar datos de textos y separarlos en oraciones y posterior a esto se los clasifico con el clasificador de textblob ( el cofigo de la extración de fraces neutras del docuemto: clasificadortextblob.py).
Después de este proceso se recopilo una porción de datos de cada documento, se creo un documento final con 250 datos, 20% positivos, 20% Negativos y 60% Neutros.
Finalmente se procedió a mesclar los datos ya que se contaba originalmente primero datos positivos, luego negativos y finalmente neutros por medio del script  aleatorios.py.   

##Selección de atributos 

En primera instancia se escogieron 4  atributos el primero que era la existencia de adjetivo que indique una emoción, un segundo atributo que indique si la emoción del adjetivo  es positiva o es negativa, un tercer atributo que indique la existencia de una negación y un cuarto atributo que indice si existe la palabra never en la frace analizada.

Una vez realizado el modelo  se observo que estaba un poco sobre ajustado y que la precisión en en lo que tiene que ver con positivos y negativos era todavía baja, para solucionar esto se procedió a analizar posibles nuevos atributos que puedan expresar un sentimiento y se llego a la conclusión después de leer  algunos documentos y se procedió a agregar el atributo de la subjetividad  y una vez implementado el modelo se observo que en lugar de producir mejores resultados, el modelo bajaba su rendimiento, así que se procedió a analizar los textos y se observo que el verbo también tiene una gran influencia para la determinación de los sentimientos de una frase así que se agregaron 2 atributos al modelo uno que indique la presencia de un archivo que exprese emoción y  un segundo que indique  si el verbo es positivo o negativo, y al implementar esto se evidencio que estos atributos si contribuían a un mejor desempeño del modelo.

También se analizo que en algunas frases se tenia dos o más verbos adjetivos a la vez  así que se se cambiaron los atributos a la indicación de si existía por lo menos un verbo que exprese emoción y cual es la polaridad positiva o negativa del conjunto de verbos y lo mismo para los adjetivos.

 Finalmente se analizo que los 2 atributos nominales del adjetivo se pueden combinar en uno nominal que brinde más información, y con esto mejorar nuestra precisión, a partir de esto quedaron definidos los siguientes atributos.

Un atributo ordinal feelAdjetive con los valores SuperNegative, Negative, None, Positive y SuperPositive que indica la emoción que nos brinda el conjunto de adjetivos.
Un atributo nominal  con valores yes, no llamado existFeelVerb que indica la existencia por lo menos un verbo que indique emoción.
Un atributo nominal con valores yes, no llamado feelVerbPositive que indica si el verbo tiene una emoción positiva
Un atributo nominal con valores yes, no llamado existNegation que indica si existe una negación en la frase.
Un atributo nominal con valores yes, no llamado existNever que indica si existe la palabra never en la frase. 
La clase llamada  feeling que puede tener los valores Positive, Negative, Neutral

El código para obtener el archivo ARFF se encuentra en transformacionAtributos.py

#Discusión de Pruebas
En las pruebas se observo que el modelo de árbol de decisiones brindaba mejores resultados a partir que se transformo de nominal a ordinal el atributo referente al objetivo y que además se denota claramente que la mayoría de aciertos se presentan para las clases neutras, lo que hace pensar que las clases neutras se están ajustando a un único conjunto de valores de los atributos, lo que daría a pensar que si se tiene un cierto grado de sobre ajuste dado que en la matriz de confusión se ve que se evidencian valores de falsos positivos y falsos negativos mas considerables para los valores positivos y negativos. 

El método de validación cruzada da la impresión que  menor incertidumbre y da mayor confianza en los resultados, también se opto por reducir la cantidad  de valores neutros a un 40% del total para llegar a una apreciación de exactitud un poco más real que esta alrededor del 70% 

#Conclusiones
+ A partir de los resultados se pudo comprobar que para nuestro modelo se ajusta de mejor manera el modelo probabilista de  árbol de decisiones y la forma de testeo por validación cruzada.  
+ La mejor forma de obtener el mejor modelo probabilista y la mejor forma de prueba es de forma experimental, además a partir de los resultados podemos sacar información para optimizar nuestro modelo. 
+ La clasificación de sentimientos es un campo muy desarrollado en los últimos años lo que ha permitido que se creen librerias como texyBlob que facilitan los procesos de manera sustancial, pero lo malo es que el desarrollo esta centrado en textos en ingles por lo que el tratamiento de textos en español es todavía muy complicado.

# Instrucciones de Instalación 
1.- Descargar el archivo datosAleatorios.txt de la carpeta DatosFS

2.-Descargar transformacionAtributos.py

3.-Cambiar la ruta del archivo datos datosAleatorios.txt en el archivo transformacionAtributos.py en la linea archi = open("C:/Users/Casa/Desktop/datosAleatorios.txt","r")

4.-Cambiar la ruta donde queremos que se guarde el archivo ARFF generado en  transformacionAtributos.py en la linea archivo = open("C:/Users/Casa/Desktop/tarea-feelings-final.arff","wb")

5.-Ejecutar  transformacionAtributos.py (Es necesario tener Python)

6.-Ejecutamos weca para probar los datos.
