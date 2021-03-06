"""polar_line URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    # Admin and Home URLs
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    # Authentication
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('signup/', views.signup_user, name='signup_user'),

    # Account URLs
    path('account/', views.account, name='account'),
    path('account/profile', views.profile, name='profile'),
    path('account/profile/edit', views.edit_profile, name='edit_profile'),
    path('account/address', views.address, name='address'),
    path('account/address/edit', views.edit_address, name='edit_address'),

    # Shop URLs
    path('shop/', views.shop, name='shop'),
    path('details/<int:product_id>', views.details, name='details'),

    # Cart URLs
    path('cart/', views.cart, name='cart'),
    path('cart/<int:cart_id>/remove', views.remove_item, name='remove_item'),
    path('cart/<int:cart_id>/increment', views.increment_item, name='increment_item'),
    path('cart/<int:cart_id>/decrement', views.decrement_item, name='decrement_item'),

    # Contact Us URLs
    path('contact/', views.contact_us, name='contactus'),

]
# Adding STATIC to URL Patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Adding MEDIA to URL Patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
