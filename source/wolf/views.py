import json, uuid
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.safestring import mark_safe

def index(request):
    return HttpResponse("")