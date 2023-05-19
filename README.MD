# URL Shortener
[![Coverage Report](https://img.shields.io/badge/coverage-98%25-green)](https://github.com/martynawitkowska/url_shortener/blob/main/media/coverage_report.png)
[![Beerware License](https://img.shields.io/badge/license-Beerware-yellowgreen)](https://github.com/martynawitkowska/url_shortener/blob/main/LICENSE)

A Django URL shortener app is a web application that generates short, customized links that redirect to longer URLs. It uses Django and a database to store original and short URLs, and may incorporate third-party services for URL shortening. The app is useful for simplifying the sharing of links online.

## Tech Stack

**Server:** Python, Django, Django Rest Framework, Pytest, Docker, Postgres


## Run Locally

Clone the project

```bash
  git clone git@github.com:martynawitkowska/url_shortener.git
```

Go to the project directory

```bash
  cd url_shortener
```

Set environmental variables

[Instructions for setting variables](#environment-variables)

```bash
  cp ./envs/api.default.env ./envs/api.env
  cp ./envs/postgres.default.env ./envs/postgres.env
  # set variable values
```

Start Docker Containers

```shell
  docker compose up
```

Load test data

```shell
docker compose exec api python manage.py loaddata fixtures/test_links.json
```

Go to your client and type 
```shell
    http://0.0.0.0:8000/api/schema/swagger-ui/
```

Here are links from test data file that you can visit:

http://0.0.0.0:8000/Nhd8rcbaSYUBhJKLq9fiGQ
http://0.0.0.0:8000/fdMYv5SadxMZ8TrEzfR3y9
http://0.0.0.0:8000/4KosSjJwwdXgT49pGWuARc

## Environment Variables

To run this project, you will need to add the following environment variables to your ./envs/api.env file

```dotenv
DJ_SECRET_KEY= # Django Secret Key for CSRF link
DJ_DEBUG= # Production development mode
DJ_ALLOWED_HOSTS= # Allowed Hosts for Django

DJ_SU_NAME= # Default superusername
DJ_SU_EMAIL= # Default superuser email
DJ_SU_PASSWORD= # Default superuser password
```

Generating DJ_SECRET_KEY in console or here [secret key generator](https://djecrety.ir/):

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

Postgres variables ./envs/postgres.env

```dotenv
POSTGRES_USER= # Postgres root user
POSTGRES_PASSWORD= # Postgres root password
POSTGRES_DB= # Database name
POSTGRES_HOST= # Database host: set to docker compose swervice name
POSTGRES_PORT= # Database port

DB_CONNECTION_STRING=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```


## Running Tests

To run tests, run the following command

```bash
  docker compose exec api pytest
```

## Authors

- [@martynawitkowska](https://github.com/martynawitkowska)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/martynawitkowska)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/martyna-witkowska-3b101684/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Martyna49841010)
