from django.db import models

class Welcome(models.Model):

    name = models.CharField(max_length =30)
    welcome_Main_Img = models.ImageField(upload_to='images/') 

    def __str__(self):
        return self.name


    def save_editor(self):
        self.save()


    def delete_editor(self):
        self.delete()

    def update_editor(self):
        self.update()
    
    def display_editor(self):
        self.display()

    class Meta:
        ordering = ['name']