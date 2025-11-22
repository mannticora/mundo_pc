from ManejoArchivos.catalogo_peliculas_proyecto.pelicula import Pelicula
from ManejoArchivos.catalogo_peliculas_proyecto.servicio_peliculas import ServicioPeliculas


class CatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def mostrar_menu(self):
        print('*** App Catalogo Peliculas ***')
        while True:
            try:
                print('''Opciones:
                1. Agregar pelicula
                2. Listar Peliculas
                3. Eliminar Peliculas
                4. Salir
                ''')
                opcion = int(input('Elige una opcion: '))
                if opcion == 1:
                    nombre_pelicula = input('Dame el nombre de la pelicula: ')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_peliculas(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo()
                elif opcion == 4:
                    print('Saliendo del progrmaa ')
                    break
                else:
                    print('Opcion invalida, proporciona un valor del 1-4')

            except ValueError:
                print('Error: introduce un valor valido.')
            except Exception as e:
                print(f'Ocurrio un error: {e}')

if __name__ == '__main__':
    app = CatalogoPeliculas()
    app.mostrar_menu()