from ClasesObjetos.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Monitor(DispositivoEntrada):
    contador_monitores = 0

    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamano = tamano

    def __str__(self):
        return (f'id: {self.id_monitor}, Marca: {self.marca}'
                f'Tamaño: {self.tamano} in')

if __name__ == '__main__':
    monitor1 = Monitor('Alien Ware', 10.5)
    monitor2 = Monitor( 'HP', 16.3)
    print(monitor1)
    print(monitor2)