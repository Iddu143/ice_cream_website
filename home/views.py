from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item
# Create your views here.
def index(request):
    context={
        'variable':"Topper of the university"
    }
    messages.success(request,"welcome to the world of IceCreams..")
    return render(request,'index.html',context)

    # return HttpResponse("welcome to home page... ")

def about(request):
    return render(request,'about.html')

    # return HttpResponse("welcome to About page... ")

def services(request):
    return render(request,'services.html')
    # return render(request,'service2.html')

def service2(request):
    return render(request,'service2.html')
    #  return HttpResponse("welcome to chocolate page... ")

def familypack(request):
    return render(request,'familypack.html')
    # return HttpResponse("welcome to family page... ")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Renamed the function to auth_login
            # login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Account created successfully. You can now login.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')
 
    # return HttpResponse("welcome to contact page... ")

def view_item(request):
        # Add your logic here for handling the "View" button click
    # You can render a template or perform any other action
    return render(request, 'view_item.html')


# def edit_item(request):
#         # Add your logic here for handling the "View" button click
#     # You can render a template or perform any other action
#     return render(request, 'edit2.html')

def edit_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = Item.objects.get(pk=item_id)
        item.quantity += 1
        item.save()
        return redirect('cart')

    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'edit2.html', context)

# def order_view(request):
#         # Add your logic here for handling the "View" button click
#     # You can render a template or perform any other action
#     return render(request, 'order.html')

def order_view(request):
    if request.method == 'POST':
        # Logic for processing the order
        # Retrieve order details from the request and perform necessary actions
        # For example, save the order to the database, calculate total price, etc.

        # Display a success message to the user
        messages.success(request, 'Your order has been processed successfully!')
        
        # Redirect the user to a success page or any other desired page
        return redirect('order_success')

    # If the request method is GET, render the order form template
    return render(request, 'order.html')

def order_success_view(request):
    return render(request, 'order_success.html')



# email_utils.py

# from django.core.mail import send_mail
# from .email_utils import send_notification_email

# def send_notification_email(email):
#     subject = 'New newsletter signup'
#     message = f'A new user has signed up for the newsletter. Email: {email}'
#     from_email = 'mdidrisbaig55@gmail.com'
#     recipient_list = ['mdidrisbaig55@gmail.com']
    
#     send_mail(subject, message, from_email, recipient_list)

# from .email_utils import send_notification_email

# def newsletter_signup(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         # Process the newsletter signup
        
#         # Send notification email
#         send_notification_email(email)
        
#         return redirect('newsletter_success')  # Redirect to a success page
    
#     return render(request, 'newsletter_signup.html')
# # payment
# from django.conf import settings
# from django.shortcuts import render, redirect
# import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY

# def checkout(request):
#     # Process the payment
#     if request.method == 'POST':
#         try:
#             # Retrieve the payment token from the request
#             token = request.POST.get('stripeToken')

#             # Create a charge using the Stripe API
#             charge = stripe.Charge.create(
#                 amount=1000,  # Amount in cents
#                 currency='usd',
#                 source=token,
#                 description='Example Charge'
#             )

#             # Render the success page if the payment is successful
#             return redirect('success')

#         except stripe.error.CardError as e:
#             # Display an error message if the payment fails
#             return redirect('error')

#     # Render the checkout page initially
#     return render(request, 'checkout.html', {'publishable_key': settings.STRIPE_PUBLISHABLE_KEY})

# def success(request):
#     return render(request, 'success.html')

# def error(request):
#     return render(request, 'error.html')

# from django.shortcuts import render
# from django.conf import settings
# import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY

# def edit_item(request):
#     # Your logic to fetch the item details and process the form submission

#     # Generate a Stripe Session ID
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=[{
#             'price_data': {
#                 'currency': 'usd',
#                 'product_data': {
#                     'name': 'Ice Cream',
#                 },
#                 'unit_amount': 1000,  # Amount in cents
#             },
#             'quantity': 1,
#         }],
#         mode='payment',
#         success_url=request.build_absolute_uri(reverse('success')),
#         cancel_url=request.build_absolute_uri(reverse('error')),
#     )

#     return render(request, 'edit_item.html', {
#         'item': item,
#         'publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
#         'session_id': session.id,
#     })
