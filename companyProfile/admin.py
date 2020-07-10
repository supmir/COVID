from django.contrib import admin
from .models import Product
from .models import Photos
from .models import Videos
# Register your models here.
admin.site.register(Product)
admin.site.register(Photos)
admin.site.register(Videos)