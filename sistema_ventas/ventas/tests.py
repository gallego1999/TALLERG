from django.test import TestCase
from .models import Producto

class ProductoModelTest(TestCase):
    def setUp(self):
        Producto.objects.create(nombre="Laptop", precio=1000.00, stock=10)

    def test_producto_str(self):
        producto = Producto.objects.get(nombre="Laptop")
        self.assertEqual(str(producto), "Laptop")
