# Blog_Django

This is a Django-based blog application.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (registration, login, logout)
- Article management (create, view, categorize)
- Commenting on articles
- Article voting system
- Pagination for article listings
- Admin interface for managing content

## Setup

To get this project up and running on your local machine, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Blog_Django.git
cd Blog_Django
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your superuser account.

## Usage

### 1. Run the development server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

### 2. Access the Admin Panel

You can access the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials you created.

## Project Structure

- `article/`: Django app for managing articles, categories, comments, and votes.
- `blog/`: Main blog application, handling overall site views like homepage, about, and contact.
- `user_account/`: Django app for user registration, login, and logout.
- `templates/`: Contains base HTML templates.
- `media/`: Stores uploaded media files (e.g., article images).
- `db.sqlite3`: SQLite database file (used in development).
- `manage.py`: Django's command-line utility for administrative tasks.
- `weblog/`: The main Django project configuration directory.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your branch to your fork.
5. Submit a pull request.

## License

This project is licensed under the MIT License.
