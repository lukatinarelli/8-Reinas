# 8 Reinas con Posición Inicial ♛

![Chess board with queens](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Eight-queens-animation.gif/220px-Eight-queens-animation.gif)

## Descripción 📜
Este proyecto implementa una solución al clásico problema de las 8 reinas en un tablero de ajedrez, con la particularidad de que:
- El usuario especifica la posición inicial de una reina
- El programa coloca automáticamente las otras 7 reinas restantes
- Garantiza que ninguna reina pueda atacarse entre sí

## Contexto Académico 🎓
Ejercicio propuesto en el módulo:
- **Implantación de Sistemas Operativos** 
- **Administración de Sistemas Operativos**

Forma parte del currículo del **Ciclo Formativo de Grado Superior en Administración de Sistemas Informáticos en Red (ASIR)**.

## Características Técnicas ⚙️
- Implementado en Python 3
- Tablero de ajedrez visualizado en consola
- Validación de movimientos entre reinas
- Interfaz de usuario simple
- Código con colores para mejor visualización

## Requisitos 📋
- Python 3.x instalado
- Terminal que soporte colores ANSI

## Uso 🖥️
1. Ejecutar el script:
```bash
python ocho_reinas.py
2. Introducir la posición inicial de la reina (ej. A1, H8, etc.)
3. El programa mostrará la solución completa

## Estructura del Código 🧱
# Tablero 9x9 (8x8 + bordes para coordenadas)
tablero = [["-" for _ in range(9)] for _ in range(9)]  

# Función principal recursiva
def colocar_reina(tablero, reinas):
    # Lógica de backtracking...

## Autor ✍️
Luka Ramon Tinarelli - Estudiante de ASIR


## Licencia 📄
Este proyecto está bajo la licencia MIT.
