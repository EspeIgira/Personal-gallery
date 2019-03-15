from django.test import TestCase
from .models import Image,Category,Location



class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.hotel = Category(name = 'hotel')
        self.place= Location(city = 'kigali',country = 'Rwanda')
        self.food= Image(name = 'food',description='Our yummy test food.', Image_Main_Img ='gallery/yummy.jpg',location=self.place,category=self.hotel)
        self.hotel.save()
        self.place.save()

        self.food.save_image()
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Image))

        # Creating a new tag and saving it
        self.hotel = Category(name = 'hotel')
        self.hotel.save()

        self.place= Location(city = 'kigali',country = 'Rwanda')
        self.place.save()

        self.place.hotel.add(self.hotel)


    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()


    def images_of_day(self):
        images = Image.images()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
       self.food.save_image()
       images = Image.objects.all()
       self.assertTrue(len(images) > 0)

    def test_display_method(self):
        self.food.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_method(self):
        self.food.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
       








