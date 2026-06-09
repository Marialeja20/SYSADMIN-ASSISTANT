import platform
import socket
import psutil
import getpass
from datetime import datetime

def GeneracionReportes():
    print("\n=== GENERACION DE REPORTES ===")
    nombre_archivo = "ReporteSistema.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as reporte:
        reporte.write("===== REPORTE DEL SISTEMA =====\n\n")
        reporte.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        reporte.write("=== INFORMACION DEL SISTEMA ===\n")
        reporte.write(f"Nombre del equipo: {socket.gethostname()}\n")
        reporte.write(f"Usuario: {getpass.getuser()}\n")
        reporte.write(f"Sistema Operativo: {platform.system()}\n")
        reporte.write(f"Version: {platform.version()}\n")
        reporte.write(f"Arquitectura: {platform.architecture()[0]}\n")
        reporte.write(f"Direccion IP: {socket.gethostbyname(socket.gethostname())}\n\n")
        reporte.write("=== RECURSOS UTILIZADOS ===\n")
        memoria = psutil.virtual_memory()
        reporte.write(f"RAM Total: {round(memoria.total/(1024**3),2)} GB\n")
        reporte.write(f"RAM Utilizada: {round(memoria.used/(1024**3),2)} GB\n")
        reporte.write(f"RAM Libre: {round(memoria.available/(1024**3),2)} GB\n")
        reporte.write(f"CPU Utilizada: {psutil.cpu_percent(1)} %\n")
        disco = psutil.disk_usage('/')
        reporte.write(f"Disco Total: {round(disco.total/(1024**3),2)} GB\n")
        reporte.write(f"Disco Utilizado: {round(disco.used/(1024**3),2)} GB\n")
        reporte.write(f"Disco Libre: {round(disco.free/(1024**3),2)} GB\n\n")
        reporte.write("=== PROCESOS ACTIVOS ===\n")
        reporte.write(f"{'PID':<10}{'NOMBRE':<30}\n")
        reporte.write("-" * 40 + "\n")
        for proceso in psutil.process_iter(['pid', 'name']):
            try:
                pid = proceso.info['pid']
                nombre = proceso.info['name']
                reporte.write(f"{pid:<10}{nombre:<30}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    print("\nReporte generado correctamente.")
    print(f"Archivo creado: {nombre_archivo}")

# ↓ FUERA de la función
if __name__ == "__main__":
    GeneracionReportes()