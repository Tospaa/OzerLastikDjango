import os
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from api.models import MamulDegisiklikForm, MamulDegisiklik, HammaddeDegisiklikForm, HammaddeDegisiklik, MamulSonDurum, HammaddeSonDurum, MamulRestockForm
from .models import AccountFormU, AccountFormP
from tsp_prj.settings import BASE_DIR

# NoAuth sayfalar:
def iletisim(request):
    return render(request, 'dashboard/iletisim.html')

def lisans(request):
    licenses = ''
    with open(os.path.join(BASE_DIR, 'dashboard', 'licenses'), 'r') as f:
        licenses = f.read().replace('\n', '<br />')
    return render(request, 'dashboard/lisans.html', {'licenses': licenses})

# Auth sayfalar
@login_required
def anasayfa(request):
    return render(request, 'dashboard/anasayfa.html', {'title': 'Dashboard'})

@login_required
def arama(request):
    return render(request, 'dashboard/arama.html', {'q': request.GET['q']})

@login_required
def hesap(request):
    loggedin_user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        formu = AccountFormU(request.POST, instance=loggedin_user)
        formp = AccountFormP(request.POST, request.FILES, instance=loggedin_user.profile)
        if formu.is_valid() and formp.is_valid():
            formu.save()
            formp.save()
            messages.add_message(request, messages.SUCCESS, 'Hesap bilgileriniz başarıyla kaydedilmiştir.')
            # from: https://groups.google.com/forum/#!topic/django-users/SLw6SrIC8wI
            return redirect('dashboard:anasayfa')
    elif request.method == 'GET':
        formu = AccountFormU(instance=loggedin_user)
        formp = AccountFormP(instance=loggedin_user.profile)
    return render(request, 'dashboard/hesap.html', {'formu': formu, 'formp': formp})

@login_required
def mamuleklecikar(request):
    son_on = MamulDegisiklik.objects.select_related('kullanici__profile').order_by('-id')[:10]
    if request.method == 'POST':
        form = MamulDegisiklikForm(request.POST)
        if form.is_valid():
            try:
                # from: https://stackoverflow.com/a/46941862
                #       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ THANK YOU SO MUCH!!!
                mamul_degisiklik_obj = form.save(commit=False)
                mamul_degisiklik_obj.kullanici_id = request.user.id
                mamul_degisiklik_obj.save()
                messages.add_message(request, messages.SUCCESS, 'Kayıt başarılı.')
                return redirect('dashboard:mamuleklecikar')
            except IntegrityError:
                messages.add_message(request, messages.ERROR, 'Veritabanına geçersiz girdi yapmaya çalıştınız. Stokta var olandan daha fazla malzemeyi çıktı gibi göstermeye çalışıyor olabilirsiniz. Girdiğiniz verileri gözden geçirin.')
    elif request.method == 'GET':
        form = MamulDegisiklikForm()
    return render(request, 'dashboard/mamuleklecikar.html', {'form': form, 'son_on': son_on})

@login_required
def mamulrapor(request):
    if 'istek' in request.GET.keys():
        if request.GET['istek'] == 'deg_tumu':
            # TODO: Implement all MamulDegisiklik
            return render(request, 'dashboard/mamulrapor.html')
        elif request.GET['istek'] == 'son_tumu':
            # TODO: Implement all MamulSonDurum
            return render(request, 'dashboard/mamulrapor.html')
    elif 'tarih' in request.GET.keys():
        pass
    mamul_son_degisiklikler = MamulDegisiklik.objects.order_by('-id')[:10]
    mamul_son_son_durum = MamulSonDurum.objects.order_by('-id')[:10]
    return render(request, 'dashboard/mamulrapor.html', {'mamul_son_degisiklikler': mamul_son_degisiklikler, 'mamul_son_son_durum': mamul_son_son_durum})

@login_required
def mamulguncelle(request):
    MamulRestockFormset = forms.formset_factory(MamulRestockForm)
    if request.method == 'POST':
        formset = MamulRestockFormset(request.POST)
    elif request.method == 'GET':
        formset = MamulRestockFormset()
    return render(request, 'dashboard/mamulguncelle.html', {'formset': formset})

@login_required
def hammaddeeklecikar(request):
    son_on = HammaddeDegisiklik.objects.select_related('kullanici__profile').order_by('-id')[:10]
    if request.method == 'POST':
        form = HammaddeDegisiklikForm(request.POST)
        if form.is_valid():
            try:
                hammadde_degisiklik_obj = form.save(commit=False)
                hammadde_degisiklik_obj.kullanici_id = request.user.id
                hammadde_degisiklik_obj.save()
                messages.add_message(request, messages.SUCCESS, 'Kayıt başarılı.')
                return redirect('dashboard:hammaddeeklecikar')
            except IntegrityError:
                messages.add_message(request, messages.ERROR, 'Veritabanına geçersiz girdi yapmaya çalıştınız. Stokta var olandan daha fazla malzemeyi çıktı gibi göstermeye çalışıyor olabilirsiniz. Girdiğiniz verileri gözden geçirin.')
    elif request.method == 'GET':
        form = HammaddeDegisiklikForm()
    return render(request, 'dashboard/hammaddeeklecikar.html', {'form': form, 'son_on': son_on})

@login_required
def hammadderapor(request):
    # TODO: Implement this.
    return render(request, 'dashboard/hammadderapor.html')

@login_required
def hammaddeguncelle(request):
    # TODO: Implement this.
    pass
