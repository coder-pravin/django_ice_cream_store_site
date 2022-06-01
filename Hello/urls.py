from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Pravin Ice cream Admin"
admin.site.site_title = "Pravin Ice cream Admin Portal"
admin.site.index_title = "Welcome to Pravin Ice cream"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]

