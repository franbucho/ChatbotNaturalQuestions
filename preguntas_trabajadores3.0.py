
import tkinter as tk
from tkinter import ttk
import random
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext
import pyperclip

# Colores para los mensajes de chat
COLORES_CHAT = ["#007bff", "#28a745", "#dc3545", "#ffc107", "#17a2b8", "#6610f2", "#fd7e14"]
ultimo_color_usado = None

# Función para generar una pregunta aleatoria según el tipo de consulta seleccionado
def generar_pregunta(tipo_consulta):
    # Cargamos las preguntas desde el archivo status_preguntas.py
    from status_preguntas import preguntas

    if tipo_consulta == "Estado de los Trabajadores Solicitados":
        return random.choice(preguntas["solicitados"])
    elif tipo_consulta == "Estado de Visados y Documentos":
        return random.choice(preguntas["visados"])
    elif tipo_consulta == "Detalles de los Trabajadores Asignados":
        return random.choice(preguntas["asignados"])
    else:
        return "No hay preguntas disponibles para este tipo de consulta."

# Función para enviar la pregunta y mostrarla en la ventana de chat
def enviar_pregunta():
    global ultimo_color_usado
    tipo_consulta = variable_tipo_consulta.get()
    pregunta = generar_pregunta(tipo_consulta)
    
    # Escoger un color diferente al último utilizado
    color_chat = random.choice([color for color in COLORES_CHAT if color != ultimo_color_usado])
    ultimo_color_usado = color_chat
    
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, f"Usuario: {pregunta}\n", ("usuario", color_chat))
    chat.config(state=tk.DISABLED)
    chat.see(tk.END)

# Función para limpiar el chat
def limpiar_chat():
    chat.config(state=tk.NORMAL)
    chat.delete('1.0', tk.END)
    chat.config(state=tk.DISABLED)

# Función para copiar el contenido del chat al portapapeles
def copiar_chat():
    contenido_chat = chat.get('1.0', tk.END)
    pyperclip.copy(contenido_chat)
    messagebox.showinfo("Chat de Consultas Laborales", "El contenido del chat ha sido copiado al portapapeles.")

# Crear la ventana principal
root = tk.Tk()
root.title("Chat de Consultas Laborales")

# Configurar el estilo del chat
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TButton", background="#007bff", foreground="black")
style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
style.configure("TEntry", background="white")

# Marco para el chat con scroll
chat_frame = ttk.Frame(root)
chat_frame.pack(padx=10, pady=10)

# Ventana de chat con scroll
chat = scrolledtext.ScrolledText(chat_frame, height=20, width=50, wrap=tk.WORD)
chat.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)
chat.config(state=tk.DISABLED)

# Sección de selección de tipo de consulta
tipo_consulta_frame = ttk.Frame(root)
tipo_consulta_frame.pack(pady=10)

label_tipo_consulta = ttk.Label(tipo_consulta_frame, text="Tipo de Consulta:")
label_tipo_consulta.pack(side=tk.LEFT, padx=5)

opciones_consulta = [
    "Estado de los Trabajadores Solicitados",
    "Estado de Visados y Documentos",
    "Detalles de los Trabajadores Asignados"
]

variable_tipo_consulta = tk.StringVar(root)
variable_tipo_consulta.set(opciones_consulta[0])

menu_consulta = ttk.Combobox(tipo_consulta_frame, textvariable=variable_tipo_consulta, values=opciones_consulta, width=40)
menu_consulta.pack(side=tk.LEFT, padx=5)

# Botón para enviar la pregunta
btn_enviar = ttk.Button(root, text="Generar Consulta", command=enviar_pregunta)
btn_enviar.pack(pady=10)

# Botón para limpiar el chat
btn_limpiar = ttk.Button(root, text="Limpiar Chat", command=limpiar_chat)
btn_limpiar.pack(pady=5)

# Botón para copiar el chat al portapapeles
btn_copiar = ttk.Button(root, text="Copiar Chat", command=copiar_chat)
btn_copiar.pack(pady=5)

# Definir estilos para el chat
for color in COLORES_CHAT:
    chat.tag_configure(color, foreground=color)

# Ejecutar la aplicación
root.mainloop()