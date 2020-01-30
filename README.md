# star_wars_api
star wars api paras prueba en  lo que necesito

requisitos:
docker y docker-compose para iniciar de manera rapida 
instrucciones de instalacion :
linux
https://runnable.com/docker/install-docker-on-linux
windows
https://docs.docker.com/docker-for-windows/install/
docker compose:
https://docs.docker.com/compose/install/

existen dos métodos para arrancar la api, uno en el cual se requiere de autentificación para poder hacer mutaciones y querys, por defecto esta desactivado, para activarlo dentro del folder star_wars_api/swapi_graphene/starwars en el archivo schema.py se encuentra una constante llamada _USE_AUTH = False, cambiar a True para activar la autentificación.

después de escoger el modo en el cual se ejecutara la aplicación la forma mas fácil de arrancarla es ejecutando dentro de la raíz del proyecto en la terminal de linux o power shell de windows:
docker-compose up --build
![image](https://user-images.githubusercontent.com/30030792/73417181-36a5c900-42e5-11ea-8ee9-2a7a4901f4bb.png)

se construirá una base de datos en posgres en el puerto 5434, cambiar el puerto en el docker-compose-yml de ser necesario.

al finalizar se tendrá construida y andando la api lista para recibir peticiones. para este caso en : http://localhost:8000/graphql "si se encuentran activas las autentificaciones probar desde postman o insomnia ya que es requerido el token de autentificación en los headers de la petición"
la información de las películas fue tomada del siguiente repositorio: https://github.com/phalt/swapi el cual cuenta con la siguiente api hecha en django-rest-framework :https://swapi.co/ toda la información de los personajes películas que se encuentra en api en los campos disponibles para los querys y las mutaciones esta disponible.
las querys disponibles son:
people
allPeople
film
los cuales funcionan de la siguiente manera:
## people:
people entrega la información de un personaje de la saga filtrando por su nombre, como se menciono arriba, todos los campos disponibles en en swapi pueden ser consultados.
un ejemplo de uso:
![image](https://user-images.githubusercontent.com/30030792/73417095-e7f82f00-42e4-11ea-97ae-7c154b2ce4bd.png)

## allpeople:
allpeople entrega todos los personajes que se encuentren registrados en la base datos, junto con toda la información de los mismos, aquí un ejemplo de como hacer la consulta:
![image](https://user-images.githubusercontent.com/30030792/73417344-c3e91d80-42e5-11ea-863f-de6d4a864fd2.png)

## film:

film entrega la información de las películas filtrada por personajes en caso de que se quiera saber las películas en las cuales este personaje a participado. un ejemplo de uso:
![image](https://user-images.githubusercontent.com/30030792/73417664-e6c80180-42e6-11ea-823c-8bb2188f793f.png)

las mutaciones disponibles son:
createpeople
createplanet
filmcreate
los cuales funcionan de la siguiente manera:
## createpeople:
sirve para crear personajes en la base de datos los campos requeridos son name, homeworld, un ejemplo de uso:
![image](https://user-images.githubusercontent.com/30030792/73417967-ea0fbd00-42e7-11ea-94d8-5788df4e9ee0.png)
 nota: se pueden agregar todos los otros campos 
## createplanet:
sirve para crear planetas en la base de datos el campo requerido es name, un ejemplo de uso:
![image](https://user-images.githubusercontent.com/30030792/73418110-699d8c00-42e8-11ea-8ca3-d44e76e03a0b.png)
nota: se pueden agregar todos los otro campos, solo es obligatorio el nombre
## filmcreate:
se usa para crear películas en la base de datos, los campos requeridos son: 
title,director,episodeId,openingCrawl,producer,releaseDate los demas campos que son relaciones se pueden llenar con el id al de quetenecen como en el ejemplo:
![image](https://user-images.githubusercontent.com/30030792/73418870-1e38ad00-42eb-11ea-887a-332490d21874.png)

apartese encueran las mutaciones para crear un usuario y para general y obtener los tokens, estas son:
## createuser:
sirve para crear un nuevo usuario. ejemplo de uso:
![image](https://user-images.githubusercontent.com/30030792/73419151-14fc1000-42ec-11ea-8f2e-fd2ac50ed40a.png)

## tokenAuth:
crea el token de autentificación necesario para poder consultar o hacer cambios en la base de datos si esta activa la autentificación. ejemplo de uso:
![image](https://user-images.githubusercontent.com/30030792/73419265-74f2b680-42ec-11ea-8d01-1725034c198c.png)

en casi de que se active la autentificación, crear primero un usuario luego obtener el token y en los headers de la peticion agregar el campo: Authorization con el valor JWT + el token como se muestra:
![image](https://user-images.githubusercontent.com/30030792/73419466-3ad5e480-42ed-11ea-9f84-795b9c7a4b3b.png)

después de esto ya se pueden hacer las peticiones pertinentes.
