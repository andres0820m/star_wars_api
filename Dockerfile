FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/local/src/aforos-api
WORKDIR /usr/local/src/aforos-api
COPY requirements.txt /usr/local/src/aforos-api
RUN pip install -r requirements.txt
COPY . /usr/local/src/aforos-api

RUN chmod +x /usr/local/src/aforos-api/api/entrypoint.sh
ENTRYPOINT ["/usr/local/src/aforos-api/api/entrypoint.sh"]
