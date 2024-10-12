# Employee Management System

## Overview

This project is a Django-based Employee Management System that implements CRUD operations for employee records. The application allows users to manage employee data, including name, email, salary, and phone number. It also includes user authentication and utilizes JWT tokens for secure access.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete employee records.
- **User Authentication**: Login and signup functionality using JWT tokens.
- **Serializers**: Data validation and serialization using Django REST Framework.
- **Middleware**: Custom middleware to log requests for debugging purposes.
- **Database**: Utilizes PostgreSQL for efficient data management.
- **CI/CD Pipeline**: Set up using GitLab for automated testing and deployment.

## Requirements

1. Django Rest Framework
2. User login/signup functionality
3. Serializers for data handling
4. JWT Token authentication
5. Middleware implementation
6. PostgreSQL database (or your choice)
7. GitLab CI/CD pipeline setup (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gauravbarde55/employee_management.git
   cd employee_management

2. Create a virtual environment:

python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

3. Install the required packages:

pip install -r requirements.txt

4. Set up your PostgreSQL database and update the settings.py file with your database credentials.

5. Run migrations:

python manage.py migrate

6. Start the development server:

python manage.py runserver

Usage
Access the API at http://127.0.0.1:8000/api/employees/ for CRUD operations on employee records.
Use the /api/token/ endpoint to obtain JWT tokens for authentication.
Testing
Run the tests using:

python manage.py test employees

CI/CD Pipeline
The project includes a GitLab CI/CD pipeline configured in .gitlab-ci.yml to automate testing and deployment processes.
Contributing
Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.
License
This project is licensed under the MIT License - see the LICENSE file for details. Thank you for reviewing this assignment!
text

### Summary

This `README.md` file provides a comprehensive overview of your project, including installation instructions, features, and usage details. Feel free to customize it further based on your specific implementation or any additional features you may have added!
