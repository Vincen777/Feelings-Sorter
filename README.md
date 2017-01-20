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

#Conclusiones

# Instrucciones de Instalación 
1.- Descargar el archivo datosAleatorios.txt de la carpeta DatosFS
2.-Descargar transformacionAtributos.py
3.-Cambiar la ruta del archivo datos datosAleatorios.txt en el archivo transformacionAtributos.py
4.-Cambiar la ruta donde queremos que se guarde el archivo ARFF generado en  transformacionAtributos.py
5.-Ejecutar  transformacionAtributos.py (Es necesario tener Python)
6.-Ejecutamos weca para probar los datos.
