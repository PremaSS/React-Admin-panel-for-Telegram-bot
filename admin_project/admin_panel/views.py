from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Media


def home(request):
    return render(request, 'home.html')


def explore(request):
    return render(request, 'explore.html')


@staff_member_required  # Ограничение доступа только для админов
def custom_admin_page(request):
    audio_files = Media.objects.all()

    context = {
        "message": "Привет! Это кастомная страница в админке.",
        "audio_files": audio_files
    }

    return render(request, "admin/custom_page.html", context)


