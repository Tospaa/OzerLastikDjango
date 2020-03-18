import os
import pickle

from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render

import api.models
import dashboard.serializers

from .decorators import group_required
from .models import AccountFormP, AccountFormU


# NoAuth sayfalar:
def iletisim(request):
    return render(request, 'dashboard/iletisim.html')


def lisans(request):
    licenses = ''
    with open(os.path.join(settings.BASE_DIR, 'dashboard', 'licenses'), 'r') as f:
        licenses = f.read().replace('\n', '<br />')
    return render(request, 'dashboard/lisans.html', {'licenses': licenses})

# Auth sayfalar:
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
        formp = AccountFormP(request.POST, request.FILES,
                             instance=loggedin_user.profile)
        if formu.is_valid() and formp.is_valid():
            formu.save()
            formp.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Hesap bilgileriniz başarıyla kaydedilmiştir.')
            # from: https://groups.google.com/forum/#!topic/django-users/SLw6SrIC8wI
            return redirect('dashboard:anasayfa')
    elif request.method == 'GET':
        formu = AccountFormU(instance=loggedin_user)
        formp = AccountFormP(instance=loggedin_user.profile)
    return render(request, 'dashboard/hesap.html', {'formu': formu, 'formp': formp})


@login_required
def sifredegistir(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # from: https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html
            messages.add_message(request, messages.SUCCESS, 'Şifreniz başarıyla değiştirilmiştir.')
            return redirect('dashboard:anasayfa')
    elif request.method == 'GET':
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/sifredegistir.html', {'form': form})


@login_required
@group_required('editor')
def kolieklecikar(request):
    son_on = api.models.KoliDegisiklik.objects.select_related(
        'kullanici__profile').order_by('-id')[:10]
    if request.method == 'POST':
        form = api.models.KoliDegisiklikForm(request.POST)
        if form.is_valid():
            try:
                # from: https://stackoverflow.com/a/46941862
                #       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ THANK YOU SO MUCH!!!
                koli_degisiklik_obj = form.save(commit=False)
                koli_degisiklik_obj.kullanici_id = request.user.id
                koli_degisiklik_obj.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Kayıt başarılı.')
                return redirect('dashboard:kolieklecikar')
            except IntegrityError:
                messages.add_message(
                    request, messages.ERROR, 'Veritabanına geçersiz girdi yapmaya çalıştınız. Stokta var olandan daha fazla malzemeyi çıktı gibi göstermeye çalışıyor olabilirsiniz. Girdiğiniz verileri gözden geçirin.')
    elif request.method == 'GET':
        form = api.models.KoliDegisiklikForm()
    return render(request, 'dashboard/koli/kolieklecikar.html', {'form': form, 'son_on': son_on})


@login_required
@group_required('editor')
def kolieklecikar_sil(request, pk):
    if request.method == 'POST':
        try:
            delet_dis = api.models.KoliDegisiklik.objects.get(pk=pk)
            delet_dis.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Silme işlemi başarılı.'
            )
        except IntegrityError:
            messages.add_message(
                request,
                messages.ERROR,
                'Kolideki değişiklikleri, kayıt sırasına göre, sondan başlayarak silmelisiniz. Ayrıca, başka gün içinde yapılan değişikliği silemezsiniz.'
            )
        return redirect('dashboard:kolieklecikar')
    elif request.method == 'GET':
        try:
            record = api.models.KoliDegisiklik.objects.get(pk=pk)
        except api.models.KoliDegisiklik.DoesNotExist:
            messages.add_message(request, messages.ERROR,
                                 'Böyle bir kayıt yok.')
            return redirect('dashboard:kolieklecikar')
        return render(request, 'dashboard/koli/kolieklecikar_sil.html', {'record': record})


