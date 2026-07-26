from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.forms import CarForm
from taxi.models import Manufacturer


class FormTests(TestCase):
    def test_car_creation_form_with_model_and_manufacturer(self):
        manufacturer = Manufacturer.objects.create(
            name="test manufacturer",
            country="test country",
        )
        driver = get_user_model().objects.create_user(
            username="test.driver",
            password="password123",
            license_number="ABC12345",
        )
        form_data = {
            "model": "test_model",
            "manufacturer": manufacturer.id,
            "drivers": [driver.id],
        }
        form = CarForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(
            form.cleaned_data["model"],
            "test_model"
        )
        self.assertEqual(
            form.cleaned_data["manufacturer"],
            manufacturer
        )
        self.assertIn(
            driver,
            form.cleaned_data["drivers"]
        )
