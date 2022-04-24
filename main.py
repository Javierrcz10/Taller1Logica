from tkinter import messagebox
from pyswip import Prolog
import tkinter as tk

def queryFinal(habilidad,decada,duracion):
    queryStr = f"generos(M,'{habilidad}'),juegos(V,M,'{duracion}',Y,{decada})"
    #queryStr = f"generos(M,'{habilidad}')"
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
        messagebox.showinfo(message="Debes marcar todas", title="Error al buscar")
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

ventana = tk.Tk()
ventana.geometry("400x300")

opcionExtra = tk.IntVar()
opcionDecada = tk.IntVar()
opcionDuracion = tk.IntVar()
opcionExperiencia = tk.IntVar()

checkboxesDecada = []
decadas = ['90','2000','2010','2020']
for i in range(4):
    checkboxesDecada.append(tk.Checkbutton(ventana, text = decadas[i],onvalue=i + 1, variable=opcionDecada))  
    checkboxesDecada[i].grid(row = i, column = 1, padx=15) 

checkboxesDuracion = []
duraciones = ['Larga','Media','Corta']
for j in range (3):
    checkboxesDuracion.append(tk.Checkbutton(ventana, text = duraciones[j],onvalue=j + 1, variable=opcionDuracion))  
    checkboxesDuracion[j].grid(row = j, column = 2,padx=15)

checkboxesExperiencia = []
experiencias = ['Inexperto','Habil','Experto']
for k in range(3):
    checkboxesExperiencia.append(tk.Checkbutton(ventana, text = experiencias[k],onvalue=k + 1, variable=opcionExperiencia))  
    checkboxesExperiencia[k].grid(row = k, column = 3,padx=15)

extras = []
btn = tk.Button(text="buscar",command= lambda: verificar())
btn.grid(row = 6, column = 3)
ventana.mainloop()

#Completar al 100%
