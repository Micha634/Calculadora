from tkinter import*
from tkinter import ttk
import math

root= Tk()
root.title("Calculadora")
root.geometry("+500+800")


estilos =ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(root, style= "mainframe.TFrame")
mainframe.grid(column =0, row=0)


#estilos Labels
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', anchor="e")



entrada1 = StringVar()
Label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
Label_entrada1.grid(column =0, row=0, columnspan= 4, sticky=(W, E))


entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe,textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column =0, row=5, columnspan= 4, sticky=(W, E))

estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton')
estilos_botones_numeros.map('Botones_numeros. TButton',foreground =[{'active','red'}], backgroung =[{'active', 'black'}])

esilos_botones_borrar =ttk.Style()



button0 = ttk.Button(mainframe, text = "0", style="Botones_numeros.TButton")
button1 = ttk.Button(mainframe, text = "1", style="Botones_numeros.TButton")
button2 = ttk.Button(mainframe, text = "2", style="Botones_numeros.TButton")
button3 = ttk.Button(mainframe, text = "3", style="Botones_numeros.TButton")
button4 = ttk.Button(mainframe, text = "4", style="Botones_numeros.TButton")
button5 = ttk.Button(mainframe, text = "5", style="Botones_numeros.TButton")
button6 = ttk.Button(mainframe, text = "6", style="Botones_numeros.TButton")
button7 = ttk.Button(mainframe, text = "7", style="Botones_numeros.TButton")
button8 = ttk.Button(mainframe, text = "8", style="Botones_numeros.TButton")
button9 = ttk.Button(mainframe, text = "9", style="Botones_numeros.TButton")

button_borrar = ttk.Button(mainframe, text = chr(9003))
button_borrar_todo = ttk.Button(mainframe, text = "C")
button_parentesis1 = ttk.Button(mainframe, text = "(")
button_parentesis2 = ttk.Button(mainframe, text = ")")
button_punto = ttk.Button(mainframe, text = ".")


button_division = ttk.Button (mainframe, text=chr(247)) 
button_multiplicacion= ttk.Button(mainframe, text="x")
button_resta =ttk. Button (mainframe, text="-")
button_suma = ttk.Button (mainframe, text="+")


button_igual = ttk. Button (mainframe, text="=") 
button_raiz_cuadrada = ttk. Button (mainframe, text="√")

#Botones en pantalla



button_parentesis1.grid(column=0, row=2)
button_parentesis2.grid(column=1, row=2)
button_borrar_todo.grid(column=2, row=2)
button_borrar.grid(column=3, row=2)

button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)
button_division.grid(column=3, row=3)

button4.grid(column=0, row=4)
button5.grid(column=1, row=4)
button6.grid(column=2, row=4)
button_multiplicacion.grid(column=3, row=4)

button1.grid(column=0, row=5)
button2.grid(column=1, row=5)
button3.grid(column=2, row=5)
button_suma.grid(column=3, row=5)

button0.grid (column=0, row=6, columnspan=2, sticky=(W, E))
button_punto.grid(column=2, row=6)
button_resta.grid(column=3, row=6)

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, E)) 
button_raiz_cuadrada.grid(column=3, row=7)



root, mainloop()




