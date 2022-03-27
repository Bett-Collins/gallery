from django.db import models
from django.db.models.base import Model

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100,blank=True,null=True )
    

    def __str__(self):
        return self.category_name

    def save_categories(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def search_by_category_name(cls,search_term):
        category = cls.objects.filter(category_name__icontains=search_term)
        return category

    def display_searched():
        category=Image.objects.all()
        return category

class Location(models.Model):
    location_name=models.CharField(max_length=50,blank=False ,null=True)
    

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()




class Image(models.Model):
    image=models.ImageField(null=True,blank=False)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=4000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    @classmethod
    def update_image(self):
        image=Image.objects.get_or_create()
        return image





