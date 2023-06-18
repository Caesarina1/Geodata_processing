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
    target_objects = []
    for target in targets:
        tar = Target.objects.get(id=target.id)
        target_objects.append({"type": tar.type, "created": tar.created_at, "user": tar.users.all()})

    return render(request=request, template_name="position.html", context={"target_objects": target_objects})
