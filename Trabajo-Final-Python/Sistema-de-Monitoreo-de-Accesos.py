
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime

# -------------------- SISTEMA DE MONITOREO DE ACCESOS --------------------
# Estructuras: vectores y matrices
usuarios = ["admin", "user1", "user2"]
servidores = ["Servidor_A", "Servidor_B", "Servidor_C"]
intentos = []  # Matriz: [usuario, servidor, IP, tipo, hora]

# Función para registrar intento
def RegistrarIntento(usuario, servidor, ip, tipo):
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    intentos.append([usuario, servidor, ip, tipo, hora])
    GenerarAlertas(usuario, ip, tipo)

# Función para generar alertas
def GenerarAlertas(usuario, ip, tipo):
    # Condición: si tipo es "fallido" o IP sospechosa
    if tipo.lower() == "fallido" or ip.startswith("192.168.0."):
        messagebox.showwarning("Alerta", f"Intento sospechoso detectado:\nUsuario: {usuario}\nIP: {ip}")

# Función para mostrar reporte en ventana
def MostrarReporte():
    if not intentos:
        messagebox.showinfo("Reporte", "No hay intentos registrados.")
        return
    df = pd.DataFrame(intentos, columns=["Usuario", "Servidor", "IP", "Tipo", "Hora"])
    reporte_text.delete("1.0", tk.END)
    reporte_text.insert(tk.END, df.to_string(index=False))

# -------------------- INTERFAZ GRÁFICA --------------------
ventana = tk.Tk()
ventana.title("Sistema de Monitoreo de Accesos")
ventana.geometry("500x500")

# Campos de entrada
frame = tk.Frame(ventana)
frame.pack(pady=10)

tk.Label(frame, text="Usuario:").grid(row=0, column=0)
entrada_usuario = tk.Entry(frame)
entrada_usuario.grid(row=0, column=1)

tk.Label(frame, text="Servidor:").grid(row=1, column=0)
entrada_servidor = tk.Entry(frame)
entrada_servidor.grid(row=1, column=1)

tk.Label(frame, text="IP:").grid(row=2, column=0)
entrada_ip = tk.Entry(frame)
entrada_ip.grid(row=2, column=1)

tk.Label(frame, text="Tipo (exitoso/fallido):").grid(row=3, column=0)
entrada_tipo = tk.Entry(frame)
entrada_tipo.grid(row=3, column=1)

# Botón para registrar intento
def registrar():
    usuario = entrada_usuario.get()
    servidor = entrada_servidor.get()
    ip = entrada_ip.get()
    tipo = entrada_tipo.get()

    if usuario and servidor and ip and tipo:
        RegistrarIntento(usuario, servidor, ip, tipo)
        messagebox.showinfo("Registro", "Intento registrado correctamente.")
        entrada_usuario.delete(0, tk.END)
        entrada_servidor.delete(0, tk.END)
        entrada_ip.delete(0, tk.END)
        entrada_tipo.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

tk.Button(ventana, text="Registrar Intento", command=registrar).pack(pady=10)

# Área de reporte
reporte_text = tk.Text(ventana, height=15, width=60)
reporte_text.pack(pady=10)

tk.Button(ventana, text="Mostrar Reporte", command=MostrarReporte).pack(pady=5)

ventana.mainloop()
