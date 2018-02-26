from django.conf.urls import re_path
from vecurityapiapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # re_path(r'^carowners/$', views.car_owner_list),
    # re_path(r'^carowners/(?P<pk>[0-9]+)/$', views.car_owner_detail), ///todo uncomment when using functions as views
    re_path(r'^carowners/$', views.CarOwnerList.as_view()),
    re_path(r'^carowners/(?P<pk>[0-9]+)/$', views.CarOwnerDetail.as_view()),
    re_path(r'^cars/$', views.CarList.as_view()),
    re_path(r'^cars/(?P<pk>[0-9]+)/$', views.CarDetail.as_view()),
    re_path(r'^addcar/$', views.AddCar.as_view()),
    re_path(r'^ownercars/(?P<oid>[0-9]+)/$', views.OwnerCars.as_view()),
    re_path(r'^login/$', views.CarOwnerLogin.as_view()),
    re_path(r'^guard-login/$', views.GuardLogin.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
