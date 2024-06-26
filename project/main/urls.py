from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.signup, name='home'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('product', views.product,  name='product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)