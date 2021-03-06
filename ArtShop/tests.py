import json
from django.http import response

from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from .models import ArtPiece, Category


class TestArtShop(TestCase):
    '''
    TODO:
        - Add tests for the following:
        - Models -> we only did the initial tests for the category model: DONE
        - We need to add test for the schemas before we add anything else:DONE
        - Add mutations to the schema:DONE for now...
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

    def test_category_name_is_valid_true(self):
        test_category = Category.objects.filter(name='Test Category')
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


class GraphQLTestCaseQueries(GraphQLTestCase):
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

    def test_query_category_by_name_fail(self):
        return_query = self.query('''
            query {
                categoryByName(name: "Test False") {
                    id,
                    name
                }
            }
            ''')
        expected_result = {'data': {'categoryByName': None}}
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

    def test_query_art_pieces_by_name_fail(self):
        return_query = self.query('''
            query{
                artPiecesByName(name: "Test Fail") {
                        id,
                        name,
                        description,
                        price
                    }
            }
            ''')
        expected_result = {'data': {'artPiecesByName': []}}
        self.assertResponseNoErrors(return_query)
        self.assertJSONEqual(return_query.content, expected_result)

    '''
    TODO:
        - artPiecesByCategory is the next test
        - Before writing this test we need to fix the resolver for this method; returns all categories instead of the one that matches the string
    '''

    def test_query_art_pieces_by_category(self):
        return_query = self.query('''
            query {
                artPiecesByCategory(name: "Test Category") {
                    id,
                    name,
                    description,
                    price
                }
            }
            ''')
        expected_result = {
            'data': {
                'artPiecesByCategory': [{
                    'id': '1',
                    'name': 'Test Art Piece',
                    'description': 'Test Description',
                    'price': '100.00'
                }]
            }
        }
        self.assertResponseNoErrors(return_query)
        self.assertJSONEqual(return_query.content, expected_result)

    def test_query_art_pieces_by_category_fail(self):
        return_query = self.query('''
            query {
                artPiecesByCategory(name: "Test False") {
                    id,
                    name,
                    description,
                    price
                }
            }
            ''')
        expected_result = {'data': {'artPiecesByCategory': []}}
        self.assertResponseNoErrors(return_query)
        self.assertJSONEqual(return_query.content, expected_result)

    def tearDown(self):
        '''Clean up purposes'''
        self.category.delete()
        self.art_piece.delete()


class GraphQLTestCaseMutations(GraphQLTestCase):
    '''
        TODO: start writing the test for the mutations
            - createArtPiece
    '''
    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(name='Test Category')
        self.art_piece = ArtPiece.objects.create(
            name='Test Art Piece',
            description='Test Description',
            category=self.category,
            price=100.00)

    def test_create_art_piece(self):
        return_query = self.query('''
            mutation {
                createArtPiece(name:"big booty judy", description:"Oh so big", price: "12.50", category:"NSFW"){
                    artPiece{
                    id,
                    name,
                    description,
                    price,
                    category{
                        id,
                        name
                    }
                        }
                    }
            }
                ''')
        expected_result = {
            'data': {
                'createArtPiece': {
                    'artPiece': {
                        'id': '2',
                        'name': 'big booty judy',
                        'description': 'Oh so big',
                        'price': '12.50',
                        'category': {
                            'id': '2',
                            'name': 'NSFW'
                        }
                    }
                }
            }
        }
        self.assertResponseNoErrors(return_query)
        self.assertJSONEqual(return_query.content, expected_result)

    def test_create_art_piece_fail(self):
        #Writing to see if someone inputs a wrong value into the mutation that it fails. eg. price being 12.50 instead of "12.50"
        return_query = self.query('''
            mutation {
                createArtPiece(name:"big booty judy", description:"Oh so big", price: 12.50, category:"NSFW"){
                    artPiece{
                    id,
                    name,
                    description,
                    price,
                    category{
                        id,
                        name
                    }
                        }
                    }
            }
                ''')
        expected_result = {'data': {'createArtPiece': {'artPiece': None}}}
        self.assertResponseHasErrors(return_query)

    def test_update_art_piece(self):
        '''
        TODO:  
            - For tomorrow check the mutation we wrote for the updateArtPiece. Code may need 
            to be changed.
            - Update the mutation to update the art piece
        '''
        pass

    def test_delete_art_piece(self):
        return_query = self.query('''
            mutation {
                deleteArtPiece(id: 1){
                    artPiece{
                    id,
                    name,
                    description,
                    price,
                    category{
                        id,
                        name
                    }
                        }
                    }
            }
                ''')
        expected_result = {'data': {'deleteArtPiece': {'artPiece': None}}}
        self.assertResponseNoErrors(return_query)
        self.assertJSONEqual(return_query.content, expected_result)

    def test_delete_art_piece_fail(self):
        '''
        WARNING:
            - This test is working since the return response has errors but, 
                when the test in ran more than likely you will get an cmd line error 
        '''
        return_query = self.query('''
            mutation {
                deleteArtPiece(id: 20){
                    artPiece{
                    id,
                    name,
                    description,
                    price,
                    category{
                        id,
                        name
                    }
                        }
                    }
            }
                ''')
        self.assertResponseHasErrors(return_query)

    def tearDown(self):
        '''Clean up purposes'''
        self.category.delete()
        self.art_piece.delete()