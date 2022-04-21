from pyswip import Prolog
prolog = Prolog()
prolog.consult("baseDeConocimiento.pl")
#list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
for soln in prolog.query("juegos(V,'Plataforma',X,Y,Z)"):
    print(soln["V"])

#juegos(nombre,genero,duracion,categoriaSpeed,decada)
#generos(genero,experiencia,adicional)

#Larga duracion
#Duracion media
#Corta duracion

#Inexperto en videojuegos
#Habil en videojuegos

#Decada de los 90
#Decada de los 2000
#Decada del 2010
#Decada del 2020

#Completar al 100%
