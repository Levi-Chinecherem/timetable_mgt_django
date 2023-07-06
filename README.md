
# Timetable Management System with Django
![Sample Image](https://github.com/Levi-Chinecherem/timetable_mgt_django/blob/master/sample.PNG)

## Overview
This is a web application built with Django, a high-level Python web framework. It provides a platform for managing timetables, courses, and lecturers.

## Features
- View timetables based on selected level and semester
- Add, edit, and delete courses
- Add, edit, and delete lecturers
- User authentication and authorization

## Technologies Used
- Django 3.2.7
- Python 3.9.6
- HTML/CSS
- JavaScript
- SQLite database

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Levi-Chinecherem/timetable_mgt_django.git
   ```
2. Navigate to the project directory:
   ```
   cd django-project
   ```
3. Create a virtual environment:
   ```
   python -m venv env
   ```
4. Activate the virtual environment:
   - Windows:
     ```
     env\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source env/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
6. Run database migrations:
   ```
   python manage.py migrate
   ```
7. Start the development server:
   ```
   python manage.py runserver
   ```
8. Access the application in your web browser at `http://localhost:8000`

## Usage
1. Create a superuser account:
   ```
   python manage.py createsuperuser
   ```
2. Start the development server:
   ```
   python manage.py runserver
   ```
3. Log in to the admin panel at `http://localhost:8000/admin` using the superuser credentials.
4. Manage timetables, courses, and lecturers through the admin panel.
5. Access the main application at `http://localhost:8000` to view timetables and perform other actions.

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! Please follow the [contributing guidelines](CONTRIBUTING.md).

## Support
For any issues or questions, please open an [issue](https://github.com/Levi-chinecherem/django-project/issues).

Dont forget to give me credit if you ever use any part of this project

## Acknowledgements
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Font Awesome Icons](https://fontawesome.com/icons)
