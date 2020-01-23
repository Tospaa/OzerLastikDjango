import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from api.models import HammaddeDegisiklikForm
from .models import AccountFormU, AccountFormP
from tsp_prj.settings import BASE_DIR

# NoAuth sayfalar:
def iletisim(request):
    return render(request, 'dashboard/iletisim.html')

def lisans(request):
    licenses = ""
    with open(os.path.join(BASE_DIR, 'dashboard', 'licenses'), 'r') as f:
        licenses = f.read().replace('\n', '<br />')
    return render(request, 'dashboard/lisans.html', {'licenses': licenses})

# Auth sayfalar
@login_required
def anasayfa(request):
    return render(request, 'dashboard/anasayfa.html', {'title': 'Dashboard'})

@login_required
def hesap(request):
    loggedin_user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        formu = AccountFormU(request.POST, instance=loggedin_user)
        formp = AccountFormP(request.POST, request.FILES, instance=loggedin_user.profile)
        if formu.is_valid() and formp.is_valid():
            formu.save()
            formp.save()
            # from: https://groups.google.com/forum/#!topic/django-users/SLw6SrIC8wI
            return redirect('dashboard:anasayfa')
    elif request.method == 'GET':
        formu = AccountFormU(instance=loggedin_user)
        formp = AccountFormP(instance=loggedin_user.profile)
    return render(request, 'dashboard/hesap.html', {'formu': formu, 'formp': formp})

@login_required
def hammadde(request):
    if request.method == 'POST':
        form = HammaddeDegisiklikForm(request.POST)
        if form.is_valid():
            # from: https://stackoverflow.com/a/46941862
            #       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ THANK YOU SO MUCH!!!
            hammadde_degisiklik_obj = form.save(commit=False)
            hammadde_degisiklik_obj.kullanici_id = request.user.id
            hammadde_degisiklik_obj.save()
            messages.add_message(request, messages.SUCCESS, 'Kayıt başarılı.')
            return redirect('dashboard:hammadde')
    elif request.method == 'GET':
        form = HammaddeDegisiklikForm()
    return render(request, 'dashboard/hammadde.html', {'form': form})
