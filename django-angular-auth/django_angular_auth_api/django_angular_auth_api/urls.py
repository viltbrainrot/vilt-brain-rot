"""django_angular_auth_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
        path('users/', UserViewSet.as_view({'get': 'list'})),
"""
from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserLogIn

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-user-login/', UserLogIn.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
