#conexion con sql magnament server studio
import pyodbc

try:
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-SAC7IAI;'
        'DATABASE=biblioteca;'       
        'Trusted_Connection=yes;'        
    )
    print(" Conexión exitosa a SQL Server.\n")
except Exception as e:
    print(" Error al conectar:", e)
    exit()

cursor = conexion.cursor()

def insertar_autor():
    nombre = input("Nombre del autor: ")
    nacionalidad = input("Nacionalidad: ")
    cursor.execute("INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)", (nombre, nacionalidad))
    conexion.commit()
    print("Autor agregado correctamente.\n")

def insertar_libro():
    titulo = input("Título del libro: ")
    genero = input("Género: ")
    anio = int(input("Año de publicación: "))
    id_autor = int(input("ID del autor: "))
    cursor.execute("INSERT INTO libros (titulo, genero, año, id_autor) VALUES (?, ?, ?, ?)", 
                   (titulo, genero, anio, id_autor))
    conexion.commit()
    print("Libro agregado correctamente.\n")

def listar_autores():
    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()
    print("\n--- LISTA DE AUTORES ---")
    for a in autores:
        print(f"ID: {a[0]}, Nombre: {a[1]}, Nacionalidad: {a[2]}")
    print()

def listar_libros():
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.genero, libros.año, autores.nombre
        FROM libros
        JOIN autores ON libros.id_autor = autores.id
    """)
    libros = cursor.fetchall()
    print("\n--- LISTA DE LIBROS ---")
    for l in libros:
        print(f"ID: {l[0]}, Título: {l[1]}, Género: {l[2]}, Año: {l[3]}, Autor: {l[4]}")
    print()

def actualizar_libro():
    id_libro = int(input("ID del libro a actualizar: "))
    nuevo_titulo = input("Nuevo título: ")
    cursor.execute("UPDATE libros SET titulo = ? WHERE id = ?", (nuevo_titulo, id_libro))
    conexion.commit()
    print(" Libro actualizado correctamente.\n")

def eliminar_autor():
    id_autor = int(input("ID del autor a eliminar: "))
    cursor.execute("DELETE FROM autores WHERE id = ?", (id_autor,))
    conexion.commit()
    print("Autor eliminado correctamente.\n")


# MENÚ PRINCIPAL
def menu():
    while True:
        print("""
========= MENÚ PRINCIPAL =========
1. Insertar autor
2. Insertar libro
3. Listar autores
4. Listar libros
5. Actualizar libro
6. Eliminar autor
0. Salir
""")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            insertar_autor()
        elif opcion == "2":
            insertar_libro()
        elif opcion == "3":
            listar_autores()
        elif opcion == "4":
            listar_libros()
        elif opcion == "5":
            actualizar_libro()
        elif opcion == "6":
            eliminar_autor()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")

menu()

cursor.close()
conexion.close()
