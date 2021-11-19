from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.


# To show other fields in the admin panel
class CarAdmin(admin.ModelAdmin):
#Add thumbnail photo with link to the admin panel
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image' ## adding heading to the thumbnail
    list_display = ('id', 'thumbnail','car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured' )
    list_display_links = ('id', 'thumbnail', 'car_title')  ## make the items clickable
    list_editable = ('is_featured',) ##make this editable from the table, instead of first clicking
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')
admin.site.register(Car, CarAdmin)
