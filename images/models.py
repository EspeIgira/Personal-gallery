from django.db import models


class Category(models.Model):

    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_category(cls,name):
        category = cls.objects.filter(name__icontains=name).first()
        images=Image.objects.filter(category=category)
        return images

class Location(models.Model):

    city = models.CharField(max_length =60)
    country = models.CharField(max_length =60)

    def __str__(self):
        return self.city

class Image(models.Model):

    name = models.CharField(max_length =30)
    Image_Main_Img = models.ImageField(upload_to='gallery/') 
    description = models.TextField()
    location = models.ForeignKey(Location, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
   

    def __str__(self):
        return self.name


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()
    
    def display_image(self):
        self.display()

    @classmethod
    def search_by_category(cls,name):
        category = Category.objects.filter(name__icontains=name).all()
        images=None
        for i in category:
            print(i)
            images=cls.objects.filter(category=i.id)
        return images

    class Meta:
        ordering = ['name']

    @classmethod
    def get_image(cls,id):
        # try:
        #     image=Image.objects.get(id=id)
        #     return image
        # except DoesNotExist:
            return Image.objects.get(id=id)

  


    