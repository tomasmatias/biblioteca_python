# Clase libro

class Libro:
    def __init__(self, titulo, autor, disponibilidad=True):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidad = disponibilidad

    def __str__(self):
        estado = "Disponible" if self.disponibilidad else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"

# Clase Biblioteca

class Biblioteca:
    def __init__(self):
        self.libros = []

# Función agregar libro

    def agregar_libro(self, titulo, autor):
        libro = Libro(titulo, autor)
        self.libros.append(libro)
        print("Libro agregado exitosamente.")

# Función buscar libro

    def buscar_libro(self, titulo):
        libros_encontrados = []
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                libros_encontrados.append(libro)
        return libros_encontrados
    
# Función prestar libro

    def prestar_libro(self, titulo):
        libro_encontrado = None
        for libro in self.libros:
            if titulo.lower() == libro.titulo.lower() and libro.disponibilidad:
                libro.disponibilidad = False
                libro_encontrado = libro
                break
        return libro_encontrado
    
# Función devolver libro

    def devolver_libro(self, titulo):
        libro_encontrado = None
        for libro in self.libros:
            if titulo.lower() == libro.titulo.lower() and not libro.disponibilidad:
                libro.disponibilidad = True
                libro_encontrado = libro
                break
        return libro_encontrado

# Función mostrar libro

    def mostrar_libros(self):
        print("----- Lista de Libros -----")
        if len(self.libros) == 0:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros:
                print(libro)

# Programa principal

biblioteca = Biblioteca()

while True:
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar libros")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        biblioteca.agregar_libro(titulo, autor)
    elif opcion == "2":
        titulo = input("Ingrese el título del libro a buscar: ")
        libros_encontrados = biblioteca.buscar_libro(titulo)
        if len(libros_encontrados) == 0:
            print("No se encontraron libros con ese título.")
        else:
            print("Libros encontrados:")
            for libro in libros_encontrados:
                print(libro)
    elif opcion == "3":
        titulo = input("Ingrese el título del libro a prestar: ")
        libro_prestado = biblioteca.prestar_libro(titulo)
        if libro_prestado:
            print(f"El libro '{libro_prestado.titulo}' ha sido prestado.")
        else:
            print("El libro no está disponible o no existe en la biblioteca.")
    elif opcion == "4":
        titulo = input("Ingrese el título del libro a devolver: ")
        libro_devuelto = biblioteca.devolver_libro(titulo)
        if libro_devuelto:
            print(f"El libro '{libro_devuelto.titulo}' ha sido devuelto.")
        else:
            print("El libro no está prestado o no existe en la biblioteca.")
    elif opcion == "5":
        biblioteca.mostrar_libros()
    elif opcion == "6":
        print("Ud esta saliendo del programa.")
        break
    else:
        print("Opción inválida.")
