from django.test import TestCase

# Create your tests here.

class MyIntegrationTest(TestCase):

    def setUp(self) -> None:
        '''
            Inicializa el set de pruebas.
        '''
        return super().setUp()

    def testHome(self):
        response = self.client.get("/")
        self.assertContains(response , "Team 5, Codo a Codo")

    def testDiego(self):
        response = self.client.get("/diego/")
        self.assertContains(response, "Hola soy Diego Barale del team 5")