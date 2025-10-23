from ClasesObjetos.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Monitor(DispositivoEntrada):
    contador_monitores = 0

    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self. tamano = tamano
        super().__init__(marca)