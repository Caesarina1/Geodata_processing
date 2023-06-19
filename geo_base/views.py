from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from .models import User, Target
from django.contrib.auth import login, authenticate
from geo_base.forms import SignUpForm, CombatUnitPositionForm
from .utils import RoleChoice


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            is_staff = True if form.cleaned_data.get('role')==RoleChoice.COMBAT_UNIT else False
            user = authenticate(username=username, password=raw_password, is_staff=is_staff)
            login(request, user)
            if is_staff:
                return redirect('position_page')
            return redirect('data_transfer_page')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def main_page(request):
    return render(request=request, template_name="start.html")


def data_transfer_page(request):
    return render(request=request, template_name="data_trans.html")


def position_page(request):
    if request.method=='POST':
        form = CombatUnitPositionForm(request.POST)
        if form.is_valid():
            your_unit = form.cleaned_data.get('your_unit')
            latitude = form.cleaned_data.get('latitude')
            longitude = form.cleaned_data.get('longitude')
            comment = form.cleaned_data.get('comment')
    else:
        form = CombatUnitPositionForm()
        targets = Target.objects.all()
        target_objects = []
        for target in targets:
            # tar = Target.objects.get(id=target.id)
            target_objects.append({"type": target.type, "created": target.created_at, "user": target.users.all()})

    return render(request=request, template_name="position.html", context={"target_objects": target_objects,
                                                                           "form": form})
