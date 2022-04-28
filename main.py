import PySimpleGUI as sg
from pyswip import Prolog


def queryFinal(habilidad,decada,duracion):
    queryStr = f"generos(M,'{habilidad}'),juegos(V,M,'{duracion}',Y,{decada})"
    print(queryStr)
    for i in prolog.query(queryStr):
        print(i)
def queryFinalExtra(habilidad,decada,duracion,extra):
    queryStr = f"generos(M,'{habilidad}'),juegos(V,M,'{duracion}',Y,{decada}),adicional(M,{extra})"
    print(queryStr)
    for i in prolog.query(queryStr):
        print(i)

def verificar():
    if opcionDecada.get() == 0 or opcionDuracion.get() == 0 or opcionExperiencia.get() == 0:
        
        return None
    
    habilidad = experiencias[opcionExperiencia.get()-1]
    decada = int(decadas[opcionDecada.get()-1])
    duracion = duraciones[opcionDuracion.get()-1]
    if opcionExtra.get() == 0:
        queryFinal(habilidad,decada,duracion)
    else:
        extra = extras[opcionExtra.get()-1]
        queryFinalExtra(habilidad,decada,duracion,extra)




prolog = Prolog()
prolog.consult("baseDeConocimiento.pl")



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
