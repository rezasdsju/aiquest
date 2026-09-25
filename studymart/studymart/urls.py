
from django.contrib import admin
from django.urls import path
from machine_learning import views
from Blogs import views as BlogViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.machine_learning),
    path('dl/', views.deep_learning),
    path('about/', views.about_us),
    path('blog/',BlogViews.blog1)
]
