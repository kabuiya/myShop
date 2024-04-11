from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from ecomm_shop.models import Products, Cart, CartItem, CustomerOrderDetails


# Create your views here.
def user_registration(request):
    # if it is a post method
    if request.method == 'POST':
        # extract details from the form
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password = request.POST['password']

        # check if all fields are filled
        if not (username and email and password and password1):
            messages.error(request, 'all fields are required')
            return render(request, "register.html")
        # check if the email or the username already exists in db
        if User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists!')
            return render(request, "register.html")
        # check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists!')
            return render(request, "register.html")
        # check if password whether matches password2
        if password1 != password:
            messages.error(request, 'password does not match')
            return render(request, "register.html")
        # validate email
        # create_new user
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, f'{new_user.username}, your  registration is successful, login to proceed')
        return redirect('login')
    return render(request, "register.html")


def user_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f' {username}, Successfully logged in!')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


# logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Successfully logged out!')
        return redirect('homepage')
    else:
        messages.error(request, 'Unauthorized! you are not logged in')
        return redirect('login')


# delete user account
def user_delete(request):
    if request.user.is_authenticated:
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, 'Your account has been successfully deleted.')
        return redirect('homepage')
    else:
        messages.error(request, 'You need to be logged in to delete your account.')
        return redirect('login')


# update user details
def user_update(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # check if user has inserted the details
            if not (request.POST.get('username') or request.POST.get('email')):
                messages.error(request, 'Email field and username cannot be empty.')
                return redirect('update_account')

            # check if the username or email is already taken
            if User.objects.filter(email=request.POST.get('email')).exclude(
                    pk=request.user.pk).exists() or User.objects.filter(username=request.POST.get('username')).exclude(
                pk=request.user.pk).exists():
                messages.error(request, 'Email or username is already taken.')
                return redirect('update_account')
            request.user.username = request.POST.get('username')
            request.user.email = request.POST.get('email')
            request.user.save()
            messages.success(request, 'successfully updated your profile')
            return redirect('homepage')
        return render(request, 'update.html')
    messages.error(request, 'Unauthorized access! Not logged in')
    return redirect('login')


def home_page(request):
    products = Products.objects.all()
    user_cart = None
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user).first()

    return render(request, 'home.html', {'products': products, 'user_cart': user_cart})


# adding to cart
def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = Products.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        cart.quantity_amount = sum(cart_item.quantity for cart_item in cart.cart_items.all())
        cart.total += product.price
        cart.save()
        return JsonResponse({'success': True, 'new_total': cart.total, 'item_quantity': cart_item.quantity,
                             'cart_quantity': cart.quantity_amount})
    else:
        return JsonResponse({'Error': True, 'error': 'User not authenticated'}, status=401)


# update from cart page, updating already added items in cart
# increase
def update_cart_item(request, cart_item_id):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(id=cart_item_id, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
        cart = cart_item.cart
        cart.quantity_amount = sum(cart_item.quantity for cart_item in cart.cart_items.all())
        cost_of_item = cart_item.quantity * cart_item.product.price
        cart.total = sum(item.product.price * item.quantity for item in cart.cart_items.all())
        cart.save()
        return JsonResponse(
            {'success': True, 'new_quantity': cart_item.quantity, 'new_cart_amount': cart.quantity_amount,
             'item_cost': cost_of_item, 'cart_total': cart.total})
    else:
        return JsonResponse({'success': False, 'error': 'User not authenticated'}, status=401)


# decrease

def decrease_cart_item(request, cart_item_id):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(id=cart_item_id, cart=cart)

        if cart_item.quantity >= 1:
            cart_item.quantity -= 1
            cart_item.save()

        if cart_item.quantity == 0:
            cart_item.delete()

        if cart.quantity_amount >= 1:
            cart.quantity_amount -= 1
            cart.total = sum(item.product.price * item.quantity for item in cart.cart_items.all())
            cart.save()

        if cart.quantity_amount == 0:
            cart.delete()

        itm_cost = cart_item.cartitem_total()
        new_item_quantity = cart_item.quantity

        return JsonResponse(
            {'success': True, 'new_item_quantity': new_item_quantity, 'cart_quantity': cart.quantity_amount,
             'item_cst': itm_cost, 'cart_total': cart.total})

    else:
        return JsonResponse({'success': False, 'error': 'User not authenticated'}, status=401)


# show cart
def cart_items(request):
    if request.user.is_authenticated:
        try:
            user_cart = Cart.objects.get(user=request.user)
            cart_obj = CartItem.objects.filter(cart=user_cart)
            return render(request, 'cartpage.html',
                          {'cart_obj': cart_obj, 'user_cart': user_cart})
        except Cart.DoesNotExist:
            messages.error(request, 'add items to cart first')
            return redirect('homepage')
    else:
        messages.error(request, 'Unauthorized access! Login')
        return redirect('login')


# checkout items

def checkout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_cart = Cart.objects.get(user=request.user)
            contact = request.POST.get('phone_number')
            address = request.POST.get('address')
            city = request.POST.get('city')
            if contact != '' and address != '' and city != '':
                order_details = CustomerOrderDetails(
                    customer_address=address,
                    customer_contact=contact,
                    customer_city=city
                )
                order_details.save()
                user_cart.delete()
                return redirect('homepage')

            else:
                messages.error(request, 'all fields are required!')
                return redirect('checkout')
        else:
            try:
                user_cart = Cart.objects.get(user=request.user)
                return render(request, 'checkout.html',
                              {'user_cart': user_cart})
            except Cart.DoesNotExist:
                messages.error(request, 'add items to cart first')
                return redirect('homepage')
    else:
        messages.error(request, 'Unauthorized access! Login')
        return redirect('login')


def terms(request):
    return render(request, 'terms.html')
