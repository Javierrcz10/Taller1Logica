#Librerias a utilizar
import PySimpleGUI as sg
from pyswip import Prolog

#Entrada: Lista de juegos
#Salida : Lista de juegos
#Función: Ordenar los juegos por categoria
def juntarPorCategoria(juegosEncontrados):
    listaJuegos = []
    #Se agrega a la lista los géneros encontrados
    for juego in juegosEncontrados:
        esta = False
        for lista in listaJuegos:
            if(juego["G"] in lista):
                esta = True
        if (not esta):
            listaJuegos.append([juego["G"]])
    #Se agrupan los juegos segun su categoria
    for juego in juegosEncontrados:
        for lista in listaJuegos:
            if(lista[0] == juego["G"]):
                lista.append([juego["N"],juego["S"]])
                break
    return listaJuegos

#Entrada: Lista de juegos
#Salida: Número entero
#Función: Identificar cual género es el que mas veces se repite dentro de la lista de entrada
def generoMasJuegos(listaJuegos):
    listaLargos= []
    #Guarda en la lista de largos la cantidad de juegos por género
    for genero in listaJuegos:
        listaLargos.append(len(genero)-1)
    #Obtiene el valor maximo de la lista
    cantidadMaxima = max(listaLargos)
    cantidadMaximos = listaLargos.count(cantidadMaxima)
    indiceMaximo = listaLargos.index(cantidadMaxima)
    if (cantidadMaximos > 1): #La busqueda es ambigua
        return -1
    return indiceMaximo #Retorna el género con mas juegos

#Entrada: Habilidad y duración seleccionados por el usuario
#Salida: Lista de juegos junto a un identificador
#Función: Realizar consulta a la base de conocimiento con los datos de entrada
def querySinDecada(habilidad,duracion):
    #Definir la query
    queryStr = f"juego(N,G,'{duracion}',S,D,'{habilidad}')"
    #Hacer consulta
    juegosEncontrados = list(prolog.query(queryStr))
    #Verificar respuesta
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    indiceGeneroMasJuegos = generoMasJuegos(listaJuegos)
    if(indiceGeneroMasJuegos == -1): #No se pudo determinar género
        return listaJuegos, 3
    return listaJuegos[indiceGeneroMasJuegos], 2 #Retorna lista de juegos y el género

#Entrada: Experiencia, década y duración seleccionados por el usuario
#Salida: Lista de juegos junto a un identificador
#Función: Realizar consulta a la base de conocimiento con los datos de entrada
def queryCompleta(habilidad, decada, duracion):
    queryStr = f"juego(N,G,'{duracion}',S,{decada},'{habilidad}')"
    listaJuegos = []
    juegosEncontrados = list(prolog.query(queryStr))
    if(len(juegosEncontrados) == 0):
        #QUITAR PARAMETRO
        return querySinDecada(habilidad,duracion)
    #Se agrega a la lista los géneros encontrados
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    #Se selecciona el género con mas juegos encontrados
    indiceGeneroMasJuegos = generoMasJuegos(listaJuegos)
    if (indiceGeneroMasJuegos == -1): #Existe géneros con más de un maximo
        return querySinDecada(habilidad,duracion)
    #Si existe un resultado concreto
    return listaJuegos[indiceGeneroMasJuegos], 1 #Retorna lista de juegos y el género

#Entrada: Experiencia, década, duración y extra seleccionados por el usuario
#Salida: Lista de juegos junto a un identificador
#Función: Realizar consulta a la base de conocimiento con los datos de entrada
def queryAdicional(habilidad,decada,duracion,extra):
    #Definir query
    queryStr = f"juego(N,G,'{duracion}',S,{decada},'{habilidad}'),adicional(G,'{extra}')"
    listaJuegos = []
    #Realizar consulta
    juegosEncontrados = list(prolog.query(queryStr))
    if(len(juegosEncontrados) == 0): # Si no encontro juegos 
        return queryCompleta(habilidad,decada,duracion)
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    return listaJuegos[0], 0 #Retornar lista de juegos con el género

#Entrada: datos ingresados por el usuario, lista de valores validos
#Salida: Booleano o un string
#Función: verificar que el usuario ingreso datos validos (True), en el caso contrario se retornan información con los datos faltantes
def verificarValores(datos,lista):
    faltantes = ""
    nombres = ["Década","Experiencia","Duración"]
    for i in range(3):
        if datos[i] not in lista[i]:
            faltantes = faltantes + " " + nombres[i]
    if faltantes == "":
        return True #Estan todos los argumentos necesarios
    else:
        return faltantes #Faltan argumentos de entrada

#Entrada: Lista de juegos
#Salida: Un string
#Función: Concatenar los nombres de los juegos en un solo string
def concatenarJuegos(listaDeJuegos):
    stringJuegos = ""
    i = 1
    cantJuegos = len(listaDeJuegos)
    while i < cantJuegos:
         stringJuegos = stringJuegos + listaDeJuegos[i][0] + " (" + listaDeJuegos[i][1] + ")" + "\n"
         i = i + 1
    return stringJuegos

#Entrada: Un string
#Salida: Un string
#Función: Cambiar todas las tildes dentro del string de entrada por letras sin tilde
def quitarTilde(palabra):
    reemplazos = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for tilde, sinTilde in reemplazos:
        palabra = palabra.replace(tilde, sinTilde)
    return palabra

