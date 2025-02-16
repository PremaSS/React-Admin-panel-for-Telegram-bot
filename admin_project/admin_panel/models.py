# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Audio(models.Model):
    file_id = models.CharField(primary_key=True, max_length=256)
    duration = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=256, blank=True, null=True)
    mime_type = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    performer = models.CharField(max_length=256, blank=True, null=True)
    file_unique_id = models.CharField(max_length=256, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audio'


class AudioCategory(models.Model):
    category = models.OneToOneField('Category', models.DO_NOTHING, primary_key=True)  # The composite primary key (category_id, file_id) found, that is not supported. The first column is selected.
    file = models.ForeignKey(Audio, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'audio_category'
        unique_together = (('category', 'file'),)


class Category(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    parent_category_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'category'
        unique_together = (('name', 'parent_category_id'),)


class User(models.Model):
    tg_user_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=254)
    username = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
