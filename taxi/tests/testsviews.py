from django.test import TestCase
from django.urls import reverse


class PublicTest(TestCase):
	def test_login_required(self):
		response_driver = self.client.get(reverse('taxi:driver-list'))
		response_manufacturer = self.client.get(reverse('taxi:manufacturer-list'))
		response_car = self.client.get(reverse('taxi:car-list'))
		self.assertNotEqual(response_driver.status_code, 200)
		self.assertNotEqual(response_manufacturer.status_code, 200)
		self.assertNotEqual(response_car.status_code, 200)
