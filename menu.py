#! /usr/bin/env python3
import sys
import datetime
from repositorioClientes import RepositorioClientes
from clienteCorporativo import ClienteCorporativo
from clienteParticular import ClienteParticular
from listaClientes import ListaClientes

class Menu:
    def __init__(self):
        self.lista_clientes = ListaClientes()
        self.repoc = RepositorioClientes()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
        }
    def mostrar_menu(self):
            print("""
Menú de la agenda:
1. mostrar todos los clientes
2. ingresar nuevo cliente
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
        if lista == None:
            lista = self.lista_clientes.lista
        for cliente in lista:
            print(cliente)
            print("___________________________________________________")

    def nuevo_cliente(self):
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

    def salir(self):
        """Sale del sistema"""
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().ejecutar()