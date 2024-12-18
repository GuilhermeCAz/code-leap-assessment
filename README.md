# CodeLeap Assessment

This is a simple Django REST Framework-based application that allows users to perform CRUD operations (Create, Read, Update, Delete) on posts. This API is designed to be used for a technical test at CodeLeap and serves as a basic demonstration of RESTful design with Django and Django REST Framework (DRF).

## Project Overview

This project provides an API for managing posts. The API allows users to:

- View a list of posts.
- Create a new post.
- Update or partially update an existing post.
- Delete a post.

The API is structured to follow standard RESTful principles and uses JSON as the data format for requests and responses.

## Deployment

This project has been deployed on PythonAnywhere for live usage. You can access the API here:

<http://guilhermecaz.pythonanywhere.com>

## API Usage

You can interact with the API using the following cURL commands (replace the your_token with your actual API token if needed):

1. GET request (Retrieve the list of posts)

   ```bash
   curl -X GET http://guilhermecaz.pythonanywhere.com/
   ```

2. POST request (Create a new post)

   ```bash
   curl -X POST http://guilhermecaz.pythonanywhere.com/ \
     -H "Content-Type: application/json" \
     -d '{"title": "New Post", "content": "This is the content of the new post."}'
   ```

3. PUT request (Update an existing post with ID 1)

   ```bash
   curl -X PUT http://guilhermecaz.pythonanywhere.com/1/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Post", "content": "This is the updated content of the post."}'
   ```

4. PATCH request (Partially update an existing post with ID 1)

   ```bash
   curl -X PATCH http://guilhermecaz.pythonanywhere.com/1/ \
     -H "Content-Type: application/json" \
     -d '{"content": "This is the partially updated content of the post."}'
   ```

5. DELETE request (Delete the post with ID 1)

   ```bash
   curl -X DELETE http://guilhermecaz.pythonanywhere.com/1/
   ```

## Installation

Follow the steps below to set up the project locally:

### Prerequisites

- Python 3.10 or higher
- pip or uv

### Step 1: Clone the repository

```bash
git clone https://github.com/GuilhermeCAz/codeleap-assessment.git
cd codeleap-assessment
```

### Step 2: Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set up the database

Run migrations to set up the database:

```bash
python manage.py migrate
```

### Step 6: Run the development server

```bash
python manage.py runserver
```

Your API should now be accessible at <http://127.0.0.1:8000>.

## Run tests

To test the API, you can use the cURL commands as described above. Additionally, there are some tests included in [posts/tests.py](posts/tests.py). To run tests for the project:

```bash
python manage.py test posts
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
