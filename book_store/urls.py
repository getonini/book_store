"""book_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from books.views import BookViewSet, ClientViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Book Store API",
        default_version='v1',
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')
router.register(r'books', BookViewSet, basename='books')


urlpatterns = [
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url('docs/', schema_view),
    path('admin/', admin.site.urls),
    url(r'v1/', include(router.urls)),
]
