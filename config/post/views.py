from django.shortcuts import redirect, get_object_or_404
from django.template import loader
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, ContactForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    item_list = Item.objects.filter(category='des')[:3]
    if len(item_list) < 3:
        item_list = Item.objects.all()[:3]
    return HttpResponse(loader.get_template('index.html').render({'item_list': item_list}, request))


def redirect_to_index(request):
    return redirect(index)


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subj = form.cleaned_data['subj']
            text = form.cleaned_data['text']

            send_mail(
                "From {}, {}".format(name, subj),
                text,
                email,
                ['vanilla-vintage@gmail.com'])
    else:
        form = ContactForm()
    return HttpResponse(loader.get_template('contact.html').render({'form': form}, request))


@csrf_exempt
def products(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            recipient = form.cleaned_data['email']
            address = form.cleaned_data['address']
            ids = form.cleaned_data['ids']
            subj = 'Order in Vanilla Vintage Shop'
            text = '''Hello, {}! You placed your order in our site recently. Our manager contacts you soon.'''

            send_mail(
                subj,
                text.format(name),
                'vanilla-vintage@gmail.com',
                [recipient])

    form = OrderForm()
    item_list = Item.objects.all()
    return HttpResponse(loader.get_template('products.html').render({'item_list': item_list, 'form': form}, request))


def about(request):
    return HttpResponse(loader.get_template('about.html').render({}, request))