from django.test import TestCase
from photos.models import Image,Location,Category
# Create your tests here.

class ImageTestClass(TestCase):
    #setup method
    def setUp(self):
        self.image1=Image(image="image",name='Flower',description="Nice image")

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image1,Image))

    def test_save_images(self):
        self.image1.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_delete_images(self):
        self.image1.save_image()
        images_record=Image.objects.all()
        self.image1.delete_image()
        self.assertTrue(len(images_record)==0)

    def test_update_image(self):
        image=Image.objects.first()
        new_image=Image.update_image()
        expected_image=f'{new_image}'
        self.assertTrue(expected_image,'new_image')

    def test_search_category(self):
        category=Image.objects.all()
        search_term='food'
        db_term=search_term
        if db_term !=search_term:
            return('no match')

        else:
            return(search_term)  
class CategoryTestClass(TestCase):
    #setup method
    def setUp(self):
        self.nature=Category(category_name="nature")
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))

    def test_save_categories(self):
        self.nature.save_categories()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)
    def test_delete_categories(self):
        self.nature.save_categories()
        category_record=Category.objects.all()
        self.nature.delete_category()
        self.assertTrue(len(category_record)==0)

class LocationTestClass(TestCase):
    #setup method
    def setUp(self):
        self.nairobi=Location(location_name="Eldoret")
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def test_save_location(self):
        self.nairobi.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete_location(self):
        self.nairobi.save_location()
        location_record=Location.objects.all()
        self.nairobi.delete_location()
        self.assertTrue(len(location_record)==0)
