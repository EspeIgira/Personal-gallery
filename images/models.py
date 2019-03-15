from django.db import models


class Category(models.Model):

    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Location(models.Model):

    city = models.CharField(max_length =60)
    country = models.CharField(max_length =60)

    def __str__(self):
        return self.city


class Image(models.Model):

    name = models.CharField(max_length =30)
    Image_Main_Img = models.ImageField(upload_to='media/images/') 
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
   

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

    class Meta:
        ordering = ['name']

    @classmethod
    def get_image(cls,id):
        try:
            image=Image.objects.get(id=id)
            return image
        except DoesNotExist:
            return Image.objects.get(id=1)

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images


    