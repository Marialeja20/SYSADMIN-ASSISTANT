# ============================================
# Módulo: informacion.py
# Funciones para obtener información del sistema
# y del hardware del equipo.
# ============================================
import platform
import socket
import psutil
import getpass

def InformacionEquipo():
    print("\n=== Informacion del equipo ===")
    print("Nombre del equipo:", socket.gethostname())
    print("Usuario actual:", getpass.getuser())
    print("Sistema Operativo:", platform.system())
    print("Version:", platform.version())
    print("Arquitectura:", platform.architecture()[0])
    print("Direccion IP:", socket.gethostbyname(socket.gethostname()))

def InformacionHardware():
    memoria = psutil.virtual_memory()
    print("\n=== Informacion del Hardware ===")
    print("RAM Total:", round(memoria.total / (1024**3), 2), "GB")
    print("RAM Utilizada:", round(memoria.used / (1024**3), 2), "GB")
    print("RAM Libre:", round(memoria.available / (1024**3), 2), "GB")
    print("CPU:", psutil.cpu_percent(1), "%")
    disco = psutil.disk_usage('/')
    print("Disco Total:", round(disco.total / (1024**3), 2), "GB")
    print("Disco Utilizado:", round(disco.used / (1024**3), 2), "GB")
    print("Disco Libre:", round(disco.free / (1024**3), 2), "GB")

if __name__ == "__main__":
    InformacionEquipo()
    InformacionHardware()