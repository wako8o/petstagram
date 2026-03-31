from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet


class Photo(models.Model):
    DES_MAX_LENGTH = 300
    DES_MIN_LENGTH = 10
    LOCATION_MAX_LENGTH = 30

    photo = models.ImageField()

    description = models.TextField(
        max_length=DES_MAX_LENGTH,
        validators=[
            MinLengthValidator(DES_MIN_LENGTH, message='Трябва да е поне 10 символа')
        ]
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        null=True,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet, blank=True
    )

