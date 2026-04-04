from django.shortcuts import render

from petstagram.common.utilis import apply_user_liked_photo
from petstagram.common.views import apply_liked_count
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')

def delete_pet(request, username,  pet_slug):
    return render(request, 'pets/pet-delete-page.html')

def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photo = pet.photo_set.all()

    all_photos = [apply_liked_count(photo) for photo in pet.photo_set.all()]
    all_photos = [apply_user_liked_photo(photo) for photo in all_photos]
    context = {
        'pet': pet,
        'photo_count': all_photo,
        'pet_photos':all_photos
    }
    return render(request, 'pets/pet-details-page.html', context)

def edit_pet(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')
