# SYSADMIN ASSISTANT

## Descripción

Este proyecto implementa un asistente de administración de sistemas desarrollado en Python. La aplicación permite obtener información del equipo, monitorear procesos, organizar archivos automáticamente, realizar copias de seguridad, generar reportes del sistema y programar tareas automáticas.

El objetivo es facilitar tareas básicas de administración y mantenimiento de un sistema operativo mediante una interfaz de consola sencilla e intuitiva.

---

## Estructura del Proyecto

### 1. Módulo de Información del Sistema

Este módulo permite visualizar información general del equipo y del hardware.

**Funciones principales:**

* Nombre del equipo.
* Usuario actual.
* Sistema operativo.
* Versión del sistema.
* Arquitectura.
* Dirección IP.
* Memoria RAM total, utilizada y libre.
* Uso de CPU.
* Estado del disco duro.

---

### 2. Módulo de Monitor de Procesos

Este módulo permite supervisar los procesos que se encuentran activos en el sistema.

**Funcionalidades:**

* Mostrar procesos activos.
* Mostrar PID.
* Mostrar nombre del proceso.
* Mostrar uso de memoria.
* Mostrar uso de CPU.
* Buscar procesos por nombre.
* Finalizar procesos seleccionados.
* Protección contra la finalización de procesos críticos del sistema.

---

### 3. Módulo de Organizador Automático de Archivos

Permite organizar automáticamente los archivos de una carpeta según su tipo.

**Clasificación automática:**

* Documentos
* Imágenes
* Videos
* Otros

El sistema crea las carpetas necesarias y mueve los archivos a su ubicación correspondiente.

---

### 4. Módulo de Copias de Seguridad

Permite generar respaldos de carpetas seleccionadas por el usuario.

**Características:**

* Selección de carpeta origen.
* Selección de carpeta destino.
* Registro de fecha y hora del respaldo.
* Almacenamiento del historial de copias realizadas.
* Validación de rutas.

---

### 5. Módulo de Generación de Reportes

Genera automáticamente reportes del estado actual del sistema.

**Información incluida:**

* Fecha de generación.
* Información del sistema.
* Recursos utilizados.
* Procesos activos.
* Estado de memoria RAM.
* Estado del disco duro.

**Formato generado:**

* TXT

---

### 6. Módulo de Automatización Programada

Permite programar tareas automáticas dentro de la aplicación.

**Tareas disponibles:**

* Generar reportes automáticamente.
* Ejecutar copias de seguridad.
* Organizar archivos.
* Programar intervalos de ejecución.

---

## Tecnologías Utilizadas

* Python 3
* psutil
* os
* shutil
* socket
* getpass
* datetime
* time

---

## Instrucciones de Uso

1. Clonar el repositorio.
2. Instalar las dependencias necesarias.

```bash
pip install psutil
```

3. Ejecutar el archivo principal.

```bash
python Main.py
```

4. Seleccionar el módulo deseado desde el menú principal.

---

## Arquitectura del Proyecto

El proyecto se encuentra organizado en módulos independientes:

* Main.py → Menú principal.
* informacion.py → Información del sistema.
* procesos.py → Monitor de procesos.
* organizador.py → Organización automática de archivos.
* backup.py → Copias de seguridad.
* reportes.py → Generación de reportes.
* automatizacion.py → Automatización de tareas.

Esta estructura permite mantener un código más organizado, reutilizable y fácil de mantener.

---

## Autor

María Alejandra Pérez Banquez

Proyecto Final – Sistemas Operativos
