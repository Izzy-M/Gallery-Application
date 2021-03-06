from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

# Create your models here.
class Pic(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    author=models.CharField(max_length=30)
    category=models.ForeignKey('Category',on_delete=CASCADE)
    location=models.ForeignKey('Location',on_delete=CASCADE)
    posted=models.DateField(auto_now=True)
    image= CloudinaryField('image')
    def __str__(self):
        return self.title
    def save_image(self):
        self.save()
        
    @classmethod
    def delete(cls,self,id):
        query=Pic.objects.get(cls.id==id)
        for item in query:
            self.delete(item)
            
    def get_all():
        query=Pic.objects.all()
        return query
    @classmethod
    def search_category(cls,category):
        query= cls.objects.filter(category=category)
        return query
    
class Location(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    def save_location(self):
        self.save()
        
    def deletelocation(self):
        self.delete()
    
        
    @classmethod
    def get_location(self):
        locations=Location.objects.all()
        
        return locations
        
    
        
class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
        
    def save_category(self):
        self.save()
        
    @classmethod
    def search_category(cls,category):
        query= cls.objects.filter(name=category)
        return query