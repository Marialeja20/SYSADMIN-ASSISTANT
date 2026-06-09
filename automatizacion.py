# ============================================
# Módulo: automatizacion.py
# ============================================
import time
from reportes import GeneracionReportes
from backup import SistemaCopiasSeguridad
from organizador import OrganizadorAutomaticoArchivos

def AutomatizacionProgramada():
    print("\n=== AUTOMATIZACION PROGRAMADA ===")
    print("1. Generar reporte automatico")
    print("2. Realizar backup automatico")
    print("3. Organizar archivos automatico")
    print("4. Volver")
    opcion = input("Seleccione una opcion: ")
    if opcion == "4":
        return
    if opcion in ["1", "2", "3"]:
        minutos = int(input("Cada cuantos minutos: "))
        print(f"Tarea programada cada {minutos} minuto(s).")
        print("Presione Ctrl+C para detener.")
        try:
            while True:
                if opcion == "1":
                    GeneracionReportes()
                elif opcion == "2":
                    SistemaCopiasSeguridad()
                elif opcion == "3":
                    OrganizadorAutomaticoArchivos()
                print(f"Proxima ejecucion en {minutos} minuto(s)...")
                time.sleep(minutos * 60)
        except KeyboardInterrupt:
            print("\nAutomatizacion detenida por el usuario.")
    else:
        print("Opcion invalida.")

if __name__ == "__main__":
    AutomatizacionProgramada()
