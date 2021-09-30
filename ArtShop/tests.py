import json
from django.http import response

from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from .models import ArtPiece, Category


class TestArtShop(TestCase):
    '''
    TODO:
        - Add tests for the following:
        - Models -> we only did the initial tests for the category model
        -- still need to test the art piece model
        - We need to add test for the schemas before we add anything else...
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


class GraphQLTestCase(GraphQLTestCase):
    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(name='Test Category')
        self.art_piece = ArtPiece.objects.create(
            name='Test Art Piece',
            description='Test Description',
            category=self.category,
            price=100.00)

    def test_some_randomness(self):
        self.assertEqual(2 + 2, 4)

    def test_query_art_piece_basic_query(self):
        return_query = self.query('''
            query {
                artPieces {
                    id,
                    name,
                    description,
                    price
                }
            }
            ''')
        expected_result = {
            'data': {
                'artPieces': [{
                    'id': '1',
                    'name': 'Test Art Piece',
                    'description': 'Test Description',
                    'price': '100.00'
                }]
            }
        }
        self.assertResponseNoErrors(return_query)
        self.assertJSONEqual(return_query.content, expected_result)

    def test_query_category_by_name(self):
        return_query = self.query('''
            query {
                categoryByName(name: "Test Category") {
                    id,
                    name
                }
            }
            ''')
        expected_result = {
            'data': {
                'categoryByName': {
                    'id': '1',
                    'name': 'Test Category'
                }
            }
        }
        self.assertResponseNoErrors(return_query)
        self.assertJSONEqual(return_query.content, expected_result)

    def test_query_art_pieces_by_name(self):
        return_query = self.query('''
            query {
                artPiecesByName(name: "Test Art Piece") {
                    id,
                    name,
                    description,
                    price
                }
            }
            ''')
        expected_result = {
            'data': {
                'artPiecesByName': [{
                    'id': '1',
                    'name': 'Test Art Piece',
                    'description': 'Test Description',
                    'price': '100.00'
                }]
            }
        }
        self.assertResponseNoErrors(return_query)
        self.assertJSONEqual(return_query.content, expected_result)

    def tearDown(self):
        '''Clean up purposes'''
        self.category.delete()
        self.art_piece.delete()
