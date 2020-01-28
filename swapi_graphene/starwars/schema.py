# cookbook/ingredients/schema.py
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import People


class PeopleNode(DjangoObjectType):
    class Meta:
        model = People
        filter_fields = ['name', 'mass']
        interfaces = (relay.Node,)


class Query(ObjectType):
    people = relay.Node.Field(PeopleNode)
    all_people = DjangoFilterConnectionField(PeopleNode)
