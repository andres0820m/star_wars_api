import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from graphene_django_extras import DjangoSerializerMutation

from .models import People, Planet, Film
from .serializers import FilmSerializer

_USE_AUTH = False


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

    def resolve_all_people(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous and _USE_AUTH:
            raise Exception('Not logged!')
        return People.objects.all()

    def resolve_people(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous and _USE_AUTH:
            raise Exception('Not logged!')
        name = kwargs.get('name')
        if name is not None:
            return People.objects.get(name=name)

    def resolve_film(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous and _USE_AUTH:
            raise Exception('Not logged!')
        character = People.objects.get(name=kwargs.get('characters'))
        return Film.objects.filter(characters=character)


class CreatePeople(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    height = graphene.String()
    mass = graphene.String()
    hair_color = graphene.String()
    skin_color = graphene.String()
    eye_color = graphene.String()
    birth_year = graphene.String()
    gender = graphene.String()
    homeworld = graphene.Field(PlanetNode)

    class Arguments:
        name = graphene.String()
        height = graphene.String()
        mass = graphene.String()
        hair_color = graphene.String()
        skin_color = graphene.String()
        eye_color = graphene.String()
        birth_year = graphene.String()
        gender = graphene.String()
        homeworld = graphene.String()

    def mutate(self, info, name, homeworld, height="", mass="", hair_color="", skin_color="", eye_color="",
               birth_year="", gender=""):
        user = info.context.user
        if user.is_anonymous and _USE_AUTH:
            raise Exception('Not logged!')
        home_id = Planet.objects.get(name=homeworld)
        people = People(
            name=name,
            height=height,
            mass=mass,
            hair_color=hair_color,
            skin_color=skin_color,
            eye_color=eye_color,
            birth_year=birth_year,
            gender=gender,
            homeworld=home_id
        )
        people.save()
        return people


class CreatePlanets(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    rotation_period = graphene.String()
    orbital_period = graphene.String()
    diameter = graphene.String()
    climate = graphene.String()
    gravity = graphene.String()
    terrain = graphene.String()
    surface_water = graphene.String()
    population = graphene.String()

    class Arguments:
        name = graphene.String()
        rotation_period = graphene.String()
        orbital_period = graphene.String()
        diameter = graphene.String()
        climate = graphene.String()
        gravity = graphene.String()
        terrain = graphene.String()
        surface_water = graphene.String()
        population = graphene.String()

    def mutate(self, info, name, rotation_period="", orbital_period="", diameter="", climate="", gravity="", terrain="",
               surface_water="", population=""):
        user = info.context.user
        if user.is_anonymous and _USE_AUTH:
            raise Exception('Not logged!')
        planet = Planet(name=name,
                        rotation_period=rotation_period,
                        orbital_period=orbital_period,
                        diameter=diameter,
                        climate=climate,
                        gravity=gravity,
                        terrain=terrain,
                        surface_water=surface_water,
                        population=population
                        )
        planet.save()
        return planet


class FilmSerializerMutation(DjangoSerializerMutation):
    class Meta:
        description = " DRF serializer based Mutation for Users "
        serializer_class = FilmSerializer


class Mutation(graphene.ObjectType):
    create_people = CreatePeople.Field()
    create_planet = CreatePlanets.Field()
    film_create = FilmSerializerMutation.CreateField()
    film_delete = FilmSerializerMutation.DeleteField()
    film_update = FilmSerializerMutation.UpdateField()
