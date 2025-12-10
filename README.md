<p align="center">
   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Eight-queens-animation.gif/220px-Eight-queens-animation.gif" 
      alt="8 queens animation"/>
</p>

<h1 align="center">♛ 8 Queens Solver — Backtracking Edition</h1>

<p align="center">
   <img src="https://img.shields.io/badge/STATUS-COMPLETED-green?style=for-the-badge">

   <a href="https://docs.python.org/3/">
      <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"></a>

   <img src="https://img.shields.io/badge/Algorithm-Backtracking-orange?style=for-the-badge">

   <a href="https://github.com/lukatinarelli/8-Queens-Backtracking/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/License-CC0-lightgrey?style=for-the-badge"></a>
</p>


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
   python main.py
   ```
2. Introducir la posición inicial de la reina (ej. A1, H8, etc.)
3. El programa mostrará la solución completa

### Ejemplo
```
Introduce la posición inicial de la reina (ejemplo: A1):
Solución encontrada:

    A B C D E F G H
  +-----------------+
1 |♛ - - - - - - - |
2 |- - - - - ♛ - - |
3 |- - - - - - - ♛ |
4 |- ♛ - - - - - - |
5 |- - - ♛ - - - - |
6 |- - - - - - ♛ - |
7 |- - ♛ - - - - - |
8 |- - - - ♛ - - - |
  +-----------------+
```

## Estructura del Código 🧱
```python
# Tablero 9x9 (8x8 + bordes para coordenadas)
tablero = [["-" for _ in range(9)] for _ in range(9)]  

# Función principal recursiva
def colocar_reina(tablero, reinas):
    # Lógica de backtracking...

# Función secundaria
def comprobar_reina(tablero, fila, columna, reinas):
    # Comprobar si alguna reina del tablero le puede atacar
```

## Recursos útiles 🔗
- [Problema de las 8 reinas en Wikipedia](https://es.wikipedia.org/wiki/Problema_de_las_ocho_reinas)
- [Documentación oficial de Python](https://docs.python.org/es/3/)

## Contribuir 🤝
Las sugerencias y mejoras son bienvenidas. Si quieres aportar, puedes abrir un issue o enviar un pull request.

## Autor ✍️
Luka Ramon Tinarelli - Técnico de ASIR en prácticas, apasionado por la programación y la automatización.

## Licencia 📄
Este proyecto está bajo la licencia [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](LICENSE).
