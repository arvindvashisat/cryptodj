from django.shortcuts import render
from .models import Setting

# Create your views here.
def settings(request):
    settings = Setting.objects.all()

    context = {
        'settings' : settings
    }
    return render(request, 'settings/settings.html', context)