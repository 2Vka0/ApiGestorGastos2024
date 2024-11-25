#Analisis de datos con panda (analisis descriptivo)
#1. Para analizar datos con pandas necesitamos instalar 
#e inportar la herramienta

import pandas as pd


#2. Se obtiene la fuente de datos
#Lista de datos 

datos=[  

    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22},
    {'Nombre':'Mc Gregor','Ciudad':'Medellin','Edad':18},
    {'Nombre':'Alonso Smith','Ciudad':'Hollywood','Edad':28},
    {'Nombre':'Paulo Londra','Ciudad':'Bogota','Edad':19},
    {'Nombre':'Gilbert Muñaño','Ciudad':'Barranquilla','Edad':33},
    {'Nombre':'Teresa Butouski','Ciudad':'Balle del cauca','Edad':22}
]

#3. Se capturan los datos:
#Pandas utiliza una tabla tabulada que se llama DataFrame

datosOrdenados=pd.DataFrame(datos)
#print(datosOrdenados)

#Utilizando el head()
#print(datosOrdenados.head(10))

#utlizando el tail()
#print (datosOrdenados.tail(50))

#utilizando el info()
#print (datosOrdenados.info())

#utilizando el describe
#print (datosOrdenados.describe())

#utilizando []
#Prediccion de la edad que tendras en 5 años
#print (datosOrdenados['Edad']+5)

#Eliminando registros
#datosOrdenados.drop(0)
#print(datosOrdenados)

#Agrupar por categoria
print(datosOrdenados.groupby('Ciudad').size())
