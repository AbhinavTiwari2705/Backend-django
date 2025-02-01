# Multilingual FAQ System

This project implements a multilingual FAQ system using Django, Django REST Framework, and CKEditor.

## Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:AbhinavTiwari2705/Backend-django.git
    cd faw-system
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.gitignore` file:
    ```sh
    touch .gitignore
    ```

5. Apply migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

1. Access the admin panel at `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

2. Add FAQ entries and manage content using the admin interface.

3. Access the FAQ system at `http://127.0.0.1:8000/`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License.

