# Feelings-Sorter

Procedimiento para la creación de modelo.
Selección de datos de entrenamiento y test.
Se utilizo un corpus propio de la librería nltk llamado sentence_polarity en el cual se proporciona una listado de frases positivas y frases negativas, para los datos neutros se procedió a recopilar datos de textos y separarlos en oraciones y posterior a esto se los clasifico con el clasificador de textblob ( el cofigo de la extración de fraces neutras del docuemto: clasificadortextblob.py).
Después de este proceso se recopilo una porción de datos de cada documento, se creo un documento final con 250 datos, 20% positivos, 20% Negativos y 60% Neutros.
