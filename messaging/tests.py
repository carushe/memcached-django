from django.test import TestCase

# Create your tests here.


class TestMeClass(TestCase):
    def setUp(self) -> None:
        self.value = "value test"

    def test_value(self):
        self.assertEqual("value test", self.value)
