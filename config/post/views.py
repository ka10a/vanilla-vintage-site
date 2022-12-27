from datetime import datetime, date, timedelta

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

# from .forms import EventForm
from .models import *
# from .utils import Calendar

from .models import Item
import calendar


def index(request):
    return HttpResponse(loader.get_template('index.html').render({}, request))

def redirect_to_index(request):
    return redirect(index)

def contacts(request):
    return HttpResponse(loader.get_template('contact.html').render({}, request))

def products(request):
    return HttpResponse(loader.get_template('products.html').render({}, request))

def about(request):
    return HttpResponse(loader.get_template('about.html').render({}, request))