from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ecomm_shop.models import Products, Cart, CartItem


class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_user_registration_valid_data(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'test123',
            'password': 'test123'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to login page on successful registration

    def test_user_registration_invalid_data(self):
        self.data = {
            'username': '',
            'email': '',
            'password1': '',
            'password': ''  # Incorrect password confirmation
        }
        response = self.client.post(self.register_url, self.data)  # Empty data
        self.assertEqual(response.status_code, 200)  # Returns registration page again with error messages

        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'test123',
            'password': 'wrongpassword'  # Incorrect password confirmation
        })
        self.assertEqual(response.status_code, 200)


#
#
class UserLoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test123')

    def test_user_login_valid_credentials(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'test123'})
        self.assertEqual(response.status_code, 302)  # Redirects to homepage on successful login

    def test_user_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Returns login page again with error messages


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('homepage')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test123')
        self.client.login(username='testuser', password='test123')

    def test_home_view_authenticated_user(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_view_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)  # Redirects to login page


#
class UserLogoutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse('logout')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test123')

    def test_user_logout_authenticated_user(self):
        self.client.login(username='testuser', password='test123')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Redirects to homepage on successful logout

    def test_user_logout_unauthenticated_user(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Redirects to login page


class UserDeleteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.delete_url = reverse('del_account')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test123')

    def test_user_delete_authenticated_user(self):
        self.client.login(username='testuser', password='test123')
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)  # Redirects to homepage on successful account deletion

    def test_user_delete_unauthenticated_user(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)  # Redirects to login page


class UpdateCartItemTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Products.objects.create(name='Test Product', price=10, quantity=10)
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test123')
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        self.update_cart_item_url = reverse('update_cart_item', args=[self.cart_item.id])

    def test_update_cart_item_authenticated_user(self):
        self.client.login(username='testuser', password='test123')
        response = self.client.get(self.update_cart_item_url)
        self.assertEqual(response.status_code, 200)  # You might want to adjust this depending on your implementation

    def test_update_cart_item_unauthenticated_user(self):
        response = self.client.get(self.update_cart_item_url)
        self.assertEqual(response.status_code, 401)  # Returns unauthorized status code


#
class DecreaseCartItemTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Products.objects.create(name='Test Product', price=10, quantity=2)
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test123')
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        self.decrease_cart_item_url = reverse('decrease_cart_item', args=[self.cart_item.id])

    def test_decrease_cart_item_authenticated_user(self):
        self.client.login(username='testuser', password='test123')
        response = self.client.get(self.decrease_cart_item_url)
        self.assertEqual(response.status_code, 200)

    def test_decrease_cart_item_unauthenticated_user(self):
        response = self.client.get(self.decrease_cart_item_url)
        self.assertEqual(response.status_code, 401)


class CartItemsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cart_items_url = reverse('cart')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test123')
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_items_authenticated_user(self):
        self.client.login(username='testuser', password='test123')
        response = self.client.get(self.cart_items_url)
        self.assertEqual(response.status_code, 200)

    def test_cart_items_unauthenticated_user(self):
        response = self.client.get(self.cart_items_url)
        self.assertEqual(response.status_code, 302)  # Redirects to login page


class CheckoutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)
        self.cart = Cart.objects.create(user=self.user)

    def test_checkout_authenticated_user(self):
        self.client.login(username='testuser', password='test123')
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)  # You might want to adjust this depending on your implementation

    def test_checkout_unauthenticated_user(self):
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)  # Redirects to login page





