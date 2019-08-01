from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'weather', views.WeatherViewSet)

urlpatterns = router.urls