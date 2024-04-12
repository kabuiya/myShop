[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/3WDH8NqBWqqcfhediMABwD/DSWZkYA96p3DdnKNskisfW/tree/main.svg?style=svg&circle-token=CCIPRJ_B49sDhqw2cCUWV1eYoGkWm_1454834b7b5c2c39d9906c76ddba969ed8f14fc3)](https://dl.circleci.com/status-badge/redirect/circleci/3WDH8NqBWqqcfhediMABwD/DSWZkYA96p3DdnKNskisfW/tree/main)
[![Coverage Status](https://coveralls.io/repos/github/kabuiya/myShop/badge.svg)](https://coveralls.io/github/kabuiya/myShop)

# My Shop - Simple E-commerce Website

Welcome to My Shop! My Shop is a simple e-commerce website where users can register, log in, add items to their cart, remove items from their cart, and place orders.

## Features

- **User Registration:** Users can create an account to access the full functionality of the website.
- **User Authentication:** Registered users can log in to their accounts securely.
- **Product Catalog:** Users can browse through the available products in the catalog.
- **Add to Cart:** Logged-in users can add items to their cart for later purchase.
- **Remove from Cart:** Users can remove items from their cart if they no longer wish to purchase them.
- **Cart Management:** Users cannot add items to the cart while not logged in. Additionally, users cannot navigate to the cart page if they haven't added any items to their cart.
- **Place Order:** Users can place orders for the items in their cart.
- **Payment:** Payment is only accepted on delivery, providing a seamless checkout experience for users.

## Technologies Used

### Frontend:
- HTML
- JavaScript
- Bootstrap

### Backend:
- Django (Python)
- PostgreSQL (Database)

## Getting Started

To run My Shop locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/my-shop.git
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the PostgreSQL database:** You'll need to have PostgreSQL installed and running on your machine. Update the database settings in `settings.py` with your PostgreSQL credentials.

4. **Apply migrations to create the necessary database schema:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access My Shop:** Open your web browser and navigate to `http://localhost:8000`.
7. **To run tests:** `python manage.py test`
8. **Run tests with coverage and generate coverage report:** 
   ```bash
   coverage run manage.py test
   coverage report -m
   ```

## Contributing

Contributions are welcome! If you'd like to contribute to My Shop, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).


