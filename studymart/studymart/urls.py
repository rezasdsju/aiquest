
from django.contrib import admin
from django.urls import path
from machine_learning.views import machine_learning
from machine_learning.views import deep_learning
from machine_learning.views import about_us
from Blogs.views import blog1
from Deep_Learning.views import deep_learning
from Data_Analysis.views import data_analysis
from About_Us.views import about_us
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',machine_learning),
    path('dl/', deep_learning),
    path('about/', about_us),
    path('blog/',blog1),
    path('deepl/',deep_learning),
    path('analysis/',data_analysis),
    path('about-us/',about_us),
]
