from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
# Create your models here.



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"










teacher_group, created = Group.objects.get_or_create(name='Teacher')

# teacher_group.permissions.add(*permissions_to_add)

# permissions = Permission.objects.filter(content_type__app_label='app')


# teacher_group.permissions.set([permission_list])
# teacher_group.permissions.add(permission, permission,)
# teacher_group.permissions.remove(permission, permission,)
# teacher_group.permissions.clear()