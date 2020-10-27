from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.image = 'destination_1.jpg'
    dest1.price = 500
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Indonesia'
    dest2.desc = 'Nulla pretium tincidunt felis, nec.'
    dest2.image = 'destination_2.jpg'
    dest2.price = 900
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'New York'
    dest3.desc = 'Nulla pretium tincidunt felis, nec.'
    dest3.image = 'destination_3.jpg'
    dest3.price = 900
    dest3.offer = False

    dest4 = Destination()
    dest4.name = 'California'
    dest4.desc = 'Nulla pretium tincidunt felis, nec.'
    dest4.image = 'destination_4.jpg'
    dest4.price = 900
    dest4.offer = False

    dest5 = Destination()
    dest5.name = 'Texas'
    dest5.desc = 'Nulla pretium tincidunt felis, nec.'
    dest5.image = 'destination_5.jpg'
    dest5.price = 900
    dest5.offer = False

    dest6 = Destination()
    dest6.name = 'Dubai'
    dest6.desc = 'Nulla pretium tincidunt felis, nec.'
    dest6.image = 'destination_6.jpg'
    dest6.price = 900
    dest6.offer = False

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    return render(request, 'index.html', {'dests': dests})