# cookbook/ingredients/schema.py
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from .models import People, Planet, Film
from graphene_django.rest_framework.mutation import SerializerMutation
from .serializers import PeopleSerializer


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

    def resolve_all_people(self, _, **kwargs):
        return People.objects.all()

    def resolve_people(self, _, **kwargs):
        name = kwargs.get('name')
        if name is not None:
            return People.objects.get(name=name)

    def resolve_film(self, _, **kwargs):
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

    def mutate(self, _, name, homeworld, height="", mass="", hair_color="", skin_color="", eye_color="",
               birth_year="", gender=""):
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

    def mutate(self, _, name, rotation_period="", orbital_period="", diameter="", climate="", gravity="", terrain="",
               surface_water="", population=""):
        Planet(name=name,
               rotation_period=rotation_period,
               orbital_period=orbital_period,
               diameter=diameter,
               climate=climate,
               gravity=gravity,
               terrain=terrain,
               surface_water=surface_water,
               population=population
               ).save()


class CreateFilm(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    characters = graphene.Field(PeopleNode)

    class Arguments:
        title = graphene.String()
        characters = graphene.String()

    def mutate(self, _, title: str, characters: str):
        total = []
        persons = characters.split(',')
        for person in persons:
            print(person)
            total.append(People.objects.get(name=person))
        Film(
            title=title,
            characters=total
        )


class Mutation(graphene.ObjectType):
    create_people = CreatePeople.Field()
    create_planet = CreatePlanets.Field()
    create_movie = CreateFilm.Field()
