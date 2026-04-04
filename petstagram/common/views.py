from django.shortcuts import render, redirect, resolve_url
import pyperclip
from django.urls import reverse

from petstagram.common.models import Photo, Like
from petstagram.common.utilis import apply_user_liked_photo, get_photo_url


def apply_liked_count(photo):
    photo.likes_count = photo.like_set.count()

    return photo



def home_common(request):
    all_photos = [apply_liked_count(photo) for photo in Photo.objects.all()]
    all_photos = [apply_user_liked_photo(photo) for photo in all_photos]


    context = {
        'all_photos': all_photos
    }

    return render(request, 'common/home-page.html', context)



def like_function(request, photo_id):

    photo = Photo.objects.get(pk=photo_id,)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()
    if liked_object:
        liked_object.delete()

    else:
        like = Like(to_photo=photo)
        like.save()

    result = get_photo_url(request, photo_id)

    return redirect(result)

    # # TODO 2:43
    # photo = Photo.objects.get(id=photo_id)
    # # liked_object = Like.objects.filter(to_photo_id=photo_id).first()
    #
    # # if liked_object:
    # #     liked_object.delete()
    # #
    # # else:
    # like = Like(to_photo=photo)
    # like.save()
    # result = request.META['HTTP_REFERER']+ f'#{photo_id}'
    # return  redirect(result)


def share_function(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
        })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))
