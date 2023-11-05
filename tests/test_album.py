import unittest

from faker import Faker

from src.logica.coleccion import Coleccion
from src.modelo.album import Album
from src.modelo.declarative_base import Session


class AlbumTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.coleccion = Coleccion()
        # Generación de datos con libreria Faker
        self.data_factory = Faker()

    def test_agregar_album(self):
        # Nombre aleatorio
        titulo_album1 = self.data_factory.name()
        # Año aleatorio
        anio_album1 = self.data_factory.year()
        # Frase aleatoria
        descripcion_album1 = self.data_factory.sentence()
        self.coleccion.agregar_album(titulo_album1, anio_album1, descripcion_album1, "CD")
        descripcion_album2 = self.data_factory.sentence()
        self.coleccion.agregar_album("Live Killers", 2013, descripcion_album2, "CASETE")
        anio_album3 = self.data_factory.year()
        descripcion_album3 = self.data_factory.sentence()
        self.coleccion.agregar_album("Clara luna", anio_album3, descripcion_album3, "CASETE")
        consulta1 = self.session.query(Album).filter(Album.titulo == titulo_album1).first()
        consulta2 = self.session.query(Album).filter(Album.id == 2).first()
        self.assertEqual(consulta1.titulo, titulo_album1)
        self.assertIsNotNone(consulta2)