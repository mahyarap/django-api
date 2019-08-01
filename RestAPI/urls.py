from django.conf.urls import url
from rest_framework import routers

from . import views


urlpatterns = [
    url(r'erase/$', views.EraseAPIView.as_view()),
    url(r'erase/(?P<pk>[^/.]+)/$', views.EraseAPIView.as_view()),
]

router = routers.SimpleRouter()
router.register(r'weather', views.WeatherViewSet)
urlpatterns += router.urls
