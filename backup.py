# ============================================
# Módulo: backup.py
# Realiza copias de seguridad automáticas y guarda
# un registro de la operación.
# ============================================
import os
import shutil
from datetime import datetime

def SistemaCopiasSeguridad():
    print("\n=== Sistema de Copias de Seguridad ===")
    origen = input("Ingrese la ruta de la carpeta a respaldar: ")
    destino = input("Ingrese la ruta donde guardar el backup: ")
    if not destino:
        destino = "./backups"
    if not os.path.exists(origen):
        print("La carpeta origen no existe.")
        return
    os.makedirs(destino, exist_ok=True)
    archivos_copiados = 0
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for archivo in os.listdir(origen):
        ruta_archivo = os.path.join(origen, archivo)
        if os.path.isfile(ruta_archivo):
            shutil.copy2(ruta_archivo, destino)
            print(f"  Copiado: {archivo}")
            archivos_copiados += 1
    with open("registro_backup.txt", "a") as log:
        log.write(f"Fecha: {fecha} | Archivos: {archivos_copiados} | Origen: {origen} | Destino: {destino}\n")
    print(f"\nBackup completo.")
    print(f"Archivos copiados : {archivos_copiados}")
    print(f"Fecha             : {fecha}")
    print(f"Registro guardado : registro_backup.txt")

if __name__ == "__main__":
    SistemaCopiasSeguridad()