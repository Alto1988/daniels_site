from django.test import TestCase
from .models import Category, ArtPiece


class TestArtShop(TestCase):
    '''
    TODO:
        - Add tests for the following:
        - Models
        - URLS
        - Add mutations to the schema
    '''
    def setUp(self):
        '''
        Create a category and art piece for testing
        '''
        self.category = Category.objects.create(name='Test Category')
        self.art_piece = ArtPiece.objects.create(
            name='Test Art Piece',
            description='Test Description',
            category=self.category,
            price=100.00)

    # def test_that_fails(self):
    #     self.assertTrue(False)

    def test_that_passes(self):
        self.assertEqual(1 + 1, 2)

    def test_category_name_is_valid_true(self):
        test_category = Category.objects.filter(name='Test Category')
        print(test_category[0])
        self.assertTrue(test_category.exists())

    def test_category_name_is_valid_false(self):
        test_category = Category.objects.filter(name='Test False')
        self.assertFalse(test_category.exists())

    def tearDown(self):
        '''
        Delete the category and art piece created for testing
        '''
        self.category.delete()
        self.art_piece.delete()