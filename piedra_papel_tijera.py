import tkinter as tk
from tkinter import messagebox
import random

# Variables globales
puntaje_jugador = 0
puntaje_computador = 0

def actualizar_puntaje():
    texto = f"Tú: {puntaje_jugador}   |   Computador: {puntaje_computador}"
    etiqueta_puntaje.config(text=texto)

def desactivar_botones():
    boton_piedra.config(state="disabled")
    boton_papel.config(state="disabled")
    boton_tijera.config(state="disabled")
    boton_reiniciar.pack(pady=10)  # Mostrar el botón de reinicio

def activar_botones():
    boton_piedra.config(state="normal")
    boton_papel.config(state="normal")
    boton_tijera.config(state="normal")
    boton_reiniciar.pack_forget()  # Ocultar el botón de reinicio

def reiniciar_juego():
    global puntaje_jugador, puntaje_computador
    puntaje_jugador = 0
    puntaje_computador = 0
    actualizar_puntaje()
    activar_botones()

def jugar(eleccion_jugador):
    global puntaje_jugador, puntaje_computador

    if puntaje_jugador == 3 or puntaje_computador == 3:
        return

    opciones = ["piedra", "papel", "tijera"]
    eleccion_computador = random.choice(opciones)

    if eleccion_jugador == eleccion_computador:
        resultado = "Empate 😐"
    elif (eleccion_jugador == "piedra" and eleccion_computador == "tijera") or \
         (eleccion_jugador == "papel" and eleccion_computador == "piedra") or \
         (eleccion_jugador == "tijera" and eleccion_computador == "papel"):
        resultado = "¡Ganaste esta ronda! 🎉"
        puntaje_jugador += 1
    else:
        resultado = "Perdiste esta ronda 😢"
        puntaje_computador += 1

    actualizar_puntaje()

    if puntaje_jugador == 3:
        messagebox.showinfo("🏆 Victoria", "¡Felicidades Francis, ganaste el juego! 🥳")
        desactivar_botones()
    elif puntaje_computador == 3:
        messagebox.showinfo("😢 Derrota", "El computador ganó esta vez. ¡Sigue practicando!")
        desactivar_botones()
    else:
        messagebox.showinfo("Resultado", f"Tú elegiste: {eleccion_jugador}\nComputador eligió: {eleccion_computador}\n\n{resultado}")

# Crear ventana
ventana = tk.Tk()
ventana.title("🎮 Piedra, Papel o Tijera")
ventana.geometry("350x380")
ventana.configure(bg="#1e1e2e")

# Título
tk.Label(ventana, text="🕹️ Elige una opción:", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2e").pack(pady=10)

# Puntaje
etiqueta_puntaje = tk.Label(ventana, text="Tú: 0   |   Computador: 0", font=("Arial", 12), fg="yellow", bg="#1e1e2e")
etiqueta_puntaje.pack(pady=5)

# Botones de juego
boton_piedra = tk.Button(ventana, text="🪨 Piedra", font=("Arial", 12), bg="#4caf50", fg="white", width=20,
                         command=lambda: jugar("piedra"))
boton_piedra.pack(pady=5)

boton_papel = tk.Button(ventana, text="📄 Papel", font=("Arial", 12), bg="#2196f3", fg="white", width=20,
                        command=lambda: jugar("papel"))
boton_papel.pack(pady=5)

boton_tijera = tk.Button(ventana, text="✂️ Tijera", font=("Arial", 12), bg="#f44336", fg="white", width=20,
                         command=lambda: jugar("tijera"))
boton_tijera.pack(pady=5)

# Botón reiniciar (inicialmente oculto)
boton_reiniciar = tk.Button(ventana, text="🔁 Jugar otra vez", font=("Arial", 12), bg="#ff9800", fg="black", width=20,
                            command=reiniciar_juego)

ventana.mainloop()

