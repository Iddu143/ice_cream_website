"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from home import views
from django.shortcuts import redirect
# from home.views import home_view, order_view, order_success_view
# from .views import order_view
# from home.views import order_view
# from home.views import order_success_view

# from mysite.views import order_view


admin.site.site_header = "Idris Ice Creams-AdminPage"
admin.site.site_title = "Idris Ice Creams Admin Portal"
admin.site.index_title = "Welcome to Idris Ice Creams"


urlpatterns = [
    path("",views.index,name="home"),
    path("admin/", admin.site.urls),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("service2/",views.service2,name="service2"),
    path("familypack/",views.familypack,name="familypack"),
    path("contact",views.contact,name="contact"),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('view/', views.view_item, name='view_item'),
    path('edit/', views.edit_item, name='edit_item'),
    path('order/', views.order_view, name='order'),
    path('success/', views.order_success_view, name='order'),
    # path('order/success/', order_success_view, name='order_success'),
    # path('order/success/', redirect('/success/'), name='order_success'),
    # path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('success/', views.success, name='success'),
    # path('error/', views.error, name='error'),
    # path("submitcontact",views.contact,name="contact"),
]
