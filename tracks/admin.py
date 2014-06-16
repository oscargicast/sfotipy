from actions import export_as_excel
from django.contrib import admin
from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'title',
        'order',
        'album',
        'player',
        'is_top_ten',
    )
    list_filter = ('artist', 'album', )
    search_fields = (
        'title',
        'artist__first_name',
        'artist__last_name',
        'album__title',
    )
    list_editable = ('title', 'album', )
    actions = (export_as_excel, )
    raw_id_fields = ('artist', )

    def is_top_ten(self, obj):
        return obj.order <= 10

    is_top_ten.boolean = True

admin.site.register(Track, TrackAdmin)
