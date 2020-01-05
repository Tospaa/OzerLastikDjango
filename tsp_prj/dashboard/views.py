from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    #context = {'latest_question_list': latest_question_list,}
    return render(request, 'dashboard/index.html', {'title': 'Özer Ayakkabı Dashboard'})
