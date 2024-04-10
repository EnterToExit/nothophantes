from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.signup, name='home'),
    path('login', views.login, name='login'),
    path('product', views.product,  name='product'),
    path('accounts/', include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)