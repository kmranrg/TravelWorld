from django.db import models

# Create your models here.

class Destination:
    id: int
    name: str
    img: str
    desc: str
    price: int
    offer: bool