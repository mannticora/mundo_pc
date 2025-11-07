from ClasesObjetos.mundo_pc.computadora import Computadora
from ClasesObjetos.mundo_pc.monitor import Monitor
from ClasesObjetos.mundo_pc.orden import Orden
from ClasesObjetos.mundo_pc.raton import Raton
from ClasesObjetos.mundo_pc.teclado import Teclado

print('*** Mundo PC ***')

# Computadora 1
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('JoyaAsser', 'Bluetooth')
raton2 = Raton('Joyaccess', 'Bluetooth')
monitor2 = Monitor('Samsung', 27.6)
computadora2 = Computadora('ASUS', monitor2, teclado2, raton2)
# Crear lista de computadoras
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
#print(orden1)

teclado3 = Teclado('Dell', 'Bluetooth')
raton3 = Raton('Dell', 'Bluetooth')
monitor3 = Monitor('Samsung', 27.6)
computadora3 = Computadora('Alienware', monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)
print(orden1)