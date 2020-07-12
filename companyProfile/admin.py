from django.contrib import admin
from .models import Product
from .models import Photos
from .models import Videos
from .models import Content
# Register your models here.
admin.site.register(Product)
admin.site.register(Photos)
admin.site.register(Videos)
admin.site.register(Content)