from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #################################################################
    # Question 1
    #
    # REPLACE THE BELOW LINE with the correct view and URL for the about page
    url(r'^about/$', views.about, name='about'),
    #################################################################
    # Question 2
    #
    # Notice the (?P<pk>\d+) in the URL.
    # This captures any numberic value in that part of the URL and passes the number as a parameter
    # named 'pk' to the URL's view function.
    #
    # REPLACE THE BELOW LINE with the correct view and URL for the post details page
    url(r'^details/(?P<pk>\d+)$', views.post_details, name='post_details'),
    url(r'^add/', views.add, name='add')
]
