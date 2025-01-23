from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice cream", price=3.5, inventory=100)
        self.assertEqual(str(item), "Ice cream : 3.5")