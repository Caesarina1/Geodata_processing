from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from .models import User, Target
from django.contrib.auth import login, authenticate
from geo_base import forms
from .utils import RoleChoice
from .distance import count_dist
from datetime import date
import time


def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            is_staff = True if form.cleaned_data.get('role') == RoleChoice.COMBAT_UNIT else False
            user = authenticate(username=username, password=raw_password, is_staff=is_staff)  #is_authenticated
            login(request, user)
            if is_staff:
                current_user = User.objects.get(username=username)
                current_user.is_staff = True
                current_user.save()
                return redirect('position_page')
            return redirect('data_transfer_page')
    else:
        form = forms.SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def main_page(request):
    return render(request=request, template_name="start.html")


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
            current_user_pk = 1  # TEMP (in the future this will be filled with pk of a user, which has been logged in)!!!!!!!!
            user_entry = User.objects.get(pk=current_user_pk)
            new_target.users.add(user_entry)
            return redirect('data_transfer_page')
    else:
        form = forms.DataTransferForm()

    return render(request=request, template_name="data_trans.html", context={"form": form})


#  getting target's data related to own position

def position_page(request):
    latitude = ""
    longitude = ""
    form = forms.CombatUnitPositionForm()
    target_objects = []

    if request.method == 'POST':
        form = forms.CombatUnitPositionForm(request.POST)
        if form.is_valid():
            your_unit = form.cleaned_data.get('your_unit')
            latitude = form.cleaned_data.get('latitude')
            longitude = form.cleaned_data.get('longitude')
            comment = form.cleaned_data.get('comment')
            targets = Target.objects.all()

#  adding weight and certainty to our data
            for target in targets:
                tar_weight = 0
                tar_certainty = 0

                if target.type == 'command_post':
                    tar_weight += 10

                for _ in target.users.all():
                    tar_weight += 2
                    tar_certainty += 10

                created_marker = target.created_at
                user_marker = target.users.all()

                user_marker_item = []
                for use in user_marker:
                    user_marker_item.append(use.username)

# !!! count_dist
                target_objects.append({"type": target.type,
                                       "latitude": target.latitude, "longitude": target.longitude,
                                       "distance": count_dist((latitude, longitude),(target.latitude, target.longitude)),
                                       "created": created_marker.strftime('%Y-%m-%d %H:%M:%S'), "Weight": tar_weight, "Certainty": tar_certainty,
                                       "user": ', '.join(user_marker_item)})

# writing down our coordinates in a file
                loc = "let locations = " + str(target_objects)
                with open("geo_base/static/targets.js", "w") as file:
                    file.write(loc)

# if filled up not correctly
    else:
        print("Put your data")

    return render(request=request, template_name="position.html", context={"target_objects": target_objects,
                                                                           "form": form, "wind_lat": latitude, "wind_long": longitude})
