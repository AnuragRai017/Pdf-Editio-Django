"""
URL configuration for pdfeditor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# pdfeditor/urls.py
from django.contrib import admin
from django.urls import path
from editor import views
from django.conf import settings
from django.conf.urls.static import static

# pdfeditor/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('edit/<int:pdf_id>/', views.edit_pdf, name='edit_pdf'),
    path('save/<int:pdf_id>/', views.save_pdf, name='save_pdf'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
