# Rick and Morty API Project

A Django-based project that integrates with the [Rick and Morty API](https://rickandmortyapi.com/).  
The application allows fetching and storing characters in a PostgreSQL database and uses Celery with Redis for asynchronous task processing.

---

## Features
- Django backend with PostgreSQL.
- Integration with the external Rick and Morty API.
- Celery workers for background jobs.
- Redis as a message broker and results backend.
- Database migrations with Django ORM.

---

## Requirements
- Python 3.9+
- PostgreSQL
- Redis
- Virtual environment (recommended)

---

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/rick_and_morty_api.git
   cd rick_and_morty_api


2. **Create and activate a virtual environment**
   ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Linux/Mac
    .venv\Scripts\activate      # On Windows

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    Configure environment variables
    Create a .env file in the project root. Use .env.example as a reference.

4. **Run database migrations**
   ```bash
   python manage.py migrate

5. **Start the development server**
    ```bash
    python manage.py runserver

6. **Celery Setup**
    ```bash
    Start Redis and Celery worker:
    celery -A rick_and_morty worker -l INFO
