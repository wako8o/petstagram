from django.core.exceptions import ValidationError

def validators_photos_size(obj_photo):
    if obj_photo.size > 5242880:
        raise ValidationError('Размера не трябва да надвишава 5MB.')