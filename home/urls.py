from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Idris Ice Creams Admin"
admin.site.site_title = "Idris Ice Creams Admin Portal"
admin.site.index_title = "Welcome to Idris Ice Creams"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
