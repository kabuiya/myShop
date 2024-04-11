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

## Contributing

Contributions are welcome! If you'd like to contribute to My Shop, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).


## Project Tasks.

# User Registration 
    Design user registration form.
    1.Implement server-side validation for registration inputs (e.g., email validation, password strength).
    2.Implement database storage for user registration data.
    3.Create frontend validation for registration form.
    4.Implement registration endpoint on the server.

# User Login:

    1.Design login form.
    2.Implement server-side validation for login credentials.
    3.Implement authentication mechanism (e.g., sessions, JSON Web Tokens).
    4.Create frontend validation for login form.
    5.Implement login endpoint on the server.

# User Logout:
    1.1mplement logout functionality on the frontend.
    2.Destroy user session on the server.
    3.Redirect user to appropriate page after logout.


# Delete Account:

    1.design delete account functionality.
    2.Implement server-side logic to delete user account.
    3.Implement frontend confirmation modal for account deletion

# Update User Details:

    1,Design user profile page.
    2.Implement form for updating user details.
    3.Implement server-side logic to update user details.
    4.Implement frontend validation for user details update form.

# Display Items:

    1.Design product listing page.
    2.Fetch fruit items data from the database.
    3.Implement pagination or infinite scroll for large datasets.
    4.Display items with relevant information (e.g., name, price, image, description).

# Add to Cart:

    1.Design "Add to Cart" button on product listing page.
    2.Implement server-side logic to handle adding items to the cart.
    3.Update cart data in the database.
    4.Implement frontend functionality to add items to the cart.

# View Cart:

    1.Design cart page.
    2.Fetch cart items data from the database.
    3.Implement logic to prevent viewing the cart if no items are added.
    4.Display cart items with relevant information (e.g., name, price, quantity, cart_total).

# Checkout:

    Design checkout page.
    Calculate total price based on items in the cart.
    Implement server-side logic for processing orders.
    Update inventory after successful order placement.

# Authentication Middleware:

    Implement middleware to check if the user is logged in for certain routes (e.g., add to cart, view cart).
    Redirect users to login page if they try to access restricted pages without authentication.

# Adding/Removing Cart Items:

    1.Create a user story for adding/removing cart items or adjusting quantity.
    2.Break down into tasks:
    3.Define API endpoints for adding/removing cart items or adjusting quantity.
    4.Implement logic for each endpoint.
    5.Update data structures to reflect changes in cart items.

# Writing Tests with unittest:
    2.Break down into tasks:
    3.Write unit tests for each endpoint.
    5.Ensure proper coverage of all endpoints and edge cases.
    5.Organize tests into appropriate test suites.
# Pushing to GitHub:

    Create a user story for pushing code to GitHub.
    Break down into tasks:
    Commit changes to local repository.
    Push changes to GitHub repository.

# Integrating CircleCI:

    Create a user story for integrating CircleCI.
    Break down into tasks:
    Integrate CircleCI with GitHub repository.
    Configure CircleCI to run tests and linters on each commit/push.
    Ensure builds pass successfully.

# Integrating Coveralls:

    Create a user story for integrating Coveralls.
    Break down into tasks:
    Integrate Coveralls with GitHub repository.
    Configure Coveralls to track test coverage.
    Ensure coverage reports are generated and updated properly.
