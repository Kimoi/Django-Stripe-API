
# Django-Stripe-API

**Integrating a payment system in Django using Stripe**

## We Did It List:

- Item model
- GET /buy/{id}
- GET /item/{id}
- Environment variables
- Application is fully Dockerized
- View Django Models in Django Admin panel
- Order model

## Local Deployment (give it a try &#9889;):

- Clone repo
- Create `.env` file in `manage.py` directory
- Copy the code up next and fill it with your own data

```bash
SECRET_KEY = YOUR_DATA_HERE
DEBUG = AND_HERE

STRIPE_PUBLISHABLE_KEY = AND_HERE
STRIPE_SECRET_KEY = AND_HERE

DB_ENGINE = AND_HERE
DB_NAME = 'AND_HERE_BUT_IN_QUOTES'
POSTGRES_USER = 'IN_QUOTES_ALSO'
POSTGRES_PASSWORD = 'THE_LAST_ONE_WITH_QUOTES'
DB_HOST = YOUR_DATA_HERE
DB_PORT = AND_HERE
YOU_ARE = 'AMAZING!'
```

- Next up - we spin up the container

```commandline
docker-compose up -d --build
```

- Migrate tables

```commandline
docker-compose exec web python manage.py migrate
```

- Create superuser

```commandline
docker-compose exec web python manage.py createsuperuser
```

- YOU ARE AMAZING! &#9889;