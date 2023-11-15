from django.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterDoneView, RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

