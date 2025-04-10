from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        This method allows the creation of initial reusable data for a user at the class level once for whole TestCase class.
        """
        cls.user = User(
            email="test@example.com",
            password="test",
            phone_number="+201010101010",
            first_name="Test",
            last_name="Last",
        )

    def test_full_name_property(self):
        """Test the full_name property is set correctly. (first_name + last_name)"""
        self.assertEqual(self.user.full_name, "Test Last")

        # Set first and last into different values
        self.user.first_name = "First"
        self.user.last_name = "Test"
        self.assertEqual(self.user.full_name, "First Test")
