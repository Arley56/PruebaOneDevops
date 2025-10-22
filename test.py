import unittest
import json
from main import app

class FlaskApiTestCase(unittest.TestCase):
    def setUp(self):
        # ✅ Corregido: es "test_client()", no "tes_client()"
        self.app = app.test_client()
        self.app.testing = True

    def test_suma(self):
        # ✅ Llamada correcta al endpoint (usa '?a=2&b=3')
        response = self.app.get('/suma?a=2&b=3')
        data = json.loads(response.data)

        # ✅ Corregido: era "asserEqual" y "resultadp"
        self.assertEqual(data['resultado'], 5)

    def test_multiplicacion(self):
        # ✅ Corregido: falta el "/" y los ":" en el json
        response = self.app.post('/multiplicacion', json={'a': 4, 'b': 5})
        data = json.loads(response.data)

        self.assertEqual(data['resultado'], 20)

if __name__ == '__main__':
    unittest.main()
