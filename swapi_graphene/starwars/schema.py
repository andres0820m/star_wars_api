# cookbook/ingredients/schema.py
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from .models import People, Planet, Film


class PeopleNode(DjangoObjectType):
    class Meta:
        model = People


class PlanetNode(DjangoObjectType):
    class Meta:
        model = Planet


class FilmNode(DjangoObjectType):
    class Meta:
        model = Film


class Query(ObjectType):
    people = graphene.Field(PeopleNode, name=graphene.String())
    all_people = graphene.List(PeopleNode)
    all_planets = graphene.List(PlanetNode)
    film = graphene.List(FilmNode, characters=graphene.String())

    # people_filter = DjangoFilterConnectionField(PeopleNode)

    def resolve_all_planets(self, info, **kwargs):
        return Planet.objects.select_related('name').all()

    def resolve_all_people(self, _, __):
        return People.objects.all()

    def resolve_people(self, _, **kwargs):
        name = kwargs.get('name')
        if name is not None:
            return People.objects.get(name=name)

    def resolve_film(self, _, **kwargs):
        character = People.objects.get(name=kwargs.get('characters'))
        return Film.objects.filter(characters=character)
