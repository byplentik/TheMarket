# TheMarket

TheMarket is a personal project created to showcase my knowledge in Django and related libraries. The project is a web application that allows users to view products, leave reviews and ratings, and more. 

I still haven't finished this project, at least I still need to make a shopping cart. 

## Technologies Used

TheMarket is built with Django and several libraries, including:
- django-allauth for user authentication
- django-crispy-forms and crispy-bootstrap5 for styling
- environs[django] for managing environment variables
- psycopg2-binary for working with PostgreSQL
- pillow for image processing
- coverage for testing coverage
- docker, docker-compose
- and others

## Running TheMarket Locally

To run TheMarket locally, you'll need to have Docker installed on your machine. Once you have Docker installed, you can run the following commands:

    # 1. Clone the repository:
    git clone https://github.com/byplentik/django-api.git

    # 2. Create a virtual environment:
    py -m venv venv
    cd venv/scripts/activate

    # 3. Install the required libraries:
    pip install -r requirements.txt

    # 4. Build and run the Docker containers:
    docker-compose up -d --build

    # 5. Apply database migrations:
    docker-compose exec web python manage.py migrate

This will start a container for the PostgreSQL database, as well as a container for the Django web server. Once the containers are up and running, you can visit http://localhost:8000 to view the site.

### Database setup

By default, TheMarket is configured to use PostgreSQL as the database. When you run `docker-compose up --build`, Docker will automatically start a container for the PostgreSQL database and create a new database called `themarket`. 

If you need to create a superuser to access the Django admin interface, you can do so by running the following command:
    
    docker-compose exec web python manage.py createsuperuser




    