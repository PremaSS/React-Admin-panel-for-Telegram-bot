from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Category


def home(request):
    return render(request, 'admin_panel/home.html')


def explore(request):
   return render(request, 'admin_panel/explore.html')



@staff_member_required
def categories_by_parent(request, category_id):
    selected_category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.filter(parent_category=selected_category).values()

    data = {
        "message": f"Категории с родительской категорией: {selected_category.name}",
        "categories": list(categories),  
    }

    return JsonResponse(data)


@staff_member_required
def catalog(request):
    return render(request, "admin_panel/catalog.html")