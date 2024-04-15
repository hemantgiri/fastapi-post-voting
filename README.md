# FastAPI PostgreSQL CRUD Project

This project is a demonstration of a FastAPI application with PostgreSQL database integration, including user authentication, CRUD operations for posts, and post voting functionality. It also includes automated tests using Pytest and database migrations managed by Alembic.

## Features

- User API authentication
- CRUD operations for posts
- Voting system for posts
- Pytest for automated testing
- Alembic for database migrations

## Installation

### Using Docker (Recommended)

1. Install Docker on your system if you haven't already. Refer to the [official Docker documentation](https://docs.docker.com/get-docker/) for installation instructions specific to your platform.

2. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    ```

3. Navigate to the project directory:

    ```bash
    cd yourproject
    ```

4. Create a `.env` file in the project directory with the following variables:

    ```plaintext
    DATABASE_HOSTNAME=localhost
    DATABASE_PORT=
    DATABASE_PASSWORD=
    DATABASE_NAME=
    DATABASE_USERNAME=
    SECRET_KEY=YOUR_SECRET_KEY_HERE
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=
    ```

    - Replace `YOUR_SECRET_KEY_HERE` with a securely generated secret key. You can generate one using :

    ```bash
        openssl rand -hex 32
        SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ```
    check this https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/ for more info.

5. Build the Docker image:

    ```bash
    docker build -t yourproject .
    ```

6. Run the Docker container:

    ```bash
    docker run -d --name container_name -p 8000:8000 image_name
    ```

7. Access the API at `http://localhost:8000`.

### Using Uvicorn (Development)

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    ```

2. Navigate to the project directory:

    ```bash
    cd yourproject
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Create a `.env` file in the project directory with the following variables:

    ```plaintext
    DATABASE_HOSTNAME=localhost
    DATABASE_PORT=
    DATABASE_PASSWORD=
    DATABASE_NAME=
    DATABASE_USERNAME=
    SECRET_KEY=YOUR_SECRET_KEY_HERE
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=
    ```

    - Replace `YOUR_SECRET_KEY_HERE` with a securely generated secret key. You can generate one using :

    ```bash
        openssl rand -hex 32
        SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ```
    check this https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/ for more info.

7. Start the Uvicorn server:

    ```bash
    uvicorn app.main:app --reload
    ```

8. Access the API at `http://localhost:8000`.

## Usage

Once the application is running, you can interact with the API endpoints using tools like cURL, Postman, or your preferred HTTP client.

## Testing

To run the automated tests:

1. Navigate to the project directory if you're not already there:

    ```bash
    cd yourproject
    ```

2. Run Pytest:

    ```bash
    pytest
    ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

