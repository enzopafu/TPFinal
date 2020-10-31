#! /usr/bin/env python3
from cliente import Cliente
from clienteParticular import ClienteParticular
from clienteCorporativo import ClienteCorporativo
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos
from trabajo import Trabajo
import datetime

class ListaTrabajos:
    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.lista_t = self.rt.get_all()

    def nuevo_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):
        t = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion, False)
        t.id_trabajo = self.rt.store(t)
        if t.id_trabajo == 0:
            return None
        else:
            self.lista_t.append(t)
            return t

    def _buscar_por_id(self, id_trabajo):
        """Recibe un id de contacto y retorna el contacto que coincide con esa
        id, o None si ninguno de ellos coincide"""
        for X in self.lista_t:
            if X.id_trabajo == int(id_trabajo):
                return (X)
        return None

    def finalizar_trabajo(self, id_trabajo):
        """Recibe un id_contacto y el nombre de una ciudad, y modifica la ciudad
        del contacto que tenga esa id. Retorna True si tiene éxito y False de
        lo contrario"""
        trabajo = self._buscar_por_id(id_trabajo)
        if trabajo:
            trabajo.fecha_entrega_real = datetime.date.today()
            self.rt.update(trabajo)
            self.lista_t = self.rt.get_all()
            return True
        return False

