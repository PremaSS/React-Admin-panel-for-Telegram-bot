from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from admin_panel.models import Category


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


def get_all_categories_api(request):
    all_categories_list = list(Category.objects.all().values('id', 'name', 'parent_category_id')) # Получаем все данные из Category из БД(models.py)

    category_map = {str(cat['id']): cat for cat in all_categories_list} # Сооздаём словарь категории по их ID, где ключ - это ID, а значение - это сам словарь cat

    for cat_id in category_map:
        category_map[cat_id]['subcategories'] = [] # Добавляем поле subcategories в каждом словаре.


    root_categories = []
    for cat_id, cat_data in category_map.items():
        parent_id = cat_data.get('parent_category_id')

        if parent_id and parent_id in category_map:
            parent_category = category_map[parent_id]
            parent_category['subcategories'].append(cat_data)
        else:
            root_categories.append(cat_data)   
            
    return JsonResponse(root_categories, safe=False)











