from django.test import TestCase

# Create your tests here.

class MyIntegrationTest(TestCase):

    def setUp(self) -> None:
        '''
            Inicializa el set de pruebas.
        '''
        return super().setUp()

    def testDiego(self):
        response = self.client.get("/diego/")
        self.assertContains(response, "Hola soy Diego Barale del team 5")
        
    def testVictor(self):
        response = self.client.get("/victor/")
        self.assertContains(response, "Hola soy victor")

    def testValen(self):
        response = self.client.get("/valen/")
        self.assertContains(response, "Hola soy Valen")
