# Expense Tracker API

## Overview
The Expense Tracker API is a RESTful service that allows users to track their expenses. Users can sign up, log in, and manage their expenses with various functionalities such as listing, filtering, adding, retrieving, updating, and deleting expenses. 

## Features
- **User Authentication**
  - Sign up as a new user
  - Generate and validate JWT for authentication and user session
- **Expense Management**
  - List and filter past expenses
    - Past week
    - Last 3 months
    - Last month
    - Custom (choose start and end date)
  - Add new expenses
  - Retrieve existing expense
  - Remove existing expenses
  - Update existing expenses
- **Expense Categories**

### Prerequisites
- Python 3.x
- Django
- Django REST Framework
- djangorestframework-jwt

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/ladiyusuph/expense-tracker-api.git
    cd expense-tracker-api
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```


### Endpoints

#### Authentication
- **Sign Up**: `POST /api/signup/`
- **Log In**: `POST /api/login/`
  - Returns a JWT token for authenticated requests.

#### Expenses
- **List Expenses**: `GET /api/expenses/`
  - Query parameters for filtering (e.g., past week, last month, custom date range).
- **Add Expense**: `POST /api/expenses/`
- **Retrieve Expense**: `GET /api/expenses/<id>/`
- **Update Expense**: `PUT /api/expenses/<id>/`
- **Delete Expense**: `DELETE /api/expenses/<id>/`

### Authentication
All endpoints (except sign up and log in) require a valid JWT token in the `Authorization` header:
