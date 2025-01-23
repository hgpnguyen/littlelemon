from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice cream", price=3.5, inventory=100)
        Menu.objects.create(title="Beef pasta", price=6.5, inventory=20)
        Menu.objects.create(title="Noodle soup", price=4, inventory=30)
        self.client = Client()
        return super().setUp()
    

    def test_getall(self):
        allMenu = Menu.objects.all()
        serializer = MenuSerializer(allMenu, many=True)
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(serializer.data, response.data)