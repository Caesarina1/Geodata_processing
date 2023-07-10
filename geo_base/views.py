from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from .models import User, Target
from geo_base import forms
from geopy import distance as gd
from django.contrib.auth.decorators import login_required, permission_required


def main_page(request):

    return render(request=request, template_name="start.html")


#  transferring target's location to DB

def data_transfer(request):
    if request.method == 'POST':
        form = forms.DataTransferForm(request.POST)

        if form.is_valid():
            type_data = form.cleaned_data.get('target_type')
            latitude_data = form.cleaned_data.get('latitude')
            longitude_data = form.cleaned_data.get('longitude')
            comment_data = form.cleaned_data.get('comment')

            #  creating new instance
            new_target = Target(type=type_data, latitude=latitude_data, longitude=longitude_data, comment=comment_data)
            new_target.save()
            user_entry = User.objects.get(username=request.user)
            new_target.users.add(user_entry)

            return redirect('data_transfer_page')

    else:
        form = forms.DataTransferForm()

    return render(request=request, template_name="data_transfer.html", context={"form": form})


#  getting target's data related to own position

@login_required
# @permission_required
def position_page(request):
    your_unit = ""
    latitude = ""
    longitude = ""
    form = forms.CombatUnitPositionForm()
    target_objects = []
    target_msg = "*баш їх, бл***!"

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
                tar_image = '/static/images/military_personnel.png'

                if target.type == "Command post":
                    tar_image = '/static/images/command_post.png'

                elif target.type == "Military equipment":
                    tar_image = '/static/images/mlrs.png'

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

#  calculating distance from combat unit to targets and displaying only close ones
                dis_for_tar = gd.distance((latitude, longitude), (target.latitude, target.longitude)).km.__round__(3)

                if dis_for_tar <= 300:
                    target_objects.append({"type": target.type,
                                           "latitude": target.latitude, "longitude": target.longitude,
                                           "distance": dis_for_tar, "created": created_marker.strftime('%Y-%m-%d %H:%M:%S'),
                                           "Weight": tar_weight, "Certainty": tar_certainty,
                                           "user": ', '.join(user_marker_item), "target_img_path": tar_image})

                else:
                    target_msg = "You have no targets"

# writing down our coordinates in a file
                loc = "let locations = " + str(target_objects)
                with open("geo_base/static/targets.js", "w") as file:
                    file.write(loc)

# if filled up not correctly
    else:
        print("Put your data")

# creating combat unit marker
    combat_object = {"typeC": your_unit, "latitudeC": latitude, "longitudeC": longitude}
    loc_c = "let locationsCU = " + str(combat_object)

    with open("geo_base/static/locationsC.js", "w") as file:
        file.write(loc_c)

    return render(request=request, template_name="position.html", context={"target_objects": target_objects,
                                                                           "form": form, "combat_object": combat_object,
                                                                           "target_msg": target_msg})
