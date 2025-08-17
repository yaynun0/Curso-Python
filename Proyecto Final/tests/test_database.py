import unittest
import copy
import database as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista=[
            db.Cliente('15J','Marta','Hernandez'),
            db.Cliente('23G','Miguel','Soto'),
            db.Cliente('23Z','Ana','Garcia')
        ]

    def test_buscar_cliente(self):
        cliente_existente=db.Clientes.buscar('15J')
        cliente_inexistente=db.Clientes.buscar('24L')
        self.assertIsNone(cliente_inexistente)
        self.assertIsNotNone(cliente_existente)

    def test_crear_cliente(self):
        nuevo_cliente=db.Clientes.crear('39X','Gerardo','Nuñez')
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(nuevo_cliente.dni,'39X')
        self.assertEqual(nuevo_cliente.nombre,'Gerardo')
        self.assertEqual(nuevo_cliente.apellido,'Nuñez')

    def test_modificar_cliente(self):
        cliente_xmod=copy.copy(db.Clientes.buscar('23Z'))
        cliente_modificado=db.Clientes.modificar('23Z','Mariana','Garcia')
        self.assertEqual(cliente_xmod.nombre,'Ana')
        self.assertEqual(cliente_modificado.nombre,'Mariana')

    def test_borrar_cliente(self):
        cliente_borrado=db.Clientes.borrar('23G')
        cliente_rebusc=db.Clientes.buscar('23G')
        self.assertEqual(cliente_borrado.dni,'23G')
        self.assertIsNone(cliente_rebusc)
