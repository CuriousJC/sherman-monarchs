# basically extending our admin module by pulling in our custom models and then registering them to our admin site

from .models import Monarch

from django.contrib import admin

admin.site.register(Monarch)