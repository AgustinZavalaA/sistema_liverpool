"""Sistema_Liverpool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from store_system import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login),
    path("login", views.login, name="login"),
    path("verify", views.verify, name="verify"),
    path("manager", views.manager, name="manager"),
    path("employee", views.employee, name="employee"),
    path("store", views.store, name="store"),
    path("purchase/<int:id>", views.purchase, name="purchase"),
    path("sell_product/<int:id>", views.sell_product, name="sell"),
    path("add", views.add, name="add"),
    path("add_product", views.add_product, name="add_product"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("del_product/<int:id>", views.del_product, name="del_product"),
    path("update/<int:id>", views.update, name="update"),
    path("upd_product/<int:id>", views.upd_product, name="upd_product"),
    path("register", views.register, name="register"),
    path("add_user", views.add_user, name="add_user"),
]
