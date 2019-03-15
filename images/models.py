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






class Images(models.Model):

    name = models.CharField(max_length =30)
    Images_Main_Img = models.ImageField(upload_to='images/') 
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
   



    def __str__(self):
        return self.name


    def save_image(self):
        self.save()

    @classmethod
    def get_image(cls,id):
        try:
            image=Images.objects.get(id=id)
            return image
        except DoesNotExist:
            return Images.objects.get(id=1)


    # def delete_editor(self):
    #     self.delete()

    # def update_editor(self):
    #     self.update()
    
    # def display_editor(self):
    #     self.display()

    # class Meta:
    #     ordering = ['name','welcome_Main_Img']
