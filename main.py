import PySimpleGUI as sg
from pyswip import Prolog


def juntarPorCategoria(juegosEncontrados):
    listaJuegos = []
    if(len(juegosEncontrados) == 0):
        print("No encontre juego")
        #QUITAR PARAMETRO
        return 
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

def querySinDuracion(habilidad,decada):
    queryStr = f"juegos(N,G,D,S,{decada},'{habilidad}')"
    juegosEncontrados = list(prolog.query(queryStr))
    print("CASO SIN DURACION")
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    print(listaJuegos)


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
    print("Caso sin decada")
    queryStr = f"juegos(N,G,'{duracion}',S,D,'{habilidad}')"
    juegosEncontrados = list(prolog.query(queryStr))
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    indiceGeneroMasJuegos = generoMasJuegos(listaJuegos)
    if(indiceGeneroMasJuegos == -1):
        print("Varios maximos")
        return listaJuegos
    return listaJuegos[indiceGeneroMasJuegos]

def queryCompleta(habilidad, decada, duracion):
    queryStr = f"juegos(N,G,'{duracion}',S,{decada},'{habilidad}')"
    listaJuegos = []
    juegosEncontrados = list(prolog.query(queryStr))
    if(len(juegosEncontrados) == 0):
        print("No encontre juego")
        #QUITAR PARAMETRO
        return querySinDecada(habilidad,duracion)
    #Se agrega a la lista los generos encontrados
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    #Se selecciona el genero con mas juegos encontrados
    indiceGeneroMasJuegos = generoMasJuegos(listaJuegos)
    if (indiceGeneroMasJuegos == -1): #Existe generos con más de un maximo
        return querySinDecada(habilidad,duracion)
    #Si existe un resultado concreto
    return listaJuegos[indiceGeneroMasJuegos]

def queryAdicional(habilidad,decada,duracion,extra):
    queryStr = f"juegos(N,G,'{duracion}',S,{decada},'{habilidad}'),adicional(G,'{extra}')"
    listaJuegos = []
    juegosEncontrados = list(prolog.query(queryStr))
    if(len(juegosEncontrados) == 0): # Si no encontro juegos 
        print("No se encontro con parametro adicional")
        return queryCompleta(habilidad,decada,duracion)
    listaJuegos = juntarPorCategoria(juegosEncontrados)
    return listaJuegos 

def verificar():
    if opcionDecada.get() == 0 or opcionDuracion.get() == 0 or opcionExperiencia.get() == 0:
        
        return None
    
    habilidad = experiencias[opcionExperiencia.get()-1]
    decada = int(decadas[opcionDecada.get()-1])
    duracion = duraciones[opcionDuracion.get()-1]
    if opcionExtra.get() == 0:
        queryCompleta(habilidad,decada,duracion)
    else:
        extra = extras[opcionExtra.get()-1]
        queryAdicional(habilidad,decada,duracion,extra)

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


prolog = Prolog()
prolog.consult("baseDeConocimiento.pl")
#queryCompleta('Experto',2020,'Larga')
testAdicional()
#queryAdicional('Habil',90,'Corta','3D')
#querySinDecada("Experto", "Corta")


decadas = ['90','2000','2010','2020']
duraciones = ['Larga','Media','Corta']
experiencias = ['Inexperto','Habil','Experto']
extras = ['2D','Precisión','Simulación','Competitivo','Exploración','Ingenio','Toma de decisiones','Reflejos']

#Contruir el contenido de la ventana principal
layoutPrincipal = [[sg.Text("(Obligatorio)  Década:"),sg.Stretch(), sg.Combo(values = decadas,  key= "Decada", size=(18,4),readonly=True) ],
                   [sg.Text("(Obligatorio)  Experiencia:"),sg.Stretch(),sg.Combo(values = experiencias, key = "Experiencia", size=(18,4),readonly=True)],
                   [sg.Text("(Obligatorio)  Duración:"),sg.Stretch(),sg.Combo(values = duraciones, key = "Duracion", size=(18,4),readonly=True)],
                   [sg.Text("Extra:"),sg.Stretch(),sg.Combo(values = extras, key = "Extra", readonly=True, size=(18,4))],
                   [sg.Stretch(),sg.OK(button_text="Buscar")],
                   [sg.Text("Respuesta:")],
                   [sg.Output(key = "Resultado")]]


#Crear la ventana
window = sg.Window("Recomendador", layoutPrincipal,resizable=True)

#Ciclo while para registrar los eventos de la ventanas
loop = True
while loop:
    evento, valores = window.read()
    print(evento)
    #Salir del ciclo cuando la ventana se cierre
    if evento == sg.WIN_CLOSED:
        break
    else:
        #print(valores)
        informacion = [valores["Decada"],valores["Experiencia"], valores["Duracion"],valores["Extra"]]
        #print(informacion)
        #if verificarValores() == True:
            #buscar valores
    
    #window.find_element("Resultado").Update("")
    #Limpiar valores de entrada
    listaKeys = list(window.ReturnValuesDictionary.keys())
    for key in listaKeys:
        try:window.find_element(key).Update("")
        except:pass
window.close()

#Completar al 100%
