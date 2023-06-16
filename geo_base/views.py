from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from .models import User, Target


# Create your views here.

def main_page(request):
    return render(request=request, template_name="start.html")


def data_transfer_page(request):
    return render(request=request, template_name="data_trans.html")


def position_page(request):
    targets = Target.objects.all()
    users = User.objects.all()
    target_objects = []
    for target in targets:
        target_objects.append(Target.objects.get(id=target.id))

    return render(request=request, template_name="position.html", context={"targets": targets, "users": users, "target_objects": target_objects})
