#! /usr/bin/env python3
import sys
import datetime
from repositorioClientes import RepositorioClientes
from clienteCorporativo import ClienteCorporativo
from clienteParticular import ClienteParticular
from trabajo import Trabajo
from listaTrabajos  import ListaTrabajos
from repositorioTrabajos import RepositorioTrabajos
from listaClientes import ListaClientes

class Menu:
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.repoc = RepositorioClientes()
        self.repot = RepositorioTrabajos()
        self.l_t = ListaTrabajos()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.modificar_cliente,
            "4": self.eliminar_cliente,
            "5": self.nuevo_trabajo,
            "6": self.mostrar_trabajos,
            "7": self.finalizar_trabajo,
            "8": self.retiro_trabajo,
            "9": self.eliminar_trabajo,
            "10": self.informe,
            "11": self.modificar_trabajo,
            "0": self.salir
        }
    def mostrar_menu(self):
            print("""
Menú de la agenda:
1. mostrar todos los clientes
2. ingresar nuevo cliente
3. modificar cliente
4. eliminar cliente
5. cargar nuevo trabajo
6. mostrar trabajos
7. finalizar trabajo
8. entrega de trabajo
9. cancelar un trabajo
10. informe trabajos de un clinte.
11. modificar trabajo
0. Salir
""")

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

    def mostrar_clientes(self, lista=None):
        """muestra a todos los clientes"""
        if lista == None:
            lista = self.lista_clientes.lista
        for cliente in lista:
            print(cliente)
            print("___________________________________________________")

    def nuevo_cliente(self):
        """Solicita los datos del cliente nuevo y lo agrega a la lista"""
        tipo = "A"
        while tipo not in ("c", "C", "p", "P"):
            tipo = input("ingrese el tipo de cliente: C=Corporativo/P=Particular")
        nombre = input("ingrese el nombre: ")
        if tipo in ("c", "C"):
            contacto = input("ingrese nombre del contacto: ")
            tc = input("ingrese el telefono del contacto: ")
        else:
            apellido = input("ingrese el apellido: ")
        tel = input("ingrese el telefono: ")
        mail = input("ingrese el mail: ")
        if tipo in ("c", "C"):
            c = self.lista_clientes.nuevo_cliente_corporativo(nombre, contacto, tc, tel, mail)
        else:
            c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido, tel, mail)
        if c is None:
            print("error al cargar cliente")
        else:
            print("cliente cargado")

    def modificar_cliente(self):
        """Solicita el id del contacto y modifica
        los datos del cliente"""
        id_cliente = int(input("ingrese el id del cliente: "))
        c = self.repoc.get_one(id_cliente)
        if c == None:
            print("el id es inexistente")
        else:
            print("estos son los datos del cliente: ", c)
            tipo = "A"
            while tipo not in ("c", "C", "p", "P"):
                tipo = input("ingrese el tipo de cliente: C=Corporativo/P=Particular")
            nombre = input("ingrese el nombre: ")
            if tipo in ("c", "C"):
                contacto = input("ingrese nombre del contacto: ")
                tc = input("ingrese el telefono del contacto: ")
            else:
                apellido = input("ingrese el apellido: ")
            tel = input("ingrese el telefono: ")
            mail = input("ingrese el mail: ")
            if tipo in ("c", "C"):
                self.lista_clientes.modificar_cliente_corporativo(id_cliente, nombre, contacto, tc, tel, mail)
            else:
                self.lista_clientes.modificar_cliente_particular(id_cliente, nombre, apellido, tel, mail)
            print("cliente modificado")

    def eliminar_cliente(self):
        """Solicita el id del contacto y elimina el contacto"""
        id_cliente = int(input("ingrese el id del cliente"))
        c = self.repoc.get_one(id_cliente)
        if c == None:
            print("el id es inexistente")
        else:
            self.repoc.delete(c)
            self.lista_clientes.lista = self.repoc.get_all()
            print("contacto eliminado")

    def nuevo_trabajo(self):
        """crea nuevo trabajo asignado al cliente correspondiente"""""
        id_cliente = int(input("ingrese el id del cliente que desea cargar: "))
        r = self.repoc.get_one(id_cliente)
        fecha_ingreso = datetime.date.today()
        dia = int(input("ingrese el dia de la entrega: "))
        mes = int(input("ingrese el mes de la entrega: "))
        anio = int(input("ingrese el año de la entrega: "))
        fecha_entrega_propuesta = datetime.date(anio, mes, dia)
        descripcion = input("ingrese las tareas realizadas: ")
        c= self.l_t.nuevo_trabajo(r, fecha_ingreso, fecha_entrega_propuesta, descripcion)
        if c == None:
            print("el trabajo no se cargo")
        else:
            print("trabajo cargado")

    def mostrar_trabajos(self, lista=None ):
        """muestra los trabajo asignado a los cliente correspondiente"""""
        if lista == None:
            lista = self.repot.get_all()
        for trabajo in lista:
            print(trabajo)
            print("___________________________________________________")

    def finalizar_trabajo(self):
        id_trabajo = int(input("ingrese el id del trabajo que desea finalizar: "))
        x = self.repot.get_one(id_trabajo)
        self.l_t.finalizar_trabajo(id_trabajo)
        if x:
            print("trabajo finalizado")
        else:
            print("trabajo no finalizado")

    def retiro_trabajo(self):
        id_trabajo = int(input("ingrese el id del trabajo que desea finalizar: "))
        x = self.repot.get_one(id_trabajo)
        self.l_t.retiro_trabajo(id_trabajo)
        if x:
            print("trabajo retirado")
        else:
            print("trabajo no retirado")

    def eliminar_trabajo(self):
        id_trabajo = int(input("ingrese el id del trabajo"))
        c = self.repot.get_one(id_trabajo)
        if c == None:
            print("el id es inexistente")
        else:
            self.repot.delete(c)
            self.l_t.lista_t = self.repot.get_all()
            print("trabajo eliminado")

    def informe(self):
        id_cliente = int(input("ingrese el id del cliente que desea ver su historial: "))
        c = self.repoc.get_one(id_cliente)
        if c == None:
            print("el id es inexistente")
        else:
            for t in self.l_t.lista_t:
                if t.cliente.id_cliente == id_cliente:
                   print (t)
    def modificar_trabajo(self):
        id_trabajo = int(input("ingrese el id del trabajo"))
        c = self.repot.get_one(id_trabajo)
        if c == None:
            print("el id es inexistente")
        else:
            dia_i = int(input("ingrese el dia del ingreso: "))
            mes_i = int(input("ingrese el mes del ingreso: "))
            anio_i = int(input("ingrese el año del ingreso: "))
            fecha_ingreso = datetime.date(anio_i, mes_i, dia_i)
            dia = int(input("ingrese el dia de la entrega propuesta: "))
            mes = int(input("ingrese el mes de la entrega propuesta: "))
            anio = int(input("ingrese el año de la entrega propuesta: "))
            fecha_entrega_propuesta = datetime.date(anio, mes, dia)
            descripcion = input("Ingrese la nueva descripcion: ")

            self.l_t.modificar_trabajo(id_trabajo,fecha_ingreso,fecha_entrega_propuesta,descripcion)




    def salir(self):
        """Sale del sistema"""
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().ejecutar()