#Se cargan la base de conocimiento
prolog = Prolog()
prolog.consult("baseDeConocimiento.pl")

#Definir opciones que puede ingresar el usuario
decadas = [90,2000,2010,2020]
duraciones = ['Larga','Media','Corta']
experiencias = ['Inexperto','Hábil','Experto']
extras = ['','2D','Precisión','Simulación','Competitivo','Exploración','Ingenio','Toma de decisiones','Reflejos']
listaEntradas = [decadas,experiencias,duraciones,extras]

#Contruir el contenido de la ventana principal
layoutPrincipal = [[sg.Text("(Obligatorio)  Década:"),sg.Stretch(), sg.Combo(values = decadas,  key= "Decada", size=(18,4),readonly=True) ],
                   [sg.Text("(Obligatorio)  Experiencia:"),sg.Stretch(),sg.Combo(values = experiencias, key = "Experiencia", size=(18,4),readonly=True)],
                   [sg.Text("(Obligatorio)  Duración:"),sg.Stretch(),sg.Combo(values = duraciones, key = "Duracion", size=(18,4),readonly=True)],
                   [sg.Text("Extra:"),sg.Stretch(),sg.Combo(values = extras, key = "Extra", readonly=True, size=(18,4))],
                   [sg.Stretch(),sg.OK(button_text="Buscar")],
                   [sg.Text("Respuesta:")],
                   [sg.Multiline(size=(50,9),key = "Resultado", disabled=True)]]

#Crear la ventana
window = sg.Window("Recomendador", layoutPrincipal).finalize()

#Ciclo while para registrar los eventos de la ventanas
loop = True
while loop:
    evento, valores = window.read()
    #Salir del ciclo cuando la ventana se cierre
    if evento == sg.WIN_CLOSED:
        break
    #Cuando presione el boton Buscar
    else:
        #Verificar si se ingresaron los datos de entrada obligatorios
        informacion = [valores["Decada"],valores["Experiencia"], valores["Duracion"],valores["Extra"]]
        verificacion = verificarValores(informacion,listaEntradas)
        #Si el ingreso de datos fue correcto se realizan consultas a la base de conocimiento
        if verificacion == True:
            informacion[1] = quitarTilde(informacion[1])
            #Se escoge el tipo de consulta dependiendo si el usuario ingreso o no un dato extra
            if informacion[3] == '':
                #Se buscan juegos sin el parámetro extra
                busqueda, identificador = queryCompleta(informacion[1], informacion[0], informacion[2])
                #Se escoge el tipo de mensaje que se retorne a usuario dependiendo de como se ejecutó la busqueda de juegos
                if identificador == 1:
                    generoRecomendado = "Los juegos del género " + busqueda[0] + " va a ser de su agrado.\n\n"
                if identificador == 2:
                    generoRecomendado = "No se pudo encontrar juegos con los datos seleccionados.\n"
                    generoRecomendado = generoRecomendado + "Pero quitando el parámetro (Década) se obtiene que el género "
                    generoRecomendado = generoRecomendado + busqueda[0] + " representa su eleccion.\n\n"
                if identificador == 3:
                    generoRecomendado = "El recomendador no pudo determinar un género en especifico, aun quitando el parámetro (Década).\n"
                    generoRecomendado = generoRecomendado + "Pero se encontraron los siguientes juegos que va a ser de su disfrute.\n\n"
                stringJuegos = concatenarJuegos(busqueda)
                respuesta = generoRecomendado + stringJuegos
            else:
                #Se buscan juegos con el parámetro extra
                informacion[3] = quitarTilde(informacion[3])
                busqueda, identificador = queryAdicional(informacion[1], informacion[0], informacion[2], informacion[3])
                #Se escoge el tipo de mensaje que se retorne a usuario dependiendo de como se ejecutó la busqueda de juegos
                if identificador == 0:
                    generoRecomendado = "Los juegos del género " + busqueda[0] + " va a ser de su agrado.\n\n"
                if identificador == 1:
                    generoRecomendado = "No se pudo encontrar juegos con los datos seleccionados.\n"
                    generoRecomendado = generoRecomendado + "Pero quitando el parámetro (Extra) se obtiene que el género "
                    generoRecomendado = generoRecomendado + busqueda[0] + " es una buena eleccion.\n\n"
                if identificador == 2:
                    generoRecomendado = "No se pudo encontrar juegos con los datos seleccionados.\n"
                    generoRecomendado = generoRecomendado + "Pero quitando el parámetro (Extra) y (Década) se obtiene que el género "
                    generoRecomendado = generoRecomendado + busqueda[0] + " representa su eleccion.\n\n"
                if identificador == 3:
                    generoRecomendado = "El recomendador no pudo determinar un género en especifico, aún quitando los parámetros (Extra) y (Década).\n"
                    generoRecomendado = generoRecomendado + "Pero se encontraron los siguientes juegos que va a ser de su disfrute.\n\n"
                #Generar el mensaje con los juegos a recomendar para el usuario
                stringJuegos = concatenarJuegos(busqueda)
                respuesta = generoRecomendado + stringJuegos
            #Mostrar el resultado de la query al usuario por la interfaz
            window.find_element("Resultado").Update(respuesta)
        #Si faltaron datos por ingresar
        else:
            #Se identifican los datos que faltan y se da el aviso al usuario por pantalla
            error = "Faltó seleccionar:" + verificacion
            window.find_element("Resultado").Update(error)
#Fin del programa
