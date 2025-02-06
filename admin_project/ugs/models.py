import uuid
from django.db import models


class Audio(models.Model):
    file_id = models.CharField(max_length=256, primary_key=True, null=False)
    duration = models.IntegerField()
    file_name = models.CharField(max_length=256)
    mime_type = models.CharField(max_length=64)
    title = models.CharField(max_length=256)
    performer = models.CharField(max_length=256)
    file_unique_id = models.CharField(max_length=256)
    file_size = models.IntegerField()

    # class Meta:
    #     managed = False  # Оставить, если не хочешь, чтобы Django управлял этой таблицей

    def __str__(self):
        return self.title


class AudioCategory(models.Model):
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)  # Связь с категорией
    file_id = models.ForeignKey('Audio', on_delete=models.CASCADE)  # Связь с аудио файлом

    # class Meta:
    #     # managed = False
    #     unique_together = ('category_id', 'file_id')  # Составной уникальный ключ

    def __str__(self):
        return f'{self.category_id.name} - {self.file_id}'


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    name = models.CharField(max_length=256, db_index=True, null=False)
    parent_category_id = models.CharField(max_length=64, default=' ', null=False)

    # class Meta:
    #     managed = False

    def __str__(self):
        return self.name


class User(models.Model):
    objects = None
    tg_user_id = models.IntegerField(primary_key=True, null=False)
    full_name = models.CharField(max_length=254, null=False)
    username = models.CharField(max_length=32, blank=True, null=True)  # Сделал пустым, чтобы был вариант оставить без username

    # class Meta:
    #     managed = False

    def __str__(self):
        return self.username or self.full_name
