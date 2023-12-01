"""
URL configuration for monarchsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from monarchsite import views

#
# These are the routes that are answered by our webserver
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monarchmiddle.urls')),  
    path('',views.home),
    path('monarchs/',views.monarchs),
    path('monarchs/<int:id>',views.monarch_detail),
    path('monarchs/add', views.monarch_add),
    path('monarchs/delete/<int:id>', views.monarch_delete),
]

# Add the following to serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
