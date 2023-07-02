from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    @classmethod
    def region_numbers(cls):
        return cls.objects.count()
