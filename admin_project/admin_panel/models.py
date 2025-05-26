# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    parent_category_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'category'
        unique_together = (('name', 'parent_category_id'),)


class Config(models.Model):
    name = models.CharField(primary_key=True, max_length=64)  # The composite primary key (name, value) found, that is not supported. The first column is selected.
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'config'
        unique_together = (('name', 'value'),)


class Media(models.Model):
    file_id = models.CharField(primary_key=True, max_length=255)
    duration = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    mime_type = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    performer = models.CharField(max_length=255, blank=True, null=True)
    file_unique_id = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'media'


class MediaCategory(models.Model):
    category = models.OneToOneField(Category, models.DO_NOTHING, primary_key=True)  # The composite primary key (category_id, file_id) found, that is not supported. The first column is selected.
    file = models.ForeignKey(Media, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'media_category'
        unique_together = (('category', 'file'),)


class Photo(models.Model):
    file_id = models.CharField(primary_key=True, max_length=128)
    create_data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'


class PhotoCategory(models.Model):
    file = models.ForeignKey(Photo, models.DO_NOTHING)
    category = models.OneToOneField(Category, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'photo_category'


class User(models.Model):
    tg_user_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
