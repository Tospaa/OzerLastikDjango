import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from api.models import HammaddeDegisiklikForm
from .models import AccountFormU, AccountFormP
from tsp_prj.settings import BASE_DIR

# NoAuth sayfalar:
def contact(request):
    return render(request, 'dashboard/contact.html')

def license(request):
    licenses = ""
    with open(os.path.join(BASE_DIR, 'dashboard', 'licenses'), 'r') as f:
        licenses = f.read().replace('\n', '<br />')
    return render(request, 'dashboard/license.html', {'licenses': licenses})

# Auth sayfalar
@login_required
def index(request):
    return render(request, 'dashboard/index.html', {'title': 'Dashboard'})

@login_required
def account(request):
    loggedin_user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        formu = AccountFormU(request.POST, instance=loggedin_user)
        formp = AccountFormP(request.POST, request.FILES, instance=loggedin_user.profile)
        if formu.is_valid() and formp.is_valid():
            print(request.FILES)
            formu.save()
            formp.save()
            return redirect('dashboard:home')
    elif request.method == 'GET':
        formu = AccountFormU(instance=loggedin_user)
        formp = AccountFormP(instance=loggedin_user.profile)
    return render(request, 'dashboard/account.html', {'formu': formu, 'formp': formp})

@login_required
def hammadde(request):
    successful = False
    if request.method == 'POST':
        form = HammaddeDegisiklikForm(request.POST)
        if form.is_valid():
            # from: https://stackoverflow.com/a/46941862
            #       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ THANK YOU SO MUCH!!!
            hammadde_degisiklik_obj = form.save(commit=False)
            hammadde_degisiklik_obj.kullanici_id = request.user.id
            hammadde_degisiklik_obj.save()
            successful = True
            form = HammaddeDegisiklikForm()
    elif request.method == 'GET':
        form = HammaddeDegisiklikForm()
    return render(request, 'dashboard/hammadde.html', {'form': form, 'successful': successful})
