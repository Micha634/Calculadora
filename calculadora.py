from tkinter import *
from tkinter import ttk
import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Crear la ventana principal
root = Tk()
root.title("CalcMaster")
root.geometry("500x700+500+100")

# Crear la barra de menús
menu_bar = Menu(root)

def open_calculate():
    print("Calcular seleccionado")

def open_Limite():
    graph_window = Toplevel(root)
    graph_window.title("Saca el límite")
    graph_window.geometry("400x300")
    
    label = Label(graph_window, text="Ingrese la expresión (Ejemplo: 3*x**2 + 2)")
    label.pack(pady=10)

    func_entry = Entry(graph_window, font=("Arial", 14))
    func_entry.pack(pady=10, padx=10, fill=X)
    
    limit_entry = Entry(graph_window, font=("Arial", 14))
    limit_entry.pack(pady=10, padx=10, fill=X)
    limit_entry.insert(0, "0")  # Valor por defecto: 0

    def calcular_limite():
        try:
            func_str = func_entry.get()
            x_val = float(limit_entry.get())
            
            x = sp.symbols('x')
            
            expr = sp.sympify(func_str)
            
            limite = sp.limit(expr, x, x_val)
            
            result_label.config(text=f"Límite: {limite}")
        except Exception as e:
            result_label.config(text="Error en el cálculo")

    calc_button = Button(graph_window, text="Calcular Límite", command=calcular_limite)
    calc_button.pack(pady=10)

    result_label = Label(graph_window, text="", font=("Arial", 14))
    result_label.pack(pady=10)

def open_Derivada():
    deriv_window = Toplevel(root)
    deriv_window.title("Calcular Derivada")
    deriv_window.geometry("400x300")
    
    label = Label(deriv_window, text="Ingrese la expresión (Ejemplo: 3*x**2 * x**3)")
    label.pack(pady=10)

    func_entry = Entry(deriv_window, font=("Arial", 14))
    func_entry.pack(pady=10, padx=10, fill=X)
    
    point_entry = Entry(deriv_window, font=("Arial", 14))
    point_entry.pack(pady=10, padx=10, fill=X)
    point_entry.insert(0, "0")  # Valor por defecto: 0

    def calcular_derivada():
        try:
            func_str = func_entry.get()
            x_val = float(point_entry.get())
            x = sp.symbols('x')
          
            expr = sp.sympify(func_str)
            
            derivada = sp.diff(expr, x)
            
            resultado = derivada.subs(x, x_val)
            
            result_label.config(text=f"Derivada: {derivada}\nValor en x = {x_val}: {resultado}")
        except Exception as e:
            result_label.config(text="Error en el cálculo")

    calc_button = Button(deriv_window, text="Calcular Derivada", command=calcular_derivada)
    calc_button.pack(pady=10)

    result_label = Label(deriv_window, text="", font=("Arial", 14))
    result_label.pack(pady=10)

def graficar_funcion():
    # Crear la ventana para graficar la función
    graph_window = Toplevel(root)
    graph_window.title("Gráficar Función")
    graph_window.geometry("600x500")

    label_graph = Label(graph_window, text="Ingrese la función para graficar (Ejemplo: x**2 + 3*x + 2)")
    label_graph.pack(pady=10)

    func_graph_entry = Entry(graph_window, font=("Arial", 14))
    func_graph_entry.pack(pady=10, padx=10, fill=X)

    # Función que grafica la función ingresada
    def graficar():
        func_str = func_graph_entry.get()
        try:
            # Definir la variable simbólica x
            x = sp.symbols('x')

            # Convertir la expresión de texto a una expresión de SymPy
            expr = sp.sympify(func_str)

            # Crear un rango de valores para x (desde -10 hasta 10)
            x_vals = np.linspace(-10, 10, 400)

            # Evaluar la función para cada valor de x
            y_vals = np.array([float(expr.subs(x, val)) for val in x_vals])

            # Crear el gráfico
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(x_vals, y_vals, label=f'Función: {func_str}')
            ax.set_xlabel('x')
            ax.set_ylabel('f(x)')
            ax.set_title(f'Gráfico de la función')
            ax.grid(True)
            ax.legend()

            # Insertar el gráfico en la interfaz de Tkinter
            canvas = FigureCanvasTkAgg(fig, master=graph_window)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except Exception as e:
            error_label.config(text="Error en la graficación")

    # Botón para graficar
    graph_button = Button(graph_window, text="Graficar", command=graficar)
    graph_button.pack(pady=10)

    error_label = Label(graph_window, text="", font=("Arial", 14))
    error_label.pack(pady=10)

# Crear el menú "Archivo"
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Calcular", command=open_calculate)
file_menu.add_command(label="Grafica", command=graficar_funcion)
file_menu.add_command(label="Limite", command=open_Limite)
file_menu.add_command(label="Derivada", command=open_Derivada)  # Nueva opción para Derivadas
file_menu.add_separator()  # Separador
file_menu.add_command(label="Salir", command=root.quit)

