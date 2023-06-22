from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from .models import User, Target
from django.contrib.auth import login, authenticate
from geo_base import forms
from .utils import RoleChoice


def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            is_staff = True if form.cleaned_data.get('role') == RoleChoice.COMBAT_UNIT else False
            user = authenticate(username=username, password=raw_password, is_staff=is_staff)
            login(request, user)
            if is_staff:
                return redirect('position_page')
            return redirect('data_transfer_page')
    else:
        form = forms.SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def main_page(request):
    return render(request=request, template_name="registration/login.html")


#  transferring target's location to DB

def data_transfer_page(request):

    if request.method == 'POST':
        form = forms.DataTransferForm(request.POST)
        if form.is_valid():
            type_data = form.cleaned_data.get('target_type')
            latitude_data = form.cleaned_data.get('latitude')
            longitude_data = form.cleaned_data.get('longitude')
            comment_data = form.cleaned_data.get('comment')
            new_target = Target(type=type_data, latitude=latitude_data, longitude=longitude_data, comment=comment_data)
            new_target.save()
            user_entry = User.objects.get(pk=1)  # TEMP (in the future this will be filled
            # by a logining with the command users.objects.get())
            new_target.users.add(user_entry)
            print('target_type')
    else:
        form = forms.DataTransferForm()

    return render(request=request, template_name="data_trans.html", context={"form": form})


#  getting target's data related to own position

def position_page(request):
    if request.method == 'POST':
        form = forms.CombatUnitPositionForm(request.POST)
        if form.is_valid():
            your_unit = form.cleaned_data.get('your_unit')
            latitude = form.cleaned_data.get('latitude')
            longitude = form.cleaned_data.get('longitude')
            comment = form.cleaned_data.get('comment')
    else:
        form = forms.CombatUnitPositionForm()
        targets = Target.objects.all()
        target_objects = []
        for target in targets:
            target_objects.append({"type": target.type, "created": target.created_at, "user": target.users.all()})

    return render(request=request, template_name="position.html", context={"target_objects": target_objects,
                                                                           "form": form})
