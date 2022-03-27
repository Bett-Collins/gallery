from django.test import TestCase
from .models import Editor,Article,tags
# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Collins= Editor(first_name = 'Collins', last_name ='Bett', email ='arapbett1996@gmail.com')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Collins,Editor))