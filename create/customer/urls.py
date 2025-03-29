from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about2/', views.about2, name='about2'),
    path('about3/', views.about3, name='about3'),
    path('menu/', views.menu, name='menu'),
    path('blog3/', views.blog3, name='blog3'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    path('book/', views.book, name='book'),
    path('services3/', views.services3, name='services3'),
    path('testimonial3/', views.testimonial3, name='testimonial3'),
    path('contact/', views.contact, name='contact'),
    path('contact3/', views.contact3, name='contact3'),
    path('product/', views.product, name='product'),
    path('login/', views.login_view, name='login'),
    path('Tracking/', views.Tracking, name='Tracking'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile', views.profile_view, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)