
from django.test import TestCase
from .forms import SignUpForm


class TestRegistrationForm(TestCase):
  
  def test_registration_form(self):
    # test invalid data
    invalid_data = {
      "username": "user@test.com",
      "password": "PASS"
    }
    form = SignUpForm(data=invalid_data)
    form.is_valid()
    self.assertTrue(form.errors)

    # test valid data
    valid_data = {
      "username": "user@test.com",
      "password": "PASS"
    }
    
