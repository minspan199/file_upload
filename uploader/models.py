# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FileManagement(models.Model):

    name = models.TextField()
    gender = models.TextField()
    file_1 = models.FileField()
    email = models.CharField(max_length=30, blank=True, null=True)
    file_managementcol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_management'

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=16)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
