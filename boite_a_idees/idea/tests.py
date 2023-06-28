from django.test import TestCase
from django.urls import reverse


# Create your tests here.
from .models import Idea, Likes, Dislikes

class IdeaModelTest(TestCase):
    
    def test_idea_unique(self):
        idea = Idea(titre="unique-idea")
        idea.save()
    
        duplicate_idea = Idea(titre='unique-idea')
        with self.assertRaises(Exception):
            duplicate_idea.save()
            
 