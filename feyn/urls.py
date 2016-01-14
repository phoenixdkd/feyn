"""feyn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings
import os
from feyn_admin import urls as feyn_admin_urls
from cmb_demo import urls as cmb_demo_urls
from django.conf.urls.static import static

urlpatterns = [
    # default admin
    url(r'^admin/', include(admin.site.urls)),

    # cmb report demo
    url(r'^demo/cmb/', include(cmb_demo_urls)),

    # app feyn_admin [default]
    url(r'', include(feyn_admin_urls)),
]
