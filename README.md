
# Django-Stripe-API

**Integrating a payment system in Django using Stripe**

## Done:

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
- Copy the code up next and fill it with your own data. You may wipe
the whole "DB" section to use default values

```bash
SECRET_KEY = YOUR_DATA_HERE_IS_MUST

STRIPE_PUBLISHABLE_KEY = YOUR_DATA_HERE_IS_MUST
STRIPE_SECRET_KEY = YOUR_DATA_HERE_IS_MUST

DB_ENGINE = 
DB_NAME = ''
POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
DB_HOST = 
DB_PORT = 
```

- Next up - we spin up the container

```commandline
docker-compose up -d --build
```

- Make migrations and apply them

```commandline
docker-compose exec web python manage.py makemigrations
```

```commandline
docker-compose exec web python manage.py migrate
```

- Create superuser

```commandline
docker-compose exec web python manage.py createsuperuser
```
