from django.contrib import admin

from petstagram.photos.models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'date_of_publication', 'get_tagged_pets']

    def get_tagged_pets(self, obj):
        boj_tagged_pets = obj.tagged_pets.all()
        return ', '.join([o.name for o in boj_tagged_pets])
