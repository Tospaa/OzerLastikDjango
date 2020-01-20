from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from api.models import HammaddeDegisiklikForm

@login_required
def index(request):
    #context = {'latest_question_list': latest_question_list,}
    return render(request, 'dashboard/index.html', {'title': 'Dashboard'})

def contact(request):
    return render(request, 'dashboard/contact.html')

@login_required
def account(request):
    if request.method == 'GET':
        return render(request, 'dashboard/account.html')
    elif request.method == 'POST':
        # TODO: Burlara user input check koy. Yanarız valla.
        user = User.objects.get(pk=request.user.id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.profile.title = request.POST['title']
        # TODO: Burda foto ekleme falan olsun.
        user.save()
        return redirect('dashboard:home')

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
            successful = True
            form = HammaddeDegisiklikForm()
    elif request.method == 'GET':
        successful = False
        form = HammaddeDegisiklikForm()
    return render(request, 'dashboard/hammadde.html', {'form': form, 'successful': successful})
