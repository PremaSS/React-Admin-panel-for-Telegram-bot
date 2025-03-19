from django.contrib import admin
from .models import Media, MediaCategory, Category, User


class MediaAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'duration', 'file_name', 'mime_type', 'title', 'performer', 'file_size')  # Поля для отображения в списке
    search_fields = ('file_name', 'mime_type', 'title', 'performer')  # Возможность поиска по этим полям
    list_filter = ('mime_type', 'performer')  # Фильтрация по этим полям


class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'file_id')
    search_fields = ('file_id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_category_id')
    search_fields = ('name',)
    list_filter = ('parent_category_id',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('tg_user_id', 'full_name', 'username')
    search_fields = ('full_name', 'username')


admin.site.register(Media, MediaAdmin)
admin.site.register(MediaCategory, MediaCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)

admin.site.site_header = "Привет, Администратор!"
admin.site.index_template = "admin/custom_index.html"