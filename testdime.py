import unittest
import db_init
from dime import *
from ana_db import SQlite
from raul_youtube import AppYoutube
from unittest.mock import Mock
from unittest.mock import MagicMock
import unittest; unittest.util._MAX_LENGTH=1000

class Testdime(unittest.TestCase):
    def setUp(self):

        self.mock_video = Mock(Id = 1, Nombre = "Go for Grab - GopherConSG 2018", Duracion = "PT30M37S", Canal = "Singapore Gophers",  Fecha= "2018-05-05T13:18:38.000Z", Likes = '7', Vistas = '718', Descripcion = "Speaker: Stephen Kruger\n\nAn inside look at how Go drives all our critical system development, from overall architecture down to tools and utilities to support our engineering processes\n\nProduced by Engineers.SG")
        self.video = Video(self.mock_video.Nombre,self.mock_video.Duracion,self.mock_video.Canal,self.mock_video.Fecha,self.mock_video.Likes,self.mock_video.Vistas,self.mock_video.Descripcion)
        # db_init.main()
        self.sql = SQlite()
        self.sql.GuardarVideo(self.video)
        self.app = AppYoutube()

    def testMostrarVideo(self):
        self.assertIsInstance(self.sql.MostrarVideo(1),Video)

    def testGuardarVideo(self):
        self.assertIsInstance(self.sql.GuardarVideo(self.video),Video)

    def testBorrarvideo(self):
        self.assertTrue(self.sql.BorrarVideo(4))
        self.asserTrue(self.sql.BorrarVideo(5))
        self.asserTrue(self.sql.BorrarVideo(6))


    def testInfoVideoNombre(self):
        self.assertEqual(self.app.InfoVideo("https://www.youtube.com/watch?v=L688sHqXL2A").Nombre,self.video.Nombre)

    def testInfoVideoDuracion(self):
    	self.assertEqual(self.app.InfoVideo("https://www.youtube.com/watch?v=L688sHqXL2A").Duracion,self.video.Duracion)

    def testInfoVideoCanal(self):
    	self.assertEqual(self.app.InfoVideo("https://www.youtube.com/watch?v=L688sHqXL2A").Canal,self.video.Canal)

    def testInfoVideoFecha(self):
    	self.assertEqual(self.app.InfoVideo("https://www.youtube.com/watch?v=L688sHqXL2A").Fecha,self.video.Fecha)

    def testInfoVideoLikes(self):
    	self.assertEqual(self.app.InfoVideo("https://www.youtube.com/watch?v=L688sHqXL2A").Likes,self.video.Likes)

    def testInfoVideoVistas(self):
    	self.assertEqual(self.app.InfoVideo("https://www.youtube.com/watch?v=L688sHqXL2A").Vistas,self.video.Vistas)

    def testInfoVideoDescripcion(self):
    	#self.maxDiff = None
    	self.assertEqual(self.app.InfoVideo("https://www.youtube.com/watch?v=L688sHqXL2A").Descripcion,self.video.Descripcion)

if __name__ == '__main__':
    unittest.main()
