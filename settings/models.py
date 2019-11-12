from django.db import models

# Setting Model.
class Setting(models.Model):
    label = models.CharField(max_length=50, null=True)
    slug = models.CharField(max_length=30, null=True)
    value = models.CharField(max_length=250, null=True)
    type = models.CharField(max_length=11, null=True)
    description = models.CharField(max_length=250, null=True)

    def __str__(self):
        label = self.label
        return label
