import os

class ServicioPeliculas:

    def __init__(self):
        self.archivo_peliculas = 'peliculas.txt'

    def agregar_peliculas(self, pelicula):
        with open(self.archivo_peliculas, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        with open(self.archivo_peliculas, 'r', encoding='utf8') as archivo:
            print('--- Listado de Peliculas ---')
            print(archivo.read())

    def eliminar_archivo(self):
        os.remove(self.archivo_peliculas)
        print(f'Archivo eliminado {self.archivo_peliculas}')