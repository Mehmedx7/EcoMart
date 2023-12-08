from .models import *
from .serializers import SliderSerializer, ServiceSerializer, ProductSerializer, CartSerializer
from faker import Faker
from django.contrib.auth.models import User
import random
from .serializers import UserSerializer
from rest_framework import viewsets

fake = Faker()

def generate_dummy_data():
    # Create Sliders
    for _ in range(5):
        Slider.objects.create(
            title=fake.word(),
            desc=fake.text(),
            cover=fake.image_url(width=800, height=400)
        )

    # Create Services
    for _ in range(5):
        Service.objects.create(
            icon=fake.word(),
            title=fake.word(),
            subtitle=fake.sentence(),
            bg=fake.hex_color()
        )

    # Create Products
    for _ in range(10):
        Product.objects.create(
            productName=fake.word(),
            imgUrl=fake.image_url(width=400, height=400),
            category=fake.word(),
            price=random.uniform(10, 100),
            discount=random.uniform(0, 20),
            shortDesc=fake.text(),
            description=fake.paragraph(),
            avgRating=random.uniform(1, 5)
        )

    # Create Users
    users = []
    for _ in range(5):
        user = User.objects.create_user(
            username=fake.user_name(),
            password=fake.password(),
            email=fake.email()
        )
        users.append(user)

class SliderViewSet(viewsets.ModelViewSet):
    # generate_dummy_data()
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer