# Social Network

## Technologies:
- python 3.10
- Django 4
- Django REST framework
- PostgreSQL
- Nginx
- Docker
- docker-compose

## Start project:

### by using docker on local server
- Run this command - it start project
```
docker-compose up --build
```

### by using docker on production server

- create `.env` file in main directory
```dotenv
SECRET_KEY=8fajd3)on9ecoq&&8__eryh-d5sz@6!8ky3+y0u5k6gw8!q$^t
DEBUG=0
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=postgres
```

- Run this command - it start project
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build
```


## License

This project is licensed under the terms of the MIT license.
