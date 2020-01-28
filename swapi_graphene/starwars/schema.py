# cookbook/ingredients/schema.py
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from .models import People, Planet


class PeopleNode(DjangoObjectType):
    class Meta:
        model = People
        filter_fields = ['name', 'mass', 'homeworld']
        interfaces = (relay.Node,)


class PlanetNode(DjangoObjectType):
    class Meta:
        model = Planet
        filter_fields = ['name']
        interfaces = (relay.Node,)


class Query(ObjectType):
    people = relay.Node.Field(PeopleNode)
    all_people = graphene.List(PeopleNode)
    all_planets = graphene.List(PlanetNode)
    people_filter = DjangoFilterConnectionField(PeopleNode)

    def resolve_all_planets(self, info, **kwargs):
        return Planet.objects.select_related('name').all()

    def resolve_all_people(self, info, **kwargs):
        return People.objects.all()
