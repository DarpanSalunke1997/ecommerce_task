# Ecommerce Application

This is an ecommerce application built with Django and Django REST Framework. The application includes product management, discount management, and order management features.

## Features

- Product Management:
  - Regular products
  - Seasonal products with seasonal discounts
  - Bulk products with bulk purchase discounts
- Discount Management:
  - Percentage-based discounts
  - Fixed amount discounts
- Order Management:
  - Calculate total price considering product types and discounts

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST Framework

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/ecommerce.git
    cd ecommerce
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create and configure the database:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Access the application:**
    - Open your web browser and go to `http://127.0.0.1:8000/admin` to access the admin panel.
    - API endpoints can be accessed at `http://127.0.0.1:8000/shop/api/`.


## Running Tests

To run the tests for the application, use the following command:

```sh
python manage.py test shop
