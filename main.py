import PySimpleGUI as sg
from pyswip import Prolog


def juntarPorCategoria(juegosEncontrados):
    listaJuegos = []
    #Se agrega a la lista los generos encontrados
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


def generoMasJuegos(listaJuegos):
    listaLargos= []
    #Guarda en la lista de largos la cantidad de juegos por genero
    for genero in listaJuegos:
        listaLargos.append(len(genero)-1)
    cantidadMaxima = max(listaLargos)
    cantidadMaximos = listaLargos.count(cantidadMaxima)
    indiceMaximo = listaLargos.index(cantidadMaxima)
    if (cantidadMaximos > 1): #La busqueda es ambigua
        return -1
    return indiceMaximo #Retorna el genero con mas juegos

def querySinDecada(habilidad,duracion):
    queryStr = f"juegos(N,G,'{duracion}',S,D,'{habilidad}')"
    juegosEncontrados = list(prolog.query(queryStr))
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    indiceGeneroMasJuegos = generoMasJuegos(listaJuegos)
    if(indiceGeneroMasJuegos == -1):
        return listaJuegos, 3
    return listaJuegos[indiceGeneroMasJuegos], 2

def queryCompleta(habilidad, decada, duracion):
    queryStr = f"juegos(N,G,'{duracion}',S,{decada},'{habilidad}')"
    listaJuegos = []
    juegosEncontrados = list(prolog.query(queryStr))
    if(len(juegosEncontrados) == 0):
        #QUITAR PARAMETRO
        return querySinDecada(habilidad,duracion)
    #Se agrega a la lista los generos encontrados
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    #Se selecciona el genero con mas juegos encontrados
    indiceGeneroMasJuegos = generoMasJuegos(listaJuegos)
    if (indiceGeneroMasJuegos == -1): #Existe generos con más de un maximo
        return querySinDecada(habilidad,duracion)
    #Si existe un resultado concreto
    return listaJuegos[indiceGeneroMasJuegos], 1

def queryAdicional(habilidad,decada,duracion,extra):
    queryStr = f"juegos(N,G,'{duracion}',S,{decada},'{habilidad}'),adicional(G,'{extra}')"
    listaJuegos = []
    juegosEncontrados = list(prolog.query(queryStr))
    if(len(juegosEncontrados) == 0): # Si no encontro juegos 
        return queryCompleta(habilidad,decada,duracion)
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    return listaJuegos, 0

#Esta función se debe borrar antes de entregar
def test():
    habilidades =["Inexperto","Habil","Experto"]
    decadas = [90,2000,2010,2020]
    duraciones = ["Corta","Media","Larga"]
    for habilidad in habilidades:
        for decada in decadas:
            for duracion in duraciones:
                print("####", habilidad, ", ",decada, ", ",duracion)
                print(queryCompleta(habilidad,decada,duracion))
                print("\n")

#Esta función se debe borrar antes de entregar
def testAdicional():
    habilidades =["Inexperto","Habil","Experto"]
    decadas = [90,2000,2010,2020]
    duraciones = ["Corta","Media","Larga"]
    adicionales = ["2D", "Precisión", "Simulación", "Competitivo", "Exploración","Ingenio", "Toma de decisiones", "Reflejos"]
    for habilidad in habilidades:
        for decada in decadas:
            for duracion in duraciones:
                for adicional in adicionales:
                    print("####", habilidad, ", ",decada, ", ",duracion, ", ", adicional)
                    print(queryAdicional(habilidad,decada,duracion,adicional))
                    print("\n")

def verificarValores(datos,lista):
    faltantes = ""
    nombres = ["Década","Experiencia","Duración"]
    for i in range(3):
        print(i)
        if datos[i] not in lista[i]:
            faltantes = faltantes + " " + nombres[i]
    if faltantes == "":
        return True
    else:
        return faltantes

def concatenarJuegos(listaDeJuegos):
    stringJuegos = ""
    i = 1
    cantJuegos = len(listaDeJuegos)
    while i < cantJuegos:
         stringJuegos = stringJuegos + listaDeJuegos[i][0] + "(" + listaDeJuegos[i][1] + ")" + "\n"
         i = i + 1
    return stringJuegos

prolog = Prolog()
prolog.consult("baseDeConocimiento.pl")


decadas = [90,2000,2010,2020]
duraciones = ['Larga','Media','Corta']
experiencias = ['Inexperto','Habil','Experto']
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

#Hacer que el cuado Output solo sea de lectura

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
            #Se escoge el tipo de consulta dependiendo si el usuario ingreso o no un dato extra
            if informacion[3] == '':
                busqueda, identificador = queryCompleta(informacion[1], informacion[0], informacion[2])
                if identificador == 1:
                    generoRecomendado = "Los juegos del género " + busqueda[0] + " seran de su agrado.\n\n"
                if identificador == 2:
                    generoRecomendado = "No se pudo encontrar juegos con los datos seleccionados.\n"
                    generoRecomendado = generoRecomendado + "Pero quitando el parámetro (Década) se obtiene que el género "
                    generoRecomendado = generoRecomendado + busqueda[0] + " es una buena eleccion.\n\n"
                if identificador == 3:
                    generoRecomendado = "El recomendador no pudo determinar un género en especifico, aun quitando el parámetro (Década).\n"
                    generoRecomendado = generoRecomendado + "Pero se encontraron los siguientes juegos que pueden ser de su disfrute.\n\n"
                stringJuegos = concatenarJuegos(busqueda)
                respuesta = generoRecomendado + stringJuegos
            else:
                busqueda, identificador = queryAdicional(informacion[1], informacion[0], informacion[2], informacion[3])
                if identificador == 0:
                    generoRecomendado = "Los juegos del género " + busqueda[0] + " seran de su agrado.\n\n"
                if identificador == 1:
                    generoRecomendado = "No se pudo encontrar juegos con los datos seleccionados.\n"
                    generoRecomendado = generoRecomendado + "Pero quitando el parámetro (Extra) se obtiene que el género "
                    generoRecomendado = generoRecomendado + busqueda[0] + " es una buena eleccion.\n\n"
                if identificador == 2:
                    generoRecomendado = "No se pudo encontrar juegos con los datos seleccionados.\n"
                    generoRecomendado = generoRecomendado + "Pero quitando el parámetro (Extra) y (Década) se obtiene que el género "
                    generoRecomendado = generoRecomendado + busqueda[0] + " es una buena eleccion.\n\n"
                if identificador == 3:
                    generoRecomendado = "El recomendador no pudo determinar un género en especifico, aun quitando los parámetros (Extra) y (Década).\n"
                    generoRecomendado = generoRecomendado + "Pero se encontraron los siguientes juegos que pueden ser de su disfrute.\n\n"
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