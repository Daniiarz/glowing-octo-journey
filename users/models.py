from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=15)
    age = models.IntegerField()
    hobby = models.TextField()
    image = models.ImageField(upload_to='users/', null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    about = models.TextField(null=True)

    def __str__(self):
        return f'{self.name} {self.sex} {self.age} {self.hobby}'