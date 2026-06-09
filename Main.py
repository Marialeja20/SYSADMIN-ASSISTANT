# MENU PRINCIPAL
# ==========================
from informacion import InformacionEquipo, InformacionHardware
from procesos import MonitorProcesos
from organizador import OrganizadorAutomaticoArchivos
from backup import SistemaCopiasSeguridad
from reportes import GeneracionReportes
from automatizacion import AutomatizacionProgramada

if __name__ == "__main__":
    while True:
        print("\n==============================")
        print("      SYSADMIN ASSISTANT")
        print("==============================")
        print("1. Informacion del equipo")
        print("2. Monitor de Procesos")
        print("3. Organizador Automatico de Archivos")
        print("4. Sistemas de Copias de Seguridad")
        print("5. Generacion de Reportes")
        print("6. Automatizacion Programada")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            InformacionEquipo()
            InformacionHardware()
        elif opcion == "2":
            MonitorProcesos()
        elif opcion == "3":
            OrganizadorAutomaticoArchivos()
        elif opcion == "4":
            SistemaCopiasSeguridad()
        elif opcion == "5":
            GeneracionReportes()
        elif opcion == "6":
            AutomatizacionProgramada()
        elif opcion == "7":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida, intentalo nuevamente")