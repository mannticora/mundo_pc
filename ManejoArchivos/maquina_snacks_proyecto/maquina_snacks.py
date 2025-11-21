from ManejoArchivos.maquina_snacks_proyecto.servicio_snacks import ServicioSnacks


class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []

    def maquinasnacks(self):
        salir = False
        print('*** Maquina de Snacks ***')
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrio un error: {e}')

    def mostrar_menu(self):
        print('''Menu:
        1. Comprar snack
        2. Mostrar Snack
        3. Agregar nuevo snack al inventario
        4. Inventario Snacks
        5. Salir
        ''')

    def ejecutar_opcion(self):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Regresa pronto!')
            return True
        else:
            print(f'Opcion invalida: {opcion}')
        return False