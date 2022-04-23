from pyswip import Prolog
import tkinter as tk
prolog = Prolog()
prolog.consult("baseDeConocimiento.pl")

ventana = tk.Tk()
ventana.geometry("800x600")


opcionDecada = tk.IntVar()
opcionDuracion = tk.IntVar()
opcionExperiencia = tk.IntVar()

checkboxesDecada = []
decadas = ['90','2000','2010','2020']
for i in range(4):
    checkboxesDecada.append(tk.Checkbutton(ventana, text = decadas[i],onvalue=i + 1, variable=opcionDecada))  
    checkboxesDecada[i].pack()

checkboxesDuracion = []
duraciones = ['Largo','Medio','Corto']
for j in range (3):
    checkboxesDuracion.append(tk.Checkbutton(ventana, text = duraciones[j],onvalue=j + 1, variable=opcionDuracion))  
    checkboxesDuracion[j].pack()

checkboxesExperiencia = []
experiencias = ['Inexperto','Habil','Experto']
for k in range(3):
    checkboxesExperiencia.append(tk.Checkbutton(ventana, text = experiencias[k],onvalue=k + 1, variable=opcionExperiencia))  
    checkboxesExperiencia[k].pack()



ventana.mainloop()
#list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
#for soln in prolog.query("juegos(V,'Plataforma',X,Y,Z)"):
#    print(soln["V"])

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
