from django.db import models

class Images(models.Model):

    name = models.CharField(max_length =30)
    Images_Main_Img = models.ImageField(upload_to='images/') 
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
   
class Category(models.Model):

    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name



class Location(models.Model):

    city = models.CharField(max_length =60)
    country = models.CharField(max_length =60)

    def __str__(self):
        return self.city




     # def __str__(self):
    #     return self.name


    # def save_editor(self):
    #     self.save()


    # def delete_editor(self):
    #     self.delete()

    # def update_editor(self):
    #     self.update()
    
    # def display_editor(self):
    #     self.display()

    # class Meta:
    #     ordering = ['name','welcome_Main_Img']
