from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase
from django.contrib.auth import get_user_model
from graphql_jwt.testcases import JSONWebTokenTestCase
from swapi_graphene.schema import schema


class UsersTests(JSONWebTokenTestCase, GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        self.user = get_user_model().objects.create(username='test')
        self.client.authenticate(self.user)

    def test_all_people(self):
        query = '''
        query{allPeople{name}}
        }'''

        self.client.execute(query)

    def test_people(self):
        query = '''
        query{
  people($name: String!){
    name
  }
        }'''

        variables = {
            'username': self.user.username,
        }

        executed = self.client.execute(query, variables)
        assert executed
