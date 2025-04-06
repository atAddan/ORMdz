from django.db import models

class Filial(models.Model):
    name = models.CharField(max_length=44)
    address = models.CharField(max_length=255)


class Otdel(models.Model):
    name = models.CharField(max_length=255)
    flor = models.IntegerField()
    filial = models.ForeignKey(
        "company.Filial",
        null=True,
        related_name="Otdels",
        on_delete=models.SET_NULL,
    )


class Sotr(models.Model):
    full_name = models.CharField(max_length=255)
    doljnost = models.CharField(max_length=255)
    fone = models.CharField(max_length=20, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    otdel = models.ForeignKey(
        "company.Otdel",
        null=True,
        related_name="Sotrs",
        on_delete=models.CASCADE,
    )


# Create your models here.
