# ============================================
# Módulo: procesos.py
# Funciones para monitorear, buscar y finalizar
# procesos activos del sistema.
# ============================================
import psutil

def MostrarProcesos():
    print("\n=== LISTA DE PROCESOS ===")
    print(f"{'PID':<10}{'NOMBRE':<30}{'MEMORIA %':<15}{'CPU %':<10}")
    for proceso in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
        try:
            pid = proceso.info['pid']
            nombre = proceso.info['name']
            memoria = proceso.info['memory_percent']
            cpu = proceso.info['cpu_percent']
            print(f"{pid:<10}{nombre:<30}{memoria:<15.2f}{cpu:<10.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def BuscarProceso():
    nombre_buscar = input("\nIngrese el nombre del proceso: ").lower()
    encontrado = False
    for proceso in psutil.process_iter(['pid', 'name']):
        try:
            nombre = proceso.info['name']
            if nombre and nombre_buscar in nombre.lower():
                print(f"PID: {proceso.info['pid']} | Nombre: {nombre}")
                encontrado = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    if not encontrado:
        print("Proceso no encontrado.")

def FinalizarProceso():
    procesos_criticos = [
        "System", "wininit.exe", "csrss.exe",
        "lsass.exe", "services.exe", "smss.exe", "svchost.exe"
    ]
    try:
        pid = int(input("Ingrese el PID del proceso a finalizar: "))
        proceso = psutil.Process(pid)
        nombre = proceso.name()
        if nombre in procesos_criticos:
            print("No se puede finalizar un proceso critico del sistema.")
        else:
            proceso.terminate()
            print("Proceso finalizado correctamente.")
    except psutil.NoSuchProcess:
        print("El proceso no existe.")
    except psutil.AccessDenied:
        print("Acceso denegado.")
    except ValueError:
        print("Debe ingresar un PID valido.")

def MonitorProcesos():
    while True:
        print("\n=== MONITOR DE PROCESOS ===")
        print("1. Mostrar procesos")
        print("2. Buscar proceso")
        print("3. Finalizar proceso")
        print("4. Volver")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            MostrarProcesos()
        elif opcion == "2":
            BuscarProceso()
        elif opcion == "3":
            FinalizarProceso()
        elif opcion == "4":
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    MonitorProcesos()