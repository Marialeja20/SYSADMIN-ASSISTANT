# ============================================
# Módulo: organizador.py
# Organiza automáticamente archivos en carpetas
# según su tipo (documentos, imágenes, videos, otros).
# ============================================
import os
import shutil

def OrganizadorAutomaticoArchivos():
    print("\n=== ORGANIZADOR AUTOMATICO DE ARCHIVOS ===")
    ruta = input("Ingrese la ruta de la carpeta: ")
    if not os.path.exists(ruta):
        print("La carpeta no existe.")
        return
    archivos_movidos = 0
    for archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_archivo):
            extension = archivo.split(".")[-1].lower()
            if extension in ["pdf", "doc", "docx", "xls", "xlsx", "txt"]:
                carpeta = "Documentos"
            elif extension in ["jpg", "jpeg", "png", "gif"]:
                carpeta = "Imagenes"
            elif extension in ["mp4", "avi", "mkv"]:
                carpeta = "Videos"
            else:
                carpeta = "Otros"
            ruta_destino = os.path.join(ruta, carpeta)
            os.makedirs(ruta_destino, exist_ok=True)
            shutil.move(ruta_archivo, os.path.join(ruta_destino, archivo))
            print(f"  Movido: {archivo} → {carpeta}")
            archivos_movidos += 1
    print(f"\nArchivos organizados correctamente. Total: {archivos_movidos}")
if __name__ == "__main__":
    OrganizadorAutomaticoArchivos()