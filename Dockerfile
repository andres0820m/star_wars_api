FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/local/src/star_wars_api
WORKDIR /usr/local/src/star_wars_api
COPY requirements.txt /usr/local/src/star_wars_api
RUN pip install -r requirements.txt
COPY . /usr/local/src/star_wars_api

RUN chmod +x /usr/local/src/star_wars_api/swapi_graphene/entrypoint.sh
ENTRYPOINT ["/usr/local/src/star_wars_api/swapi_graphene/entrypoint.sh"]

