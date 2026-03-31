from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    PET_MAX_LENGTH = 30

    name = models.CharField(
        max_length=PET_MAX_LENGTH,
        null=False,
        blank=False,
    )
    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        editable=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"
    # class Meta:
    #     verbose_name_plural = 'Pet'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.pk} {self.name}')
        return super().save(*args, **kwargs)
