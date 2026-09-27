
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ml/', include('machine_learning.urls')),
    path('about/',include('About_Us.urls')),
    path('blog/', include('Blogs.urls')),
    path('deep/',include('Deep_Learning.urls')),
    path('data/', include('Data_Analysis.urls')),
    

]
