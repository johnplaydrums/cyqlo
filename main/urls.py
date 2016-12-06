""" URLs for main app """

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_view', views.login_view, name='login_view'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^logout_view', views.logout_view, name='logout_view'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^about', views.about, name='about'),
    url(r'^routes_page', views.routes_page, name='routes_page'),
    url(r'^west_side_route', views.west_side_route, name='west_side_route'),
    url(r'^bronx_green_lands', views.bronx_green_lands, name='bronx_green_lands'),
    url(r'^shore_parkway_route', views.shore_parkway_route, name='shore_parkway_route'),
    url(r'^pizza_tour_route', views.pizza_tour_route, name='pizza_tour_route'),
    url(r'^cunningham_park_trail', views.cunningham_park_trail, name='cunningham_park_trail'),
    url(r'^columbuscircle_bearmtn_route', views.columbuscircle_bearmtn_route, name='columbuscircle_bearmtn_route'),
    url(r'^harlem_soulfood_tour', views.soulfoodHarlem, name='soulfoodHarlem'),
]
