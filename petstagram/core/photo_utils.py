def apply_likes_counts(photo):
    photo.likes_count = photo.photo_likes.count()
    return photo

def apply_user_liked_photo(photo):
    photo.is_liked.by_user = photo.likes_count > 0
    return photo