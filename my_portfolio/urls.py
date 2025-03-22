

import statistics
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from my_site import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('testimonios/', views.testimonios, name='testimonios'),
    path("about/", views.about, name="about"),
    path("certificaciones/", views.certificaciones, name="certificaciones"),
    path('api/blog/', views.BlogPostListView.as_view(), name='blog-list'),
    path('blog/', views.blog_list, name='blog-list'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog-detail'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