@login_required
def kolirapor(request):
    if 'istek' in request.GET.keys():
        if request.GET['istek'] == 'deg_tumu':
            data = api.models.KoliDegisiklik.objects.select_related(
                'kullanici').order_by('-id')
            return render(request, 'dashboard/koli/kolirapor_degtumu.html', {'data': data})
        elif request.GET['istek'] == 'son_tumu':
            data = None
            if request.method == 'POST':
                form = api.models.GunGetirForm(request.POST)
                if form.is_valid():
                    try:
                        data = dashboard.serializers.SingleRecordSerializer(
                            api.models.KoliSonDurum.objects.get(tarih=form.cleaned_data['gun']))
                    except api.models.KoliSonDurum.DoesNotExist:
                        messages.add_message(
                            request, messages.ERROR, 'Girilen güne ait veri bulunamadı.')
            elif request.method == 'GET':
                form = api.models.GunGetirForm()
            return render(request, 'dashboard/koli/kolirapor_sontumu.html', {'form': form, 'data': data})
    elif 'tarih' in request.GET.keys():
        pass
    elif 'detay' in request.GET.keys():
        pass
    # from: https://books.agiliq.com/projects/django-orm-cookbook/en/latest/select_some_fields.html
    # The only difference between 'only' and 'values' is 'only' also fetches the id
    # guess what: if you don't use 'only', get_mamul_model_display won't work. yeah, just try to live with that.
    koli_son_degisiklikler = api.models.KoliDegisiklik.objects.order_by(
        '-id').only('tarih', 'mamul_model', 'koli_turu', 'koli_adet')[:10]
    koli_son_durum_ = dashboard.serializers.SingleRecordSerializer(
        api.models.KoliSonDurum.objects.latest('tarih'))
    return render(request, 'dashboard/koli/kolirapor.html', {'koli_son_degisiklikler': koli_son_degisiklikler, 'durum': koli_son_durum_})


@login_required
@group_required('editor')
def koliguncelle(request):
    api.models.KoliRestockFormset = forms.formset_factory(
        api.models.KoliRestockForm)
    if request.method == 'POST':
        formset = api.models.KoliRestockFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                try:
                    record = api.models.KoliSonDurum.objects.latest('tarih')
                    new_value = form.cleaned_data['koli_adet'] - pickle.loads(vars(record)[form.cleaned_data['mamul_model']])[
                        form.cleaned_data['kalite']][form.cleaned_data['koli_turu']][form.cleaned_data['kolideki_mamul_adet']]
                except (KeyError, EOFError, api.models.KoliSonDurum.DoesNotExist):
                    new_value = form.cleaned_data['koli_adet']
                api.models.KoliDegisiklik.objects.create(
                    mamul_model=form.cleaned_data['mamul_model'],
                    koli_turu=form.cleaned_data['koli_turu'],
                    kolideki_mamul_adet=form.cleaned_data['kolideki_mamul_adet'],
                    kalite=form.cleaned_data['kalite'],
                    koli_adet=new_value,
                    notlar='Bu değişiklik Koli Güncelleme ekranından yapılmıştır.',
                    kullanici=request.user
                )
            messages.add_message(request, messages.SUCCESS, 'Kayıt başarılı.')
            return redirect('dashboard:koliguncelle')
    elif request.method == 'GET':
        formset = api.models.KoliRestockFormset()
    return render(request, 'dashboard/koli/koliguncelle.html', {'formset': formset})


@login_required
@group_required('editor')
def hammaddeeklecikar(request):
    son_on = api.models.HammaddeDegisiklik.objects.select_related(
        'kullanici__profile').order_by('-id')[:10]
    if request.method == 'POST':
        form = api.models.HammaddeDegisiklikForm(request.POST)
        if form.is_valid():
            try:
                hammadde_degisiklik_obj = form.save(commit=False)
                hammadde_degisiklik_obj.kullanici_id = request.user.id
                hammadde_degisiklik_obj.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Kayıt başarılı.')
                return redirect('dashboard:hammaddeeklecikar')
            except IntegrityError:
                messages.add_message(
                    request, messages.ERROR,
                    'Veritabanına geçersiz girdi yapmaya çalıştınız. Stokta var olandan daha fazla malzemeyi çıktı gibi göstermeye çalışıyor olabilirsiniz. Girdiğiniz verileri gözden geçirin.')
    elif request.method == 'GET':
        form = api.models.HammaddeDegisiklikForm()
    return render(request, 'dashboard/hammadde/hammaddeeklecikar.html', {'form': form, 'son_on': son_on})


