import unittest
import copy
import helpers
import database as db
import csv
import config

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

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido("00A",db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("233Z",db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("F3Z",db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("23Z",db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('15J')
        db.Clientes.borrar('23G')
        db.Clientes.modificar('23Z','Mariana','García')

        dni,nombre,apellido=None,None,None
        
        with open(config.DATABASE_PATH,newline='\n') as arch:
            reader=csv.reader(arch,delimiter=';')
            dni,nombre,apellido=next(reader)

        self.assertEqual(dni,'23Z')
        self.assertEqual(nombre,'Mariana')
        self.assertEqual(apellido,'García')