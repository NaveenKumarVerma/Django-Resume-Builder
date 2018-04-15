from django.conf.urls import url
from .import views

urlpatterns = [
    # url(r'^$', ,),
    url(r'^resumefill', views.resumeFill, name='resume_fill'),
    url(r'^resumeview', views.resumeView, name='resume_view'),


]
