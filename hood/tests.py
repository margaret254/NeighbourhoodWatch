from django.test import TestCase
from .models import Neighbourhood,Profile

# Create your tests here.
 class NeighbourhoodTestClass(TestCase):

     # Set Up method

     def setUp(self):
         self.nairobi = Neighbourhood(name = 'Nairobi',location='Kayole',occupants='5',health_contact='3456789',police_contact='2345677')

         # Testing Instance

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Neighbourhood))

    def test_save_post(self):
        self.new_hood.create_neigborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_post(self):
        self.new_hood.create_neigborhood()
        self.new_hood.delete_neigborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood)==0)

    def tearDown(self):
        Neighborhood.objects.all().delete() 



class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_profile = Profile(user_id=2,hood_id=3,bio="Hello", email='maggiemwas91@gmail.com',name="Tesh")
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    
    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0) 
    
    def tearDown(self):
        Profile.objects.all().delete()