@login_required
@group_required('editor')
def hammaddeeklecikar_sil(request, pk):
    if request.method == 'POST':
        try:
            delet_dis = api.models.HammaddeDegisiklik.objects.get(pk=pk)
            delet_dis.delete()
            messages.add_message(request, messages.SUCCESS,
                                 'Silme işlemi başarılı.')
        except IntegrityError:
            messages.add_message(
                request, messages.ERROR, 'Başka bir gün içinde yapılmış değişikliği silemezsiniz.')
        return redirect('dashboard:hammaddeeklecikar')
    elif request.method == 'GET':
        try:
            record = api.models.HammaddeDegisiklik.objects.get(pk=pk)
        except api.models.HammaddeDegisiklik.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Böyle bir kayıt yok.')
            return redirect('dashboard:hammaddeeklecikar')
        return render(request, 'dashboard/hammadde/hammaddeeklecikar_sil.html', {'record': record})


@login_required
def hammadderapor(request):
    if 'istek' in request.GET.keys():
        if request.GET['istek'] == 'deg_tumu':
            data = api.models.HammaddeDegisiklik.objects.select_related(
                'kullanici').order_by('-id')
            return render(request, 'dashboard/hammadde/hammadderapor_degtumu.html', {'data': data})
        elif request.GET['istek'] == 'son_tumu':
            data = None
            if request.method == 'POST':
                form = api.models.GunGetirForm(request.POST)
                if form.is_valid():
                    try:
                        data = dashboard.serializers.SingleRecordSerializer(
                            api.models.HammaddeSonDurum.objects.get(tarih=form.cleaned_data['gun']))
                    except api.models.HammaddeSonDurum.DoesNotExist:
                        messages.add_message(
                            request, messages.ERROR, 'Girilen güne ait veri bulunamadı.')
            elif request.method == 'GET':
                form = api.models.GunGetirForm()
            return render(request, 'dashboard/hammadde/hammadderapor_sontumu.html', {'form': form, 'data': data})
    ham_son_degisiklikler = api.models.HammaddeDegisiklik.objects.order_by(
        '-id').only('tarih', 'madde', 'miktar')[:10]
    ham_son_durum = dashboard.serializers.SingleRecordSerializer(
        api.models.HammaddeSonDurum.objects.latest('tarih'))
    return render(request, 'dashboard/hammadde/hammadderapor.html', {'ham_son_degisiklikler': ham_son_degisiklikler, 'durum': ham_son_durum})


@login_required
@group_required('editor')
def hammaddeguncelle(request):
    api.models.HammaddeRestockFormset = forms.formset_factory(
        api.models.HammaddeRestockForm)
    if request.method == 'POST':
        formset = api.models.HammaddeRestockFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                try:
                    record = api.models.HammaddeSonDurum.objects.latest(
                        'tarih')
                    new_value = form.cleaned_data['miktar'] - \
                        vars(record)[form.cleaned_data['madde']]
                except (KeyError, EOFError, api.models.HammaddeSonDurum.DoesNotExist):
                    new_value = form.cleaned_data['miktar']
                api.models.HammaddeDegisiklik.objects.create(
                    madde=form.cleaned_data['madde'],
                    miktar=new_value,
                    notlar='Bu değişiklik Hammadde Güncelleme ekranından yapılmıştır.',
                    kullanici=request.user
                )
            messages.add_message(request, messages.SUCCESS, 'Kayıt başarılı.')
            return redirect('dashboard:hammaddeguncelle')
    elif request.method == 'GET':
        formset = api.models.HammaddeRestockFormset()
    return render(request, 'dashboard/hammadde/hammaddeguncelle.html', {'formset': formset})

@login_required
def yasak(request):
    return render(request, 'dashboard/yasak.html')
