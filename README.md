# Chat de Consultas Laborales

Este programa de Python es un chat de simulación para consultas laborales, donde se generan preguntas de manera aleatoria para diferentes tipos de consultas relacionadas con trabajadores y empresas.

## Funcionamiento

Al ejecutar el programa, se abrirá una ventana de chat con una serie de opciones para seleccionar el tipo de consulta:

1. **Estado de los Trabajadores Solicitados**
2. **Estado de Visados y Documentos**
3. **Detalles de los Trabajadores Asignados**

Al presionar el botón "Enviar", se generará una pregunta aleatoria del tipo seleccionado y se mostrará en el chat. Cada consulta tendrá un color de letra aleatorio para facilitar la diferenciación de mensajes en la misma conversación.

## Archivos Principales

### `preguntas_trabajadores4.0.py`

Este archivo contiene el código principal del chat. Al ejecutarlo, se abrirá la interfaz gráfica donde se podrá interactuar con el chat y generar consultas aleatorias.

### `status_preguntas.py`

En este archivo se encuentran las preguntas disponibles para cada tipo de consulta. Las preguntas se eligen de manera aleatoria para simular la interacción del usuario.

### `listado_Clientes.py`

Aquí se encuentra un listado de clientes que son empresas importantes en los Estados Unidos. Este listado se utiliza para asignar un cliente aleatorio a cada consulta generada.

## Requisitos

- Python 3.x
- Bibliotecas Python: `tkinter`, `random`, `pyperclip`

## Ejecución

Para ejecutar el programa, puedes usar el siguiente comando:

```bash
