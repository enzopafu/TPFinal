#! /usr/bin/env python3
from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes

class ListaClientes:
    def __init__(self):
        self.rc = RepositorioClientes()
        self.lista = self.rc.get_all()

    def nuevo_cliente_corporativo(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail):
        c = ClienteCorporativo(nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return None
        else:
            self.lista.append(c)
            return c

    def nuevo_cliente_particular(self, nombre, apellido, telefono, mail):
        c = ClienteParticular(nombre, apellido, telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return None
        else:
            self.lista.append(c)
            return c

    def _buscar_por_id(self, id_cliente):
        """Recibe un id de contacto y retorna el contacto que coincide con esa
        id, o None si ninguno de ellos coincide"""
        for X in self.lista:
            if X.id_cliente == int(id_cliente):
                return (X)
        return None

    def modificar_cliente_corporativo(self, id_cliente, nombre_empresa, nombre_contacto, telefono_contacto, telefono,
                                      mail):
        """Recibe un id_cliente y el nombre de la empresa, nombre del contacto y su telefono, telefono de la empresa y mail y lo modifica la ciudad
        al cliente que tenga esa id. Retorna True si tiene éxito y False de
        lo contrario"""
        cliente = self._buscar_por_id(id_cliente)
        if cliente:
            cliente.nombre_empresa = nombre_empresa
            cliente.nombre_contacto = nombre_contacto
            cliente.telefono_contacto = telefono_contacto
            cliente.telefono = telefono
            cliente.mail = mail
            return True
        return False

    def modificar_cliente_particular(self, id_cliente, nombre, apellido, telefono, mail):
        """Recibe un id_cliente y el nombre de la empresa, nombre del contacto y su telefono, telefono de la empresa y mail y lo modifica la ciudad
        al cliente que tenga esa id. Retorna True si tiene éxito y False de
        lo contrario"""
        cliente = self._buscar_por_id(id_cliente)
        if cliente:
            cliente.nombre = nombre
            cliente.apellido = apellido
            cliente.telefono = telefono
            cliente.mail = mail
            return True
        return False