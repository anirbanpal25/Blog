from django.test import TestCase

from blog.models import Author

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Ani', last_name='Pal')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        len_of_str = len(author.first_name)
        self.assertLess(len_of_str, max_length)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        len_of_str = len(author.last_name)
        self.assertLess(len_of_str, max_length)

   
