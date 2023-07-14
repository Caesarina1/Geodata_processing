from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from auth_app import forms
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
                current_user = User.objects.get(username=username)
                current_user.is_staff = True
                current_group = Group.objects.get(name='Combat Units')
                current_user.groups.add(current_group)
                current_user.save()
                return redirect('position_page')

            return redirect('data_transfer_page')

    else:
        form = forms.SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def forbidden(request):

    return render(request=request, template_name="forbidden_page.html")
