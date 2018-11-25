"""
Definition of urls for WebSiteProject.
"""

from django.conf.urls import include, url
import WebSiteApp.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', WebSiteApp.views.index, name='index'),
    url(r'^home$', WebSiteApp.views.index, name='home'),
]