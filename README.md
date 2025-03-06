# User Authentication System

This project is a Django-based User Authentication System with role-based access control (RBAC). It ensures that newly registered users cannot access any pages until an admin assigns them a role. Each user is redirected to different pages based on their assigned role after logging in.

## Features
- User authentication (signup, login, logout)
- Role-based access control (RBAC)
- SQLite database support
- Template-based UI for authentication pages

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- pip (Python package manager)

### Steps to Install and Run
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/user-authentication-system.git
   cd user-authentication-system/User
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin user.

6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage
- New users must sign up.
- An admin must assign roles to new users via the Django admin panel (`/admin`).
- Users are redirected based on their assigned roles after logging in.

## Folder Structure
```
User/
│── app1/       # Django app 1
│── app2/       # Django app 2
│── app3/       # Django app 3
│── app4/       # Django app 4
│── templates/  # HTML templates
│── manage.py   # Django management script
│── requirements.txt # Project dependencies
│── db.sqlite3  # SQLite database file
```

## Contributing
Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.
