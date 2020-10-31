#! /usr/bin/env python3
from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo

class ListaTrabajos:
    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.lista_t = self.rt.get_all()

    def nuevo_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):
        t = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion, False)
        t.id_cliente = self.rt.store(t)
        if t.id_cliente == 0:
            return None
        else:
            self.lista_t.append(t)
            return t
    def _buscar_por_id(self, id_trabajo):
        """Recibe un id de contacto y retorna el contacto que coincide con esa
        id, o None si ninguno de ellos coincide"""
        for X in self.lista_t:
            if X.id_cliente == int(id_trabajo):
                return (X)
        return None