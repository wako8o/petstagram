from petstagram.common.models import Photo

def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.like_set.exists()

    return photo

def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER']+ f'#{photo_id}'