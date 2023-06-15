from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from .models import User, Target


# Create your views here.

def main_page(request):
    return render(request=request, template_name="start.html")


def data_transfer_page(request):
    return render(request=request, template_name="data_trans.html")


def position_page(request):
    targets_to_render = Target.objects.all()
    return render(request=request, template_name="position.html")