# Añadir el menú "Archivo" a la barra de menús
menu_bar.add_cascade(label="Menú", menu=file_menu)

# Configurar la barra de menús en la ventana
root.config(menu=menu_bar)

# Estilo de la interfaz
estilos = ttk.Style()
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

# Configurar filas y columnas para que se expandan
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Estilos de los Labels
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', anchor="e", font=("Arial", 20))

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', anchor="e", font=("Arial", 20))

entrada1 = StringVar()
Label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
Label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E, N, S), ipadx=10, ipady=20)

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, E, N, S), ipadx=10, ipady=20)

# Funciones para los botones de la calculadora
def ingresarvalor(tecla):
    """Función para ingresar valores en la pantalla"""
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
    elif tecla in ('+', '-', '*', '/','(', ')'):
        if entrada2.get():  # Solo si hay algo en la pantalla
            entrada2.set(entrada2.get() + tecla)
    elif tecla == '=':
        try:
            entrada1.set(entrada1.get() + entrada2.get())
            resultado = eval(entrada1.get())  # Evaluar la operación
            entrada2.set(resultado)
        except Exception as e:
            entrada2.set("Error" + str(e))  # Mostrar error si algo sale mal

def raizcuadrada():
    """Función para calcular la raíz cuadrada"""
    try:
        entrada1.set('')
        resultado = math.sqrt(float(entrada2.get()))
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")

def borrar():
    """Función para borrar el último caracter"""
    entrada2.set(entrada2.get()[:-1])

def borrartodo():
    """Función para borrar toda la entrada"""
    entrada1.set('')
    entrada2.set('')

# Estilos de los botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font=("Arial", 14))

# Botones de la calculadora
button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton", command=lambda: ingresarvalor('0'))
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton", command=lambda: ingresarvalor('1'))
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton", command=lambda: ingresarvalor('2'))
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton", command=lambda: ingresarvalor('3'))
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton", command=lambda: ingresarvalor('4'))
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton", command=lambda: ingresarvalor('5'))
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton", command=lambda: ingresarvalor('6'))
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton", command=lambda: ingresarvalor('7'))
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton", command=lambda: ingresarvalor('8'))
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton", command=lambda: ingresarvalor('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_numeros.TButton", command=lambda: borrar())
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_numeros.TButton", command=lambda: borrartodo())
button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_numeros.TButton", command=lambda: ingresarvalor('('))
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_numeros.TButton", command=lambda: ingresarvalor(')'))
button_punto = ttk.Button(mainframe, text=".", style="Botones_numeros.TButton", command=lambda: ingresarvalor('.'))

button_division = ttk.Button(mainframe, text=chr(247), style="Botones_numeros.TButton", command=lambda: ingresarvalor('/'))
button_multiplicacion = ttk.Button(mainframe, text="x", style="Botones_numeros.TButton", command=lambda: ingresarvalor('*'))
button_resta = ttk.Button(mainframe, text="-", style="Botones_numeros.TButton", command=lambda: ingresarvalor('-'))
button_suma = ttk.Button(mainframe, text="+", style="Botones_numeros.TButton", command=lambda: ingresarvalor('+'))

button_igual = ttk.Button(mainframe, text="=", style="Botones_numeros.TButton", command=lambda: ingresarvalor('='))

# Distribución de los botones en la ventana
button_parentesis1.grid(column=0, row=2, sticky="nsew")
button_parentesis2.grid(column=1, row=2, sticky="nsew")
button_borrar_todo.grid(column=2, row=2, sticky="nsew")
button_borrar.grid(column=3, row=2, sticky="nsew")

button7.grid(column=0, row=3, sticky="nsew")
button8.grid(column=1, row=3, sticky="nsew")
button9.grid(column=2, row=3, sticky="nsew")
button_division.grid(column=3, row=3, sticky="nsew")

button4.grid(column=0, row=4, sticky="nsew")
button5.grid(column=1, row=4, sticky="nsew")
button6.grid(column=2, row=4, sticky="nsew")
button_multiplicacion.grid(column=3, row=4, sticky="nsew")

button1.grid(column=0, row=5, sticky="nsew")
button2.grid(column=1, row=5, sticky="nsew")
button3.grid(column=2, row=5, sticky="nsew")
button_suma.grid(column=3, row=5, sticky="nsew")

button0.grid(column=0, row=6, columnspan=2, sticky="nsew")
button_punto.grid(column=2, row=6, sticky="nsew")
button_resta.grid(column=3, row=6, sticky="nsew")

button_igual.grid(column=0, row=7, columnspan=3, sticky="nsew")

# Configurar las filas y columnas para que se expandan
for r in range(8):
    mainframe.grid_rowconfigure(r, weight=1)

for c in range(4):
    mainframe.grid_columnconfigure(c, weight=1)

# Ejecutar el mainloop
root.mainloop()